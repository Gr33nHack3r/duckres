#!/usr/bin/env python

from PIL import Image
from argparse import ArgumentParser
from sys import exit
import os

#############################################################################################################

def ratio(iterable):
    return iterable[0] / iterable[1]

def expand_path(path):
    if not path.startswith("/"):
        if path.startswith("~"):
            return os.path.expanduser(path)
        else:
            return f"{os.getcwd()}/{path}"
    else:
        return path

#############################################################################################################

def prop(input_image_size, output_aspect_ratio, show_results=False):

    if args.debug:
        print(f"Ratio input image dimensions: {input_image_size} = {ratio(input_image_size)}")
        print(f"Ratio output aspect ratio: {output_aspect_ratio} = {ratio(output_aspect_ratio)}")

    if ratio(input_image_size) < ratio(output_aspect_ratio):
        output_image_size = [input_image_size[0], int(input_image_size[0] / ratio(output_aspect_ratio))]
    elif ratio(input_image_size) > ratio(output_aspect_ratio):
        output_image_size = [int(input_image_size[1] * ratio(output_aspect_ratio)), input_image_size[1]]
    else:
        output_image_size = input_image_size

    if show_results:
        print(f"Output size: {output_image_size[0]}/{output_image_size[1]} = {ratio(output_image_size)}")

    return output_image_size

#############################################################################################################

def autocrop(input_image_path, output_aspect_ratio):

    if args.debug:
        print(f"Initial input image path: {input_image_path}")

    input_image_path = expand_path(input_image_path)

    if args.debug:
        print(f"Final input image path: {input_image_path}")

    with Image.open(input_image_path) as input_image:

        # ! input_image.size is a tuple

        if args.debug:
            print(f"Input image format: {input_image.format}")

        output_image_size = prop(list(input_image.size), output_aspect_ratio)

        crop_factor = [int((input_image.size[0] - output_image_size[0]) / 2),
                       int((input_image.size[1] - output_image_size[1]) / 2)]

        if output_image_size[0] != input_image.size[0]:
            output_image = input_image.crop((crop_factor[0], 0, input_image.size[0]-crop_factor[0], input_image.size[1]))
        elif output_image_size[1] != input_image.size[1]:
            output_image = input_image.crop((0, crop_factor[1], input_image.size[0], input_image.size[1]-crop_factor[1]))
        else:
            output_image = input_image

        if args.preview:
            output_image.show()
            if input("Save the cropped image? [y/n] ") == "y":
                if args.output_path:
                    output_image.save(expand_path(args.output_path))
                else:
                    output_image.save(input_image_path)
            else:
                print("The cropped image was not saved")
        else:
            if args.output_path:
                output_image.save(expand_path(args.output_path))
            else:
                output_image.save(input_image_path)

#############################################################################################################
# COMMAND-LINE ARGS PARSING

parser = ArgumentParser(description="From one aspect ratio to another, simple")

parser.add_argument(
    "--image-path",
    "-i",
)

parser.add_argument(
    "--output-path",
    "-o",
)

parser.add_argument(
    "--crop",
    "-c",
    action="store_true"
)

parser.add_argument(
    "--size-input",
    "-s",
    nargs=2,
    type=int,
    metavar=("width", "height")
)

parser.add_argument(
    "--ratio-output",
    "-r",
    nargs=2,
    type=int,
    metavar=("x", "y")
)

parser.add_argument(
    "--preview",
    "-p",
    action="store_true"
)

parser.add_argument(
    "--debug",
    "-d",
    action="store_true"
)

args = parser.parse_args()

if args.image_path:
    if args.ratio_output:
        if not args.crop:
            with Image.open(args.image_path) as input_image:
                input_image_size = list(input_image.size)
            prop(input_image_size, args.ratio_output, show_results=True)
        else:
            autocrop(args.image_path, list(args.ratio_output))
    else:
        print("Error: --ratio-output not specified")
        exit(1)
elif args.size_input and args.ratio_output:
    prop(list(args.size_input), args.ratio_output, show_results=True)
else:
    print("Wrong usage, you may want to use -h or --help")
    exit(1)
