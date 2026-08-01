#!/usr/bin/env python3
"""
wordlist_b64.py

For each line in a wordlist file, appends it to a static base string,
base64-encodes the resulting string, and writes each encoded value
to an output file (one per line).

Usage:
    python3 wordlist_b64.py -w wordlist.txt -o output.txt
    python3 wordlist_b64.py -w wordlist.txt -o output.txt -s "prefix_"
"""

import argparse
import base64
import sys

# Default static string that each wordlist line is appended to.
STATIC_STRING = "base_string_"


def process_wordlist(wordlist_path: str, output_path: str, static_string: str) -> int:
    """
    Reads each line from wordlist_path, appends it to static_string,
    base64-encodes the result, and writes it to output_path.

    Returns the number of lines processed.
    """
    count = 0
    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as infile, \
             open(output_path, "w", encoding="utf-8") as outfile:

            for line in infile:
                word = line.rstrip("\n\r")
                if not word:
                    continue  # skip blank lines

                combined = f"{static_string}{word}"
                encoded = base64.b64encode(combined.encode("utf-8")).decode("utf-8")

                outfile.write(encoded + "\n")
                count += 1

    except FileNotFoundError:
        print(f"Error: wordlist file not found: {wordlist_path}", file=sys.stderr)
        sys.exit(1)
    except OSError as e:
        print(f"Error handling files: {e}", file=sys.stderr)
        sys.exit(1)

    return count


def main():
    parser = argparse.ArgumentParser(
        description="Append each wordlist line to a static string, base64 encode, and write to a file."
    )
    parser.add_argument(
        "-w", "--wordlist", required=True,
        help="Path to the input wordlist file (one entry per line)."
    )
    parser.add_argument(
        "-o", "--output", required=True,
        help="Path to the output file where base64 strings will be written."
    )
    parser.add_argument(
        "-s", "--static-string", default=STATIC_STRING,
        help=f"Static string to prepend to each wordlist entry (default: '{STATIC_STRING}')."
    )

    args = parser.parse_args()

    total = process_wordlist(args.wordlist, args.output, args.static_string)
    print(f"Processed {total} entries. Base64 output written to: {args.output}")


if __name__ == "__main__":
    main()
