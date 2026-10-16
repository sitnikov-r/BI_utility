#Converts bounds to tuple. Return (0, value) if a single number is given.
def parse_bounds(bounds):
    if isinstance(bounds, (int, float)):
        return (0, bounds)
    return bounds

#Calculate GC content percentage.
def calc_gc_content(seq):
    if len(seq) == 0:
        return 0.0

    gc_count = 0
    for nucleotide in seq:
        if nucleotide == "G" or nucleotide == "C":
            gc_count += 1

    return (gc_count / len(seq)) * 100

def chech_gc_bounds(seq, gc_bounds):
    #Checks if GC content is within bounds.
    gc_content = calc_gc_count(seq)
    lower, upper = gc_bounds
    if lower <= gc_content <= upper:
        return True
    return False

def check_length_bounds(seq, length_bouds):
    #Checks if sequence length is within bounds. Return bool.
    seq_len = len(seq)
    lower, upper = length_bouds
    if lower <= seq_len <= upper:
        return True
    return False

def calc_avg_quality(qual_str):
    #Calculates average read quality (Phred33)
    if len(qual_str) == 0:
        return 0.0

    total_quality = 0
    for char in qual_str:
        total_quality += ord(char) - 33

    return total_quality / len(qual_str)

def check_quality_threshold(qual_str, quality_threshold):
    #Checks if average quality is above threshold. Return bool.
    avg_quality = calc_avg_quality(qual_str)
    if avg_quality >= quality_threshold:
        return True
    return False
