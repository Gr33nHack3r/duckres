# duckres

This simple python program transform the resolution of an image from an aspect ratio to another one.
It let you to cut a 16:10 ratio to a 21:9 ratio wallpaper to make it perfect for your 21:9 monitor. (Yes, that's why it was created)
And of course it has WTFPL so you can do whatever you want.

## Dependencies

The Python library Pillow is the only dependency at the moment. You can get it in the following ways:

- __Arch Linux__: available in the community repository as [python-pillow](https://www.archlinux.org/packages/community/x86_64/python-pillow/), in the AUR as [python-pillow-git](https://aur.archlinux.org/packages/python-pillow-git/). You can also use the method described in the next element of the list.

- __Almost every distro__: available in the `pip` packet manager repos as `Pillow`. Install with

      $ sudo pip --user install Pillow

-__MacOS__: available in the `pip` packet manager repos as `Pillow`. Install with
      $ sudo pip install Pillow

## Installation

The only file you really need is `duckres.py`. There are various methods for downloading it:

- `git clone https://github.com/Gr33nHack3r/duckres`.

- `wget https://raw.githubusercontent.com/Gr33nHack3r/duckres/master/duckres.py`

- `curl https://raw.githubusercontent.com/Gr33nHack3r/duckres/master/duckres.py > duckres.py`

## Usage

After the installation you can run `duckres` with:

    $ python duckres.py
    
You can find more info on functionalities and options by running:

    $ python duckres.py --help
    
