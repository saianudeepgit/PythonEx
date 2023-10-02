filenames = ['file1.txt', 'file2.txt']
with open('file3.txt', 'w') as outfile:

    for names in filenames:
        with open(names) as infile:
            outfile.write(infile.read())
        outfile.write("\n")