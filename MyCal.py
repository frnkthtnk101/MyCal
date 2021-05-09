'''
MyCal.py
Create a professional looking calendars without spending millions of dollars.
'''
import argparse
import os
from PIL import Image, ImageDraw, ImageFont


class Image_generator_interface:
    def create_image(self, picture, font, destination, text):
        """Create an image and save."""
        pass


class Picture_on_top_with_Text_at_bottom(Image_generator_interface):
    def create_image(self, picture, font, destination, text):
        given_image = Image.open(picture)
        picture_size = (given_image.size[0] * 1.25, given_image.size[1] * 1.25)
        generated_image = Image.new('RGB', picture_size, color='white')
        offset_for_image = (picture.size[0] * .25, picture.size[1] * .10)
        generated_image.paste(given_image,offset_for_image)
        fnt = ImageFont.truetype(font, 15)
        d = ImageDraw.Draw(generated_image)
        d.text((10, 10), text, font=fnt, fill=(0, 0, 0))
        generated_image.save(destination)



class Args:
    def __init__(self, picture_folder_Path, font, destination):
        self.picture_folder_path = picture_folder_Path
        self.font = font
        self.destination = destination


def main(args):
    img = Image.new('RGB', (100, 100), color='white')
    fnt = ImageFont.truetype(args.font, 15)
    d = ImageDraw.Draw(img)
    d.text((10, 10), "I <3 bruna.", font=fnt, fill=(0, 0, 0))


    img.save(args.destination)

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
            font = "C:\Windows\Fonts\comic.ttf"
        destination_directory_given = given_args.output is not None
        if destination_directory_given:
            destination = given_args.output
        else:
            destination = os.path.join(os.environ['HOMEPATH'], 'Desktop', 'test.jpg')
        parsed_args = Args(given_args.picture_directory, font, destination)
        main(parsed_args)
    else:
        print('Pleas provide a valid directory!')
