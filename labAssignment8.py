#!/usr/bin/env python

#user defined method that gets the sum of a sequence
def avg(l):
	return sum(l) / len(l)

#fastq file is opened
with open('lab8.fq') as f:
	lines = [line.rstrip() for line in f]

p = open("output.txt","w")

#sequence and quality lists are created
header = []
seq = []
qual = []

#lists seq and qual are populated with sequences and qualities from the fastq file
for i in range(len(lines)):
	if lines[i].startswith('@'):
		header.append(lines[i])
		seq.append(lines[i+1])
		qual.append(lines[i+3])
		i=i+4

#for loop that does all the work
for z in range(0,len(qual)):
	q = []
	for i in qual[z]:
		q.append(ord(i)-33)
	start = []
	stop = []
	x = 0
	while x < len(q):
		j = 0
		average = avg(q[x:x+10])
		if average >= 15:
			x+=1
			continue
		if average < 15:
			while average < 15:
				if ((x+10+j)>125):
					break
				average = avg(q[x:x+10+j])
				j=j+1
			start.append(x)
			stop.append(x+1)
		x = x+10+j

	start = start[::-1]
	stop = stop[::-1]
	newSeq = list(seq[z])
	newQual = list(qual[z])

	for c in range(0,len(start)):
		del newSeq[start[c]:stop[c]]
		del newQual[start[c]:stop[c]]
	
        #stuff is printed to output file
        p.write(header[z] + "\n" + "".join(newSeq) + "\n" + "".join(newQual) + "\n" + "+" + "\n")			

#output file is closed
p.close()


