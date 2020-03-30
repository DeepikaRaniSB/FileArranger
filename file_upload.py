# usr/bin/python
import os


class File(object):
    """
    class File to instantiate object of File.
    """

    def __init__(self, file=''):
        self.file_path = file
        self.file_name = os.path.split(self.file_path)[1]
        self.extension = self.file_name.split('.')[1]

    def __repr__(self):
        return f"file: { self.file_name }, \npath: { self.file_path }, \nextension: { self.extension }"

    def __str__(self):
        return f"file: { self.file_name }"

    def get_target_folder(self, base_location=''):
        """
        gives location where file need to be arranged on the bases of file extension.
        :param base_location: based on configuration of arranged folder.
        :return: target_folder: location where file need to be kept.
        """
        target_folder = os.path.join(base_location, self.extension)
        if not os.path.exists(target_folder):
            print(f"going to create target folder: '{ target_folder }' for ext: '.{ self.extension }'")
            os.mkdir(target_folder)
        return target_folder

    def upload_file(self, target_folder=''):
        """

        :param target_folder:
        :return: target_file:
        """
        file_data = ''
        with open(self.file_path, 'r+b') as file:
            file_data = file.read()

        target_file = os.path.join(target_folder, self.file_name)
        with open(target_file, 'w+b') as file:
            file.write(file_data)
        return target_file


# if __name__ == '__main__':
#     ARRANGED_FOLDER = os.path.join(os.getcwd(), "test_Arranged_Folder")#
#     if not os.path.exists(ARRANGED_FOLDER):
#         print(f"going to create arranged folder location: '{ARRANGED_FOLDER}'")
#         os.mkdir(ARRANGED_FOLDER)
#     file = os.path.join(os.getcwd(), "test_file.txt")
#     file1 = File(file)
#     print(file1)
#     target_file = file1.upload_file(file1.get_target_folder(ARRANGED_FOLDER))
#
#     if os.path.exists(target_file):
#         print(f"sucessfully placed file at '{ target_file }")
#     else:
#         print(f"Failed to arrange file: { file1.file_name }")
# print(__name__)
