import csv
from Bio.Seq import Seq

def getsubsequence(MS11Seq_String, up_start, up_stop):
    upsubsequence= MS11Seq_String[up_start:up_stop-1]
    return upsubsequence

with open('pubMLSTms11.fa') as f:
    MS11Seq=""
    for line in f:
        if not line.startswith('>'):
            MS11Seq += line.strip()
with open('MS11Seq.txt', 'w') as f:
    f.write(MS11Seq)
with open("MS11Seq.txt", 'r') as f:
    MS11Seq_String = f.read()

#upstreamseq
with open('MS11Forward.csv', 'r') as MS11Forward:
    with open('MS11ForwardUpstreamSeq.csv', 'w', newline='') as MS11ForUp_sequence:
        writer = csv.writer(MS11ForUp_sequence)
        reader = csv.reader(MS11Forward)

        # header row in output file
        header_row = next(reader)
        header_row.append('upsequence')
        writer.writerow(header_row)

        #loop through to get the start and stop
        for row in reader:
            up_start = int(row[6])
            up_stop = int(row[7])
            upsubsequence = getsubsequence(MS11Seq_String, up_start, up_stop)
            upsequence = upsubsequence
            row.append(upsequence)
            writer.writerow(row)


def getsubsequence(MS11Seq_String, down_start, down_stop):
    downsubsequence= MS11Seq_String[down_start:down_stop-1]
    return downsubsequence

#downstream seq
with open('MS11Forward.csv', 'r') as MS11Forward:
    with open('MS11ForwardUpstreamSeq.csv', 'w', newline='') as MS11ForUp_sequence:
        writer = csv.writer(MS11ForUp_sequence)
        reader = csv.reader(MS11Forward)

        # header row in output file
        header_row = next(reader)
        header_row.append('downstream')
        writer.writerow(header_row)

        #loop through to get the start and stop
        for row in reader:
            down_start = int(row[8])
            down_stop = int(row[9])
            downsubsequence = getsubsequence(MS11Seq_String, down_start, down_stop)
            downsequence = (downsubsequence)
            row.append(downsequence)
            writer.writerow(row)


#whole seq

import csv

kan_primer = 'GCATTGAGCTAGTCAGTGAG'
#primer sequence between upstream and barcode
kan_cassette = 'TTAATTAAATGGCGATAGCTAGACTGGGCGGTTTTATGGACAGCAAGCGAACCGGAATTGCCAGCTGGGGCGCCCTCTGGTAAGGTTGGGAAGCCCTGCAAAGTAAACTGGATGGCTTTCTTGCCGCCAAGGATCTGATGGCGCAGGGGATCAAATCTGATCAAGAGACAGGATGAGGATCGTTTCGCATGATTGAACAAGATGGATTGCACGCAGGTTCTCCGGCCGCTTGGGTGGAGAGGCTATTCGGCTATGACTGGGCACAACAGACAATCGGCTGCTCTGATGCCGCCGTGTTCCGGCTGTCAGCGCAGGGGCGCCCGGTTCTTTTTGTCAAGACCGACCTGTCCGGTGCCCTGAATGAACTCCAAGACGAGGCAGCGCGGCTATCGTGGCTGGCCACGACGGGCGTTCCTTGCGCAGCTGTGCTCGACGTTGTCACTGAAGCGGGAAGGGACTGGCTGCTATTGGGCGAAGTGCCGGGGCAGGATCTCCTGTCATCTCACCTTGCTCCTGCCGAGAAAGTATCCATCATGGCTGATGCAATGCGGCGGCTGCATACGCTTGATCCGGCTACCTGCCCATTCGACCACCAAGCGAAACATCGCATCGAGCGAGCACGTACTCGGATGGAAGCCGGTCTTGTCGATCAGGATGATCTGGACGAAGAGCATCAGGGGCTCGCGCCAGCCGAACTGTTCGCCAGGCTCAAGGCGCGGATGCCCGACGGCGAGGATCTCGTCGTGACCCATGGCGATGCCTGCTTGCCGAATATCATGGTGGAAAATGGCCGCTTTTCTGGATTCATCGACTGTGGCCGGCTGGGTGTGGCGGACCGCTATCAGGACATAGCGTTGGCTACCCGTGATATTGCTGAAGAGCTTGGCGGCGAATGGGCTGACCGCTTCCTCGTGCTTTACGGTATCGCCGCTCCCGATTCGCAGCGCATCGCCTTCTATCGCCTTCTTGACGAGTTCTTCTGATTCAGACGGCATGCGGCCGC'
# includeskan cassette (Pac1 +promoter+kanr+Dus+Not1)


with open('MS11Forward.csv', 'r') as MS11Forward_updown:
    with open('MS11ForFullConstructSeq.csv', 'w', newline='') as MS11For_full:
        writer = csv.writer(MS11For_full)
        reader = csv.reader(MS11Forward_updown)

        # header row in output file
        header_row = next(reader)
        header_row.append('fullconstruct')
        writer.writerow(header_row)

        #loop through to get the start and stop
        for row in reader:
            up = row[10]
            down = row[11]
            barcode = row[12]
            fullconstruct = up + kan_primer + barcode + kan_cassette + down
            row.append(fullconstruct)
            writer.writerow(row)