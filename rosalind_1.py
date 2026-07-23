def count_bases(dna):
    return {base: dna.count(base) for base in "ACGT"}


# Rosalind problem 1 sample. Known answer: A=20 C=12 G=17 T=21.
sequence = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

counts = count_bases(sequence)
for base in "ACGT":
    print(f"{base}={counts[base]}")
