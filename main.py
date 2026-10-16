import os
from helpers_fastq import (parse_bounds, chech_gc_bounds, check_length_bounds, check_quality_threshold)
from helpers_bio_files import (convert_multiline_fasta_to_oneline, parse_blast_output)


def filter_fastq(input_fastq, output_fastq, gc_bounds=(0,100), length_bounds=(0, 2**32), quality_theshold=0):
   
   """Filters FASTQ file by parameters: 
    -input_fastq - path to input FASTQ file;
    -output_fastq - output file name;
    -gc_bounds - GC content bounds (default (0, 100));
    -length_bounds - length bounds (default (0, 2**32)):
    -quality_threshold - quality theshold (default 0).
    """
   
   gc_bounds = parse_bounds(gc_bounds)
   length_bounds = parse_bounds(length_bounds)

   
   output_dir = "filtered"
   if not os.path.exists(output_dir):
      os.makedirs(output_dir)

   output_path = os.path.join(output_dir, output_fastq)


   with open(input_fastq, 'r') as infile, open(output_path, 'w') as outfile:
      while True:
         line1 = infile.readline()
         if not line1:
            break
         line2 = infile.readline()
         line3 = infile.readline()
         line4 = infile.readline()

         if not line4:
            break
         
         seq = line2.strip()
         qual = line4.strip()

         is_lenght_ok = check_length_bounds(seq, length_bounds)
         is_gc_ok = check_gc_bounds(seq, gc_bounds)
         is_quality_ok = chech_quality_threshold(qual, quality_theshold)

         if is_lenght_ok and is_gc_ok and is_quality_ok:
            outfile.write(line1)
            outfile.write(line2)
            outfile.write(line3)
            outfile.write(line4)


if __name__ == "__main__":
   
   """Main entry point"""

   print('Биоинформатические улиты готовы к работе.')
