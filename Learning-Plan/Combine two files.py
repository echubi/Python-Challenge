file1 = '..\\..\\..\\Documents\\file1.txt'
file2 = '..\\..\\..\\Documents\\file2.txt'


data = data2 = ""

with open(file1) as fp:
    data = fp.readlines()

with open(file2) as fp:
    data2 = fp.readlines()

with open("..\\..\\..\\Documents\\file 3.txt", 'w') as z:
    for i in range(len(data)):
        line = data[i].strip() + ' ' + data2[i]
        z.write(line)
