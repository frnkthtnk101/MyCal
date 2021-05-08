'''
MyCal.py
Create professional looking calendars without spending millions
of dollars.
'''
import argparse
import os


class Args:
    def __init__(self, picture_folder_Path, font):
        self.picture_folder_path = picture_folder_Path
        self.font = font


def main(args):
    print(args.font)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    arg_group = parser.add_argument_group()
    arg_group.add_argument('-f', '--font', type=str)
    arg_group.add_argument('-p', '--picture_directory', type=str)
    given_args = parser.parse_args()
    font_given = given_args.font is not None
    picture_directory_given = given_args.picture_directory is not None and os.path.exists(given_args.picture_directory)
    if picture_directory_given:
        if font_given:
            font = given_args.font
        else:
            font = "Comic Sans"
        parsed_args = Args(given_args.picture_directory, font)
        main(parsed_args)
    else:
        print('Pleas provide a valid directory!')
