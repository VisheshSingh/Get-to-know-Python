# ipsum_file = open('files/ipsum.txt')

# for line in ipsum_file:
#     #print(line)
#     print(line.rstrip())


# ipsum_file.seek(0)
# lines = ipsum_file.readlines()
# print(lines)


# ipsum_file.seek(50)
# lines = ipsum_file.readlines(100)
# print(lines)

# ipsum_file.close()


def seq_filter(line):
    return '>' not in line

with open('files/dna_sequence.txt') as dna_seq:
    lines = dna_seq.readlines()
    print(list(filter(seq_filter, lines)))