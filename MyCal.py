'''
MyCal.py
Create a professional looking calendars without spending millions of dollars.
'''
import argparse
import os


class Args:
    def __init__(self, picture_folder_Path, font, destination):
        self.picture_folder_path = picture_folder_Path
        self.font = font
        self.destination = destination


def main(args):
    print(args.font)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    arg_group = parser.add_argument_group()
    arg_group.add_argument('-f', '--font', type=str)
    arg_group.add_argument('-p', '--picture_directory', type=str)
    arg_group.add_argument('-o', '--output', type=str)
    given_args = parser.parse_args()
    picture_directory_given = given_args.picture_directory is not None and os.path.exists(given_args.picture_directory)
    if picture_directory_given:
        font_given = given_args.font is not None
        if font_given:
            font = given_args.font
        else:
            font = "Comic Sans"
        destination_directory_given = given_args.output is not None
        if destination_directory_given:
            destination = given_args.output
        else:
            destination = os.path.join(os.environ['HOMEPATH'], 'Desktop', 'test.jpg')
        parsed_args = Args(given_args.picture_directory, font, destination)
        main(parsed_args)
    else:
        print('Pleas provide a valid directory!')
