# sanger-fasta-merge

Joins many Sanger FASTA files into one FASTA file. Sequences are copied as they are, in alphabetical order of the file names. Nothing is edited.

## Run

No installation is needed beyond Python 3. Open PowerShell in the folder that holds the FASTA files and run:

```
python merge_fasta.py
```

Or point it at a folder:

```
python merge_fasta.py path\to\reads
```

The output is `combined.fasta` in the folder where you ran the command. The terminal prints the number of files and sequences. The sequence count should match your own count.

## Try it

```
python merge_fasta.py example_data
```

## Notes

- Reads files ending in `.fasta`, `.fas` or `.fa`.
- Each file must have its own `>` header line.
- A newline is added after each file, so the last line of one file never joins the header of the next.
- Headers are not changed. Duplicate headers across files stay duplicated, so check for them before using aligners or BLAST.

## Licence

MIT
