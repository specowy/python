import os


def foo(count, file_size, file_name):
    x = 0
    while x < count:
        with open(file_name, "a") as fd:
            ##
            fd.write("text")
            ##
            if int(os.path.getsize(file_name)) > file_size:
                x += 1
                file_name = "file"+str(x)+".txt"


if __name__ == "__main__":
    count = 3
    file_size = 100
    file_name = "file.txt"
    foo(count, file_size, file_name)
    print(os.stat('file.txt').st_size)
    print(os.stat('file1.txt').st_size)
    print(os.stat('file2.txt').st_size)
