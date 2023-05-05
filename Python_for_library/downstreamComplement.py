import csv


def get_complement(seq):
    complement_dict = {'a': 't', 't': 'a', 'c': 'g', 'g': 'c'}
    return ''.join([complement_dict[base] for base in reversed(seq)])

with open('MS11ReversedownstreamSeq.csv', 'r') as downstream_seq:
    with open('MS11Rev_Downstream_complementSeq.csv','w', newline='') as down_complement:
        writer = csv.writer(down_complement)

        reader = csv.reader(downstream_seq)

        header_row = next(reader)
        header_row.append('downcomplement')
        writer.writerow(header_row)

        for row in reader:
            seq = row[10]
            complement = get_complement(seq)
            downComplement = complement
            row.append(downComplement)
            writer.writerow(row)
            