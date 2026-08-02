# CharpendTo64

A small Python tool that prepends a static string (default: `base_string_`) to each line of a wordlist and Base64-encodes the result. Useful for quickly generating Base64-encoded wordlist variants (e.g., for payload/credential fuzzing during authorized security testing).

## Usage

```
usage: wordlist_b64.py [-h] -w WORDLIST -o OUTPUT [-s STATIC_STRING]

options:
  -h, --help            show this help message and exit
  -w WORDLIST, --wordlist WORDLIST
                        Path to the input wordlist file
  -o OUTPUT, --output OUTPUT
                        Path to write the Base64-encoded output
  -s STATIC_STRING, --static-string STATIC_STRING
                        Static string to prepend to each wordlist entry (default: 'base_string_')
```

## Example

```
python3 wordlist_b64.py -w wordlist.txt -o output.txt -s "prefix_"
```

Each line in `wordlist.txt` has the static string prepended, and the resulting value is Base64-encoded and written to `output.txt`.
