"""provides analysis on DNA sequences"""



def ATGC_content(DNA):
    """returns ATGC contents in the form of a dict"""
    ATGCDict = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
    for nucleotide in DNA:
        try:
            ATGCDict[nucleotide] += 1
        except KeyError:
            pass
    return ATGCDict


def complementary(DNA):
    """Given a DNA sequence, will return a complementary DNA sequence"""
    cDNA = []
    complementary = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    for nucleotide in DNA:
        try:
            cDNA.append(complementary[nucleotide])
        except KeyError:
            cDNA.append('X')
    
    # Return cDNA as string instead of list. Remove if list is prefered
    cDNA = ''.join(cDNA)
    
    return cDNA

# Function that determines what RNA sequence is made from a DNA sequence
def DNA2RNA(DNA_sequence): #Needs to be a string
    """Theory: When a gene is read, only one strand is read and transcribed to mRNA.
    The mRNA that is transcribed is the complimentary of the read strand, the anti-sense strand.
    However, you have to take in account for the direction of transcription and translation of the strand (5' to 3').
    The the sense strand (coding strand) has the same sequence as the mRNA but with U instead of T.
    Simplified solution: The coding strand (the gene) is the same as the mRNA sequence, but with U instead of T."""    
    
    # Simply replacing T with U
    mRNA_sequence = DNA_sequence.replace('T','U')
    
    return mRNA_sequence


def hamming_differences(DNA1, DNA2):
    """Returns info on positional/nucleotide differences in 2 DNA strands in
    the form of a list"""
    hDiff = []

    if len(DNA1) > len(DNA2):
        for i in range(len(DNA1)):
            DNA2 += 'X'
    else:
        for i in range(len(DNA2)):
            DNA1 += 'X'
    for n1, n2 in list(zip(DNA1, DNA2)):
        if n1 != n2:
            locDiff = list(zip(DNA1, DNA2)).index((n1, n2))
            nucDiff = n1 + n2
            print(str(locDiff) + nucDiff)
            hDiff.append(str(locDiff) + nucDiff)
    return hDiff
