# convert -scale 1% -scale 10000% original.png pixelated-01.png
# convert -scale 5% -scale 2000% original.png pixelated-05.png
# convert -scale 10% -scale 1000% original.png pixelated-10.png
# convert -scale 100% -scale 100% original.png pixelated-100.png

 #!/bin/bash 
convert -scale 1% -scale 10000% original.png frames/pixelated-01.gif
convert -scale 5% -scale 2000% original.png frames/pixelated-05.gif
convert -scale 10% -scale 1000% original.png frames/pixelated-10.gif
convert -scale 100% -scale 100% original.png frames/pixelated-100.gif

# make gif
# gifsicle --colors 256 -d 100 frames/*.gif > all.gif