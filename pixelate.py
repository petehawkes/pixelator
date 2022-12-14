

#!/usr/bin/env python3

import os
from wand.image import Image


def main():

	og = Image(filename ='original.png')
	
	# number of pixelations (.01 scale increments from .01)
	count = 8;

	# clear frames folder
	os.system("rm frames/*")


	# start gifsicle command, needs an arg per frame
	_gif = "gifsicle -b pixelated.gif -d5 "

	for i in range(1, count):

		new = og.convert('gif')

		down_scale = i/100;
		print (i, down_scale)

		new.sample(int(og.width*down_scale), int(og.height*down_scale))
		new.sample(og.width, og.height)
		new.save(filename = 'frames/pixelated-' + str(i).zfill(2) + '.gif')

		_gif += "'#" + str(i-1) + "' "

	end = og.convert('gif')
	end.save(filename = 'frames/pixelated-' + str(count).zfill(2) + '.gif')
	os.system("gifsicle --colors 256 -d10 frames/*.gif > pixelated.gif")

	_gif += "-d1000 '#" + str(count-1) + "' --no-loopcount -o pixelated-fix.gif"

	print(_gif)
	os.system(_gif)


if __name__ == "__main__":
    main()

