# read file, write files/create files

f = open('input.txt', 'r')
maleFile = open('file/MaleFile.txt', 'w')
femaleFile = open('file/FemaleFile.txt', 'w')
for line in f:
    line_split = line.split()
    if line_split[2] == 'Male':
        maleFile.write(line)
    else:
        femaleFile.write(line)
f.close()
maleFile.close()
femaleFile.close()
