import sys
from pathlib import Path

# Folder with the FASTA files: given on the command line, otherwise the current folder
folder = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
output = Path("combined.fasta")

n_files = n_seqs = 0
with open(output, "w", newline="\n") as out:
    for f in sorted(folder.iterdir()):                      # files in alphabetical order
        if f.suffix.lower() not in (".fasta", ".fas", ".fa"):
            continue                                        # only FASTA files
        if f.resolve() == output.resolve():
            continue                                        # never read the output file
        text = f.read_text(encoding="utf-8-sig").strip()    # read the file, trim blank ends
        if not text:
            continue                                        # skip empty files
        out.write(text + "\n")                              # one newline after each file
        n_files += 1
        n_seqs += sum(1 for line in text.splitlines() if line.startswith(">"))

print(f"{n_files} files, {n_seqs} sequences written to {output}")
