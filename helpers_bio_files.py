def convert_multiline_fasta_to_oneline(input_fasta: str, output_fasta: str = None) -> None:
    """
    Converts multiline FASTA to online FASTA.
    Args:
    - input_fasta - path to input FASTA;
    - output_fasta - output FASTA name.
    """

    if output_fasta is None:
        parts = input_fasta.split('.')
        if len(parts) >1:
            output_fasta = parts[0] + '_oneline.' + parts[1]
        else:
            output_fasta = input_fasta + '_oneline.fasta'

    current_header = ""
    current_sequence = ""

    with open(input_fasta, 'r') as infile, open(output_fasta, 'w') as outfile:
        for line in infile:
            line = line.strip()
            if not line:
                continue

            if line.startswith('>'):

                if current_header:
                    outfile.write(current_header + '\n')
                    outfile.write(current_sequence + '\n')

                current_header = line
                current_sequence = ""

            else:

                current_sequence += line

        if current_header:
            outfile.write(current_header + '\n')
            outfile.write(current_sequence + '\n')


def parse_blast_output(input_file: str, output_file: str) -> None:

    """ 
    Extract best hit for each query from BLAST output.
    Args:
    - input_file - path to BLAST output file;
    - output_file - path to save best hits.
    """


    best_matches = []
    is_alignments_section = False

    with open(input_file, 'r') as infile:
        for line in infile:
            line = line.strip()

            if not line:
                continue

            if line.startwith('Query='):
                is_alignments_section = True
                continue

            if "Sequences producing significant aligments:" in line:
                is_alignments_section = True

            if is_alignments_section:
                parts = line.split('  ')
                if parts:
                    best_matches.append(parts[0].strip())
                is_alignments_section = False

    with open(output_file, 'w') as outfile:
        for match in best_matches:
            outfile.write(match + '\n')

