# usr/bin/python
import os


class File(object):
    """
    class file
    """

    def __init__(self, file=''):
        self.file_path = file
        self.file_name = os.path.split(self.file_path)[1]
        self.extension = self.file_name.split('.')[1]

    def __repr__(self):
        return f"file: { self.file_name }, \npath: { self.file_path }, \nextension: { self.extension }"

    def __str__(self):
        return f"file: { self.file_name }"


if __name__ == '__main__':
    file = os.path.join(os.getcwd(), "test_file.txt")
    file1 = File(file)
    print(file1)

# print(__name__)
