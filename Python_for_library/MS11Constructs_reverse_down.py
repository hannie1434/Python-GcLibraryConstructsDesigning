import csv


from Bio.Seq import Seq

def getsubsequence(MS11Seq_String, down_start, down_stop):
    downsubsequence= MS11Seq_String[down_start:down_stop-1]
    return downsubsequence

with open('pubMLSTms11.fa') as f:
    MS11Seq=""
    for line in f:
        if not line.startswith('>'):
            MS11Seq += line.strip()
with open('MS11Seq.txt', 'w') as f:
    f.write(MS11Seq)
with open("MS11Seq.txt", 'r') as f:
    MS11Seq_String = f.read()


with open('MS11Constructs_ReverseForPython.csv', 'r') as MS11Reverse:
    with open('MS11ReversedownstreamSeq.csv', 'w', newline='') as MS11Revdown_sequence:
        writer = csv.writer(MS11Revdown_sequence)
        reader = csv.reader(MS11Reverse)

        # header row in output file
        header_row = next(reader)
        header_row.append('downstream')
        writer.writerow(header_row)

        #loop through to get the start and stop
        for row in reader:
            down_start = int(row[7])
            down_stop = int(row[8])
            downsubsequence = getsubsequence(MS11Seq_String, down_start, down_stop)
            downsequence = (downsubsequence)
            row.append(downsequence)
            writer.writerow(row)
            



