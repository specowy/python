with open('filecreate.txt', 'w+') as f:
    f.write('Lorem Ipsum')
    f.seek(0)
    print(f.read())
