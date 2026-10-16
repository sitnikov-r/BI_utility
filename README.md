# Bioinformatics Utilities

A simple Python package for basic bioinformatics file handling.

## Features

- **FASTQ Filtering:** Filters FASTQ files by GC content, length, and quality.
- **FASTA Conversion:** Converts multiline FASTA files to oneline FASTA format.
- **BLAST Parsing:** Extracts the best hit for each query from BLAST output files.

## Requirements

- Python 3.x
- Standard library only (no external dependencies).

## Project Structure

```text
- /
|-- README.md
|-- main.py
|-- helpers/
    |-- fastq.py
    |-- bio_files.py