infile = open("d:\\phones1.txt",'r')
#lines = infile.read()
#lines = infile.readlines()
line = infile.readline().rstrip()
while line != "":
    print(line)
    line = infile.readline().rstrip()

infile.close()
