import anthropic
import time
import os
import re
from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
from anthropic.types.messages.batch_create_params import Request

# Konstanten für Limits
CHAR_LIMIT = 200000
TOKEN_LIMIT = 64000
# Konservative Schätzung: ~4 Zeichen pro Token
CHARS_PER_TOKEN = 4


def split_markdown_sections(text, char_limit=CHAR_LIMIT):
    """
    Teilt Markdown-Text in Abschnitte auf, die unter dem Zeichenlimit bleiben.
    Berücksichtigt Markdown-Überschriften und Absätze.
    """
    # Markdown-Überschriften und Absätze als Trennpunkte
    sections = []
    current_section = []
    current_length = 0

    # Text in Zeilen aufteilen
    lines = text.split('\n')

    for line in lines:
        line_length = len(line) + 1  # +1 für Newline

        # Prüfen ob eine neue Überschrift beginnt
        is_heading = re.match(r'^#+\s', line)

        # Wenn Limit überschritten würde und es ein guter Trennpunkt ist
        if current_length + line_length > char_limit and current_section:
            # Aktuellen Abschnitt speichern
            sections.append('\n'.join(current_section))
            current_section = [line]
            current_length = line_length
        else:
            current_section.append(line)
            current_length += line_length

    # Letzten Abschnitt hinzufügen
    if current_section:
        sections.append('\n'.join(current_section))

    return sections


def create_translation_batch(client, text_segments, source_lang, target_lang, batch_prefix="translation"):
    """
    Erstellt einen Batch-Job für mehrere Textsegmente.
    """
    requests = []

    for idx, segment in enumerate(text_segments):
        translation_prompt = (
            f"Translate this text from {source_lang} to {target_lang}. "
            f"Maintain the exact Markdown formatting. "
            f"Gib ausschließlich den übersetzten Text als Ergebnis aus. "
            f"Füge keine Kommentare, Erklärungen oder zusätzlichen Text hinzu.\n\n{segment}"
        )

        requests.append(
            Request(
                custom_id=f"{batch_prefix}_{idx}",
                params=MessageCreateParamsNonStreaming(
                    model="claude-sonnet-4-5",
                    max_tokens=TOKEN_LIMIT,
                    messages=[{
                        "role": "user",
                        "content": translation_prompt
                    }]
                )
            )
        )

    batch = client.messages.batches.create(requests=requests)
    return batch.id


def wait_for_batch(client, batch_id):
    """
    Wartet auf Abschluss eines Batch-Jobs.
    """
    print(f"Warte auf Batch {batch_id}...")

    while True:
        batch_status = client.messages.batches.retrieve(batch_id)

        if batch_status.processing_status == "ended":
            print(f"Batch {batch_id} abgeschlossen!")
            return True
        elif batch_status.processing_status == "failed":
            print(f"Batch {batch_id} fehlgeschlagen!")
            return False
        else:
            print(f"Status: {batch_status.processing_status}")
            time.sleep(5)


def get_batch_results(client, batch_id, num_segments):
    """
    Holt die Ergebnisse eines Batch-Jobs in der richtigen Reihenfolge.
    """
    results = {}

    for result in client.messages.batches.results(batch_id):
        if result.result.type == "succeeded":
            # Custom ID extrahieren (z.B. "translation_0" -> 0)
            custom_id = result.custom_id
            idx = int(custom_id.split('_')[-1])
            results[idx] = result.result.message.content[0].text
        else:
            print(f"Fehler bei {result.custom_id}: {result.result}")
            return None

    # Ergebnisse in richtiger Reihenfolge zusammenfügen
    ordered_results = [results[i] for i in range(num_segments) if i in results]

    if len(ordered_results) != num_segments:
        print(f"Warnung: Nur {len(ordered_results)} von {num_segments} Segmenten erhalten!")
        return None

    return '\n\n'.join(ordered_results)


def find_differences(original, back_translated):
    """
    Findet Unterschiede zwischen Original und Rückübersetzung.
    Einfache zeilenbasierte Differenzanalyse.
    """
    orig_lines = original.split('\n')
    back_lines = back_translated.split('\n')

    differences = []
    max_lines = max(len(orig_lines), len(back_lines))

    for i in range(max_lines):
        orig_line = orig_lines[i] if i < len(orig_lines) else "[FEHLT]"
        back_line = back_lines[i] if i < len(back_lines) else "[FEHLT]"

        if orig_line.strip() != back_line.strip():
            differences.append({
                'line': i + 1,
                'original': orig_line,
                'back_translated': back_line
            })

    return differences


def display_differences(differences, max_display=20):
    """
    Zeigt Unterschiede zwischen Original und Rückübersetzung an.
    """
    if not differences:
        print("\n✓ Keine Unterschiede gefunden! Übersetzung scheint korrekt zu sein.")
        return

    print(f"\n⚠ {len(differences)} Unterschiede gefunden:")
    print("=" * 80)

    for i, diff in enumerate(differences[:max_display]):
        print(f"\nZeile {diff['line']}:")
        print(f"  Original:        {diff['original'][:100]}")
        print(f"  Rückübersetzt:   {diff['back_translated'][:100]}")

    if len(differences) > max_display:
        print(f"\n... und {len(differences) - max_display} weitere Unterschiede")


