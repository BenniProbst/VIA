"""
Reverse Translation Script: English → German to identify differences
Translates English documentation back to German in chunks to find additions.
Preserves context by tracking paragraph boundaries.
"""

import anthropic
import os
import sys
import re
from pathlib import Path
import difflib

# Set UTF-8 encoding for console output on Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Initialize Claude client with API key from environment
API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
if not API_KEY:
    print("Error: ANTHROPIC_API_KEY environment variable not set")
    sys.exit(1)
client = anthropic.Anthropic(api_key=API_KEY)

# File paths
ENGLISH_FILE = Path(r"C:\Users\benja\OneDrive\Dokumente\Firmensachen\BEP Venture UG\Projekte\VIA\docs\english\PROJECT_DESCRIPTION_AND_RESEARCH.md")
GERMAN_EXPOSE = Path(r"C:\Users\benja\OneDrive\Dokumente\Firmensachen\BEP Venture UG\Projekte\VIA\playbooks\Analyse_eines_Forschungsthemas_Expose.md")
OUTPUT_FILE = Path(r"C:\Users\benja\OneDrive\Dokumente\Firmensachen\BEP Venture UG\Projekte\VIA\english_translated_to_german.md")

# Maximum tokens per request: 64000 (leaving margin for response)
# Maximum characters per request: 200000
MAX_INPUT_TOKENS = 60000  # Conservative limit
MAX_CHARS = 180000  # Conservative limit

def split_by_sections(text):
    """Split document into sections while preserving context."""
    # Split by major headings (## level)
    sections = []
    current_section = []
    lines = text.split('\n')

    for i, line in enumerate(lines):
        # Check if this is a major section header (## followed by number)
        if re.match(r'^## \d+\.', line):
            # Save previous section if it exists
            if current_section:
                sections.append('\n'.join(current_section))
            # Start new section with previous 5 lines for context
            context_start = max(0, i - 5)
            current_section = lines[context_start:i]

        current_section.append(line)

    # Add final section
    if current_section:
        sections.append('\n'.join(current_section))

    return sections

def estimate_tokens(text):
    """Rough estimate: 1 token ≈ 4 characters for English/German."""
    return len(text) // 4

def translate_chunk(english_text, chunk_number, total_chunks):
    """Translate English chunk to German using Claude API."""

    prompt = f"""Translate the following English technical research document excerpt to German. This is chunk {chunk_number} of {total_chunks}.

**Critical Requirements:**
- Translate to professional academic German
- Maintain all technical terms (VIA, AAS, OPC UA, IPC, M3/M2/M1, ROS, etc.) unchanged
- Preserve ALL markdown formatting (headers, lists, tables, code blocks)
- Keep all references, citations, and footnotes intact
- Maintain paragraph structure and spacing
- Translate headings, subheadings, and bullet points
- Do NOT add explanations or preambles
- Output ONLY the German translation

**Context:** This is part of a technical exposé about industrial automation systems.

English text:
{english_text}

Provide ONLY the German translation:"""

    try:
        message = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=16000,
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )

        return message.content[0].text

    except Exception as e:
        print(f"[ERROR] Translation failed for chunk {chunk_number}: {e}")
        return None

def compare_documents(german_reverse_translation, german_original):
    """Compare reverse-translated German with original to find differences."""

    # Split into lines for comparison
    reverse_lines = german_reverse_translation.split('\n')
    original_lines = german_original.split('\n')

    # Use difflib to find differences
    diff = difflib.unified_diff(
        original_lines,
        reverse_lines,
        fromfile='German Exposé (Original)',
        tofile='English → German Translation',
        lineterm=''
    )

    differences = list(diff)

    if differences:
        print("\n" + "="*80)
        print("DIFFERENCES FOUND:")
        print("="*80)
        for line in differences[:100]:  # Show first 100 diff lines
            print(line)
        print(f"\n... ({len(differences)} total diff lines)")
    else:
        print("\n[OK] No significant differences found.")

    return differences

def main():
    print("="*80)
    print("REVERSE TRANSLATION: English → German Comparison")
    print("="*80)
    print(f"English source: {ENGLISH_FILE}")
    print(f"German original: {GERMAN_EXPOSE}")
    print(f"Output: {OUTPUT_FILE}")
    print()

    # Read English document
    print("[1/5] Reading English document...")
    with open(ENGLISH_FILE, 'r', encoding='utf-8') as f:
        english_content = f.read()

    print(f"      English document: {len(english_content)} characters, {len(english_content.split())} words")

    # Split into manageable sections
    print("[2/5] Splitting document into sections...")
    sections = split_by_sections(english_content)
    print(f"      Split into {len(sections)} sections")

    # Translate each section
    print("[3/5] Translating sections to German...")
    translated_sections = []

    for i, section in enumerate(sections, 1):
        section_chars = len(section)
        section_tokens = estimate_tokens(section)

        print(f"\n      Section {i}/{len(sections)}: {section_chars} chars (~{section_tokens} tokens)")

        # Check if section is within limits
        if section_chars > MAX_CHARS or section_tokens > MAX_INPUT_TOKENS:
            print(f"      [WARNING] Section too large, splitting further...")
            # Split by paragraphs
            paragraphs = section.split('\n\n')
            sub_translated = []

            for j, para in enumerate(paragraphs, 1):
                print(f"            Paragraph {j}/{len(paragraphs)}...")
                result = translate_chunk(para, f"{i}.{j}", len(sections))
                if result:
                    sub_translated.append(result)

            translated_sections.append('\n\n'.join(sub_translated))
        else:
            result = translate_chunk(section, i, len(sections))
            if result:
                translated_sections.append(result)
                print(f"      [OK] Translated successfully")
            else:
                print(f"      [ERROR] Translation failed, keeping original")
                translated_sections.append(section)

    # Combine translated sections
    print("\n[4/5] Combining translated sections...")
    full_german_translation = '\n\n'.join(translated_sections)

    # Write output
    print(f"[5/5] Writing output to {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(full_german_translation)

    print(f"      Output: {len(full_german_translation)} characters")

    # Read original German exposé
    print("\n[6/6] Comparing with original German Exposé...")
    with open(GERMAN_EXPOSE, 'r', encoding='utf-8') as f:
        german_original = f.read()

    differences = compare_documents(full_german_translation, german_original)

    print("\n" + "="*80)
    print("TRANSLATION COMPLETE")
    print("="*80)
    print(f"✓ Reverse-translated German saved to: {OUTPUT_FILE}")
    print(f"✓ Found {len(differences)} diff lines")
    print(f"\nNext steps:")
    print(f"1. Review differences to identify English additions")
    print(f"2. Add valuable details back to German Exposé")
    print(f"3. Ensure both documents are synchronized")
    print("="*80)

if __name__ == "__main__":
    main()
