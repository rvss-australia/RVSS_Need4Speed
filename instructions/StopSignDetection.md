## Creating a safe delivery robot

To avoid any danger (and large _10 second_ penalties!), your robot needs to be able to detect stop signs so that it can stop driving before proceeding safely. There are a number of ways to do this, but often the simplest is the best. For this workshop, we recommend using simple colour thresholding and blob detection!

<p align="center"><img src="../pics/sample_stop_sign.png" width="200" height="150"></p>

One of the packages included in your conda environment should be Peter Corke's [machinevision-toolbox for python](https://github.com/petercorke/machinevision-toolbox-python). Given a thresholded image (black and white, with target areas in white), this package makes it very easy to detect blobs! For example:

```
from machinevisiontoolbox import Image

thresholded_im = Image(<insert_your_thresholded_im_variable_here>)
blobs = thresholded_im.blobs()
print(blobs)

```
The blobs contain a number of features, including their centroid, area, perimeter, circularity and more! The package also includes features like image smoothing, cropping, colorspace conversion and more. You can explore these in more details on the [package github](https://github.com/petercorke/machinevision-toolbox-python).

Things to be aware of:
- you'll need to threshold your images for the stop sign. You may need to collect more data to help you choose the best thresholds. Be aware that the stop sign can be on urban or rural road tracks.
- cv2 loads images in BGR, but the machinevisiontoolbox is expecting RGB by default.
- if im.blobs() finds no blobs, it usually throws an error. Consider using a try/except block to watch out for this.
- The first time you import the package, it can be a little slow (should not be more than 5 seconds) .