def translate_with_validation(client, text, source_lang, target_lang):
    """
    Führt Übersetzung mit Validierung durch Rückübersetzung durch.
    """
    print("\n" + "=" * 80)
    print("SCHRITT 1: Text in Segmente aufteilen")
    print("=" * 80)

    # Text in Segmente aufteilen
    segments = split_markdown_sections(text, CHAR_LIMIT - 1000)  # Puffer für Prompt
    print(f"Text wurde in {len(segments)} Segmente aufgeteilt:")
    for i, seg in enumerate(segments):
        print(f"  Segment {i + 1}: {len(seg)} Zeichen")

    # Prüfen, ob einzelne Segmente zu groß sind
    for i, seg in enumerate(segments):
        estimated_tokens = len(seg) / CHARS_PER_TOKEN
        if estimated_tokens > TOKEN_LIMIT * 0.9:  # 90% als Sicherheitsgrenze
            print(f"⚠ Warnung: Segment {i + 1} könnte Token-Limit überschreiten!")

    print("\n" + "=" * 80)
    print("SCHRITT 2: Übersetzung von {} nach {}".format(source_lang, target_lang))
    print("=" * 80)

    # Erste Übersetzung
    batch_id = create_translation_batch(client, segments, source_lang, target_lang, "forward")

    if not wait_for_batch(client, batch_id):
        print("Fehler bei der Übersetzung!")
        return None, None, None

    translated_text = get_batch_results(client, batch_id, len(segments))

    if not translated_text:
        print("Fehler beim Abrufen der Übersetzung!")
        return None, None, None

    print("\n✓ Übersetzung abgeschlossen!")
    print(f"Übersetzter Text: {len(translated_text)} Zeichen")

    print("\n" + "=" * 80)
    print("SCHRITT 3: Rückübersetzung zur Validierung")
    print("=" * 80)

    # Rückübersetzung
    back_segments = split_markdown_sections(translated_text, CHAR_LIMIT - 1000)
    print(f"Übersetzter Text in {len(back_segments)} Segmente aufgeteilt")

    back_batch_id = create_translation_batch(client, back_segments, target_lang, source_lang, "backward")

    if not wait_for_batch(client, back_batch_id):
        print("Fehler bei der Rückübersetzung!")
        return translated_text, None, None

    back_translated_text = get_batch_results(client, back_batch_id, len(back_segments))

    if not back_translated_text:
        print("Fehler beim Abrufen der Rückübersetzung!")
        return translated_text, None, None

    print("\n✓ Rückübersetzung abgeschlossen!")

    print("\n" + "=" * 80)
    print("SCHRITT 4: Qualitätsprüfung")
    print("=" * 80)

    # Unterschiede finden
    differences = find_differences(text, back_translated_text)

    # Unterschiede anzeigen
    display_differences(differences)

    # Qualitätsbewertung
    total_lines = len(text.split('\n'))
    error_rate = len(differences) / total_lines if total_lines > 0 else 0

    print(f"\n📊 Qualitätsmetriken:")
    print(f"  Gesamtzeilen: {total_lines}")
    print(f"  Unterschiede: {len(differences)}")
    print(f"  Fehlerrate: {error_rate * 100:.2f}%")

    if error_rate < 0.05:
        quality = "AUSGEZEICHNET"
    elif error_rate < 0.15:
        quality = "GUT"
    elif error_rate < 0.30:
        quality = "AKZEPTABEL"
    else:
        quality = "UNZUREICHEND"

    print(f"  Qualität: {quality}")

    return translated_text, back_translated_text, differences


def simple_query():
    """Einfache Anfrage an Claude ohne Übersetzung"""
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        api_key = input("Bitte geben Sie Ihren Anthropic API-Key ein: ").strip()

    if not api_key:
        print("Fehler: Kein API-Key angegeben!")
        return

    client = anthropic.Anthropic(api_key=api_key)

    print("Bitte geben Sie Ihre Anfrage ein.")
    print("Beenden Sie die Eingabe mit einer Zeile, die nur '###END###' enthält:")
    print("-" * 50)

    lines = []
    while True:
        line = input()
        if line.strip() == "###END###":
            break
        lines.append(line)

    prompt = "\n".join(lines)

    print("\nErstelle Batch-Anfrage...")

    batch = client.messages.batches.create(
        requests=[
            Request(
                custom_id="simple_query_request",
                params=MessageCreateParamsNonStreaming(
                    model="claude-sonnet-4-5",
                    max_tokens=64000,
                    messages=[{
                        "role": "user",
                        "content": prompt
                    }]
                )
            )
        ]
    )

    batch_id = batch.id
    print(f"Batch erstellt mit ID: {batch_id}")

    if not wait_for_batch(client, batch_id):
        return

    print("\n" + "=" * 50)
    print("ERGEBNIS:")
    print("=" * 50)

    for result in client.messages.batches.results(batch_id):
        if result.result.type == "succeeded":
            print(result.result.message.content[0].text)
        else:
            print(f"Fehler: {result.result}")


def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        api_key = input("Bitte geben Sie Ihren Anthropic API-Key ein: ").strip()

    if not api_key:
        print("Fehler: Kein API-Key angegeben!")
        return

    client = anthropic.Anthropic(api_key=api_key)

    # Eingabesprache abfragen
    source_language = input("Bitte geben Sie die Eingabesprache ein (z.B. 'Deutsch', 'German'): ")

    # Zielsprache abfragen
    target_language = input("Bitte geben Sie die Zielsprache ein (z.B. 'Englisch', 'English'): ")

    # Option: Text aus Datei laden
    load_from_file = input("\nMöchten Sie den Text aus einer Datei laden? (j/n): ")

    if load_from_file.lower() in ['j', 'ja', 'y', 'yes']:
        file_path = input("Bitte geben Sie den Dateipfad ein: ")
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                text_to_translate = f.read()
            print(f"✓ Text geladen: {len(text_to_translate)} Zeichen")
        except Exception as e:
            print(f"Fehler beim Laden der Datei: {e}")
            return
    else:
        # Text zur Übersetzung abfragen - Multiline-Unterstützung
        print("\nBitte geben Sie den zu übersetzenden Text ein.")
        print("Beenden Sie die Eingabe mit einer Zeile, die nur '###END###' enthält:")
        print("-" * 50)

        lines = []
        while True:
            line = input()
            if line.strip() == "###END###":
                break
            lines.append(line)

        text_to_translate = "\n".join(lines)

    # Übersetzung mit Validierung durchführen
    translated_text, back_translated_text, differences = translate_with_validation(
        client, text_to_translate, source_language, target_language
    )

    if not translated_text:
        print("\n❌ Übersetzung fehlgeschlagen!")
        return

    print("\n" + "=" * 80)
    print("ÜBERSETZUNGSERGEBNIS:")
    print("=" * 80)
    print(translated_text[:1000])  # Erste 1000 Zeichen anzeigen
    if len(translated_text) > 1000:
        print(f"\n... ({len(translated_text) - 1000} weitere Zeichen)")

    # Benutzerentscheidung
    print("\n" + "=" * 80)
    accept = input("\nAkzeptieren Sie die Übersetzungsqualität? (j/n): ")

    if accept.lower() not in ['j', 'ja', 'y', 'yes']:
        print("Übersetzung verworfen.")
        return

    # Ergebnis speichern
    save_to_file = input("\nMöchten Sie das Ergebnis in einer Datei speichern? (j/n): ")

    if save_to_file.lower() in ['j', 'ja', 'y', 'yes']:
        file_path = input("Bitte geben Sie den gewünschten Dateipfad ein (z.B. 'uebersetzung.md'): ")
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(translated_text)
            print(f"✓ Übersetzung erfolgreich in '{file_path}' gespeichert.")

            # Optional: Detaillierten Report speichern
            save_report = input("Möchten Sie auch einen detaillierten Qualitätsreport speichern? (j/n): ")
            if save_report.lower() in ['j', 'ja', 'y', 'yes']:
                report_path = file_path.replace('.md', '_report.txt')
                with open(report_path, 'w', encoding='utf-8') as f:
                    f.write(f"ÜBERSETZUNGSREPORT\n")
                    f.write("=" * 80 + "\n\n")
                    f.write(f"Von: {source_language}\n")
                    f.write(f"Nach: {target_language}\n")
                    f.write(f"Originalzeichen: {len(text_to_translate)}\n")
                    f.write(f"Übersetzte Zeichen: {len(translated_text)}\n\n")

                    if differences:
                        f.write(f"Gefundene Unterschiede: {len(differences)}\n\n")
                        for diff in differences[:50]:  # Erste 50 Unterschiede
                            f.write(f"Zeile {diff['line']}:\n")
                            f.write(f"  Original: {diff['original']}\n")
                            f.write(f"  Rückübersetzt: {diff['back_translated']}\n\n")

                print(f"✓ Report gespeichert in '{report_path}'")

        except Exception as e:
            print(f"Fehler beim Speichern: {e}")


if __name__ == "__main__":
    print("=" * 80)
    print("CLAUDE BATCH-ÜBERSETZUNGSTOOL MIT QUALITÄTSKONTROLLE")
    print("=" * 80)
    print("\nWählen Sie eine Option:")
    print("1 - Übersetzung mit Validierung")
    print("2 - Einfache Anfrage")
    choice = input("\nIhre Wahl (1 oder 2): ").strip()

    if choice == "1":
        main()
    elif choice == "2":
        simple_query()
    else:
        print("Ungültige Auswahl!")
