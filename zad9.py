try:
    with open("file.txt", 'r') as f1:
        with open("other_file.txt", 'w') as f2:
            for line in f1:
                f2.write(line)
except:
    print('Exception during opening file1!')