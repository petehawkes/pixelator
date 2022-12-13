

#!/usr/bin/env python3

import os
from wand.image import Image


def main():

	og = Image(filename ='original.png')
	
	count = 20;
	for i in range(1, count):

		new = og.convert('gif')

		down_scale = i/100;

		print (i, down_scale)

		new.sample(int(og.width*down_scale), int(og.height*down_scale))
		new.sample(og.width, og.height)
		
		new.save(filename = 'frames/pixelated-' + str(i).zfill(2) + '.gif')

	end = og.convert('gif')
	end.save(filename = 'frames/pixelated-' + str(count).zfill(2) + '.gif')
	os.system("gifsicle --colors 256 -d 5 frames/*.gif > all.gif")


if __name__ == "__main__":
    main()


# recreating this

# convert -scale 1% -scale 10000% original.png pixelated-01.png
# convert -scale 5% -scale 2000% original.png pixelated-05.png
# convert -scale 10% -scale 1000% original.png pixelated-10.png
# convert -scale 100% -scale 100% original.png pixelated-100.png
