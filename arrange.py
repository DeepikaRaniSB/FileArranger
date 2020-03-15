# usr/bin/python

import os
import sys
from file_upload import File

#: :::::::::::: Global Variables ::::::::::::: :#
ARRANGED_FOLDER = os.path.join(os.getcwd(), "Arranged_Folder")
#: ::::::::::::: End of Global Variables ::::::::::::: :#

def main(file=''):
    """
    master function to call all the functionalities to upload and arrange files.
    :param: Input file which need to be uploaded and arrange.
    :return: None
    """
    # print(__name__)
    if file == '':
        print("file is empty")
    else:
        if not os.path.exists(ARRANGED_FOLDER):
            print(f"going to create arranged folder location: '{ARRANGED_FOLDER}'")
            os.mkdir(ARRANGED_FOLDER)
        upload_file = File(file)
        print(upload_file)


def test():
    """
    test arrange.py for different test cases.
    :return: None.
    """
    print("test main")


if __name__ == '__main__':
    # print(sys.argv)
    file = ''
    if len(sys.argv) > 1:
        file = os.path.join(os.getcwd(), sys.argv[1])
    main(file)
