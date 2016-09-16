import numpy as np

# Our image processing tools
import skimage.filters
import skimage.io
import skimage.measure
import skimage.morphology
import skimage.segmentation

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('dark')


#Correct for uneven illumination.




#Correct for "hot" or "bad" pixels in an image.
#Perform a thresholding operation.
#Remove bacteria or objects near/touching the image border.
#Remove objects that are too large (or too small) to be bacteria. Think carefully! For a multipurpose function, would you always want the same area cutoff?
#Remove improperly segmented cells.
#Return a labeled segmentation mask.
