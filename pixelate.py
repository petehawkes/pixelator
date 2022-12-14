

#!/usr/bin/env python3

import os
import argparse
from wand.image import Image


def main():

	# receive an image as a parameter
	parser = argparse.ArgumentParser(description="""
		from a source image, creates an resolve-from-pixelation animated GIF
		""")
	parser.add_argument('img', help='path to source image')
	args = parser.parse_args()
	path = os.path.realpath(args.img)
	
	
	# load iamge
	og = Image(filename = path)

	print ("\nPixelating " + args.img + "\n")
	
	# number of pixelations (.01 scale increments from .01)
	count = 8;

	# clear frames folder
	os.system("rm frames/*")

	# start gifsicle command, which needs an arg per frame
	_gifsicle = "gifsicle -b pixelated.gif -d5 "

	# create each frame, most pixelated first
	for i in range(1, count):

		new = og.convert('gif')

		down_scale = i/100;
		print (i, down_scale)

		# down sample then pop back to full size
		new.sample(int(og.width*down_scale), int(og.height*down_scale))
		new.sample(og.width, og.height)
		new.save(filename = 'frames/pixelated-' + str(i).zfill(2) + '.gif')

		_gifsicle += "'#" + str(i-1) + "' "

	# make the last frame
	end = og.convert('gif')
	end.save(filename = 'frames/pixelated-' + str(count).zfill(2) + '.gif')
	
	# create animated gif from all frames, constant delay
	os.system("gifsicle --colors 256 -d10 frames/*.gif > pixelated.gif")

	# set up the command
	new_file = str(args.img).rsplit('.', 1)[0] + "-pixelated.gif"
	_gifsicle += "-d1000 '#" + str(count-1) + "' --no-loopcount -o " + new_file

	# test command
	# print (gifsicle)

	# apply a short delay to all but the last frame
	os.system(_gifsicle)

	print("\n——— —— - ·· ·\nPIXELATED: " + new_file + "\n——— —— - ·· ·\n")
 


if __name__ == "__main__":
	main()

