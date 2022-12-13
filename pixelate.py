

#!/usr/bin/env python3

import os
from wand.image import Image


def main():

	og = Image(filename ='original.png')
	new = og.convert('png')

	down_scale = .01;

	new.sample(int(og.width*down_scale), int(og.height*down_scale))
	new.sample(og.width, og.height)
	
	new.save(filename = 'frames/pixelated.png')

	print (og.height, og.width)


if __name__ == "__main__":
    main()


# recreating this

# convert -scale 1% -scale 10000% original.png pixelated-01.png
# convert -scale 5% -scale 2000% original.png pixelated-05.png
# convert -scale 10% -scale 1000% original.png pixelated-10.png
# convert -scale 100% -scale 100% original.png pixelated-100.png
