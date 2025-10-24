"""
Automated translation script for VIA research document.
Translates remaining German sections in the English document to English.
Uses Claude API for high-quality translations.
"""

import anthropic
import os
import re
from pathlib import Path
import sys

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

def detect_german_paragraphs(text):
    """Detect paragraphs that contain German text."""
    # Split by double newlines to get paragraphs
    paragraphs = text.split('\n\n')
    german_paragraphs = []

    for i, para in enumerate(paragraphs):
        # Skip code blocks, URLs, references
        if para.startswith('```') or para.startswith('http') or para.startswith('[^'):
            continue

        # Check for German indicators
        german_indicators = [
            r'\bDie\b', r'\bDer\b', r'\bDas\b', r'\bEin\b', r'\bEine\b',
            r'\bund\b', r'\boder\b', r'\baber\b', r'\bmit\b', r'\bvon\b',
            r'\bzu\b', r'\bim\b', r'\bam\b', r'\bdes\b', r'\bdem\b',
            r'\bwird\b', r'\bwerden\b', r'\bist\b', r'\bsind\b',
            r'\bkann\b', r'\bsoll\b', r'\bmuss\b', r'\berfolgt\b',
            r'\bfür\b', r'\bdurch\b', r'\bals\b', r'\bwährend\b'
        ]

        # Check if paragraph contains German
        for indicator in german_indicators:
            if re.search(indicator, para):
                german_paragraphs.append((i, para))
                break

    return german_paragraphs

def translate_paragraph(german_text):
    """Translate a German paragraph to English using Claude API."""
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4000,
        messages=[{
            "role": "user",
            "content": f"""Translate the following German text to English. This is part of a technical research document about industrial automation and compiler design.

Requirements:
- Maintain all technical terms unchanged (VIA, AAS, OPC UA, IPC, M3/M2/M1, etc.)
- Keep all code snippets, file paths, and formatting unchanged
- Preserve markdown formatting
- Use professional academic English
- Keep references and citations in original format
- Maintain the same structure and paragraph breaks

German text:
{german_text}

Provide ONLY the English translation without any explanations or preamble."""
        }]
    )

    return message.content[0].text

def main():
    print("Starting automated translation...")
    print(f"Reading file: {ENGLISH_FILE}")

    # Read the current English file
    with open(ENGLISH_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Detect German paragraphs
    print("\nDetecting German paragraphs...")
    german_paragraphs = detect_german_paragraphs(content)
    print(f"Found {len(german_paragraphs)} paragraphs with German content")

    if not german_paragraphs:
        print("No German content found! Document appears to be fully translated.")
        return

    # Split content into paragraphs for processing
    paragraphs = content.split('\n\n')

    # Translate each German paragraph
    print("\nStarting translation process...")
    translated_count = 0

    for idx, german_para in german_paragraphs:
        print(f"\nTranslating paragraph {translated_count + 1}/{len(german_paragraphs)}...")
        print(f"Preview: {german_para[:100]}...")

        try:
            # Translate
            english_translation = translate_paragraph(german_para)

            # Replace in paragraphs array
            paragraphs[idx] = english_translation.strip()

            translated_count += 1
            print(f"✓ Translated successfully")

            # Progress update every 10 paragraphs
            if translated_count % 10 == 0:
                print(f"\n--- Progress: {translated_count}/{len(german_paragraphs)} paragraphs translated ---")

        except Exception as e:
            print(f"✗ Error translating paragraph: {e}")
            print(f"Keeping original German text for manual review")

    # Reconstruct the document
    print("\nReconstructing document...")
    translated_content = '\n\n'.join(paragraphs)

    # Write back to file
    print(f"Writing translated content to: {ENGLISH_FILE}")
    with open(ENGLISH_FILE, 'w', encoding='utf-8') as f:
        f.write(translated_content)

    print(f"\n✓ Translation complete!")
    print(f"  - Total paragraphs translated: {translated_count}")
    print(f"  - Output file: {ENGLISH_FILE}")
    print("\nPlease review the translated document and commit the changes.")

if __name__ == "__main__":
    main()
