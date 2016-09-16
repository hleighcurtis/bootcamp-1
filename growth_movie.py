import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('dark')
import glob
import os
import PIL

# Our image processing tools
import skimage.filters
import skimage.io
import skimage.measure
import skimage.morphology
import skimage.segmentation

# Load in the series of images contained in the directory data/bacterial_growth/.
# Be sure that however you store them (a list or tuple or other object) has the
# frames in the proper order.
# bac_list = [glob.glob('data/bacterial_growth/*.tif')]

# Make an array to deposit areas later.
filelist = glob.glob("data/bacterial_growth/*.tif")
tot_area=np.zeros(len(filelist))
i=0
for filename in filelist:
    im_df = skimage.io.imread(filename)

    # Perform the median filter.
    # Make the structuring element
    selem = skimage.morphology.square(3)

    # Perform the median filter
    im_filt = skimage.filters.median(im_df, selem)

    # Apply a gaussian blur with a 50 pixel radius.
    im_gauss = skimage.filters.gaussian(im_filt, 50.0)

    # Convert the median-filtered phase image to a float64
    im_float = skimage.img_as_float(im_filt)

    # Subtract our gaussian blurred image from the original.
    im_sub = im_float - im_gauss

    # Segment the images to separate bacteria from background. You do not need
    #to segment individual bacteria; this would likely require some more advanced
    #techniques involving edge detection that we haven't covered in bootcamp.

    # Compute Otsu thresholds
    thresh_bac_otsu = skimage.filters.threshold_otsu(im_sub)

    # # Threshold value, as obtained by eye
    # thresh_bac = 588

    # Generate thresholded image
    im_bac_bw = im_sub > thresh_bac_otsu
    #
    # # Display filt and thresholded image
    # with sns.axes_style('dark'):
    #     fig, ax = plt.subplots(1, 2, figsize=(10, 5))
    #     ax[0].imshow(im_filt, cmap=plt.cm.gray)
    #     ax[1].imshow(im_bac_bw, cmap=plt.cm.gray)

    # Compute bacterial area
    bacterial_area_pix = im_bac_bw.sum()

    # Define interpixel distance
    interpix_dist = 0.063 # microns

    # Compute bacterial area
    bacterial_area_micron = bacterial_area_pix * interpix_dist**2

    # # Print total area
    # print('bacterial area =', bacterial_area_pix, 'pixels')

    # Define interpixel distance
    interpix_dist = 0.063 # microns

    # Compute bacterial area
    bacterial_area_micron = bacterial_area_pix * interpix_dist**2

    # # Print total area
    #print('bacterial area =', bacterial_area_micron, 'square microns')

    # Add areas to empty array
    tot_area[i] = bacterial_area_micron
    i += 1


# Plot a growth curve for this growing colony. What values should be on the
# yy -axis? (This is one of those times where I ask an open question for which
# there is no "right" answer.)
time = np.linspace(0, 825, 55)
# plt.semilogy(time, tot_area, marker='.', linestyle='none', alpha=0.5, markersize=15)
# plt.xlabel('time (min)')
# plt.ylabel('Change in Area of Bacterial Footprint')
# plt.title('B. subtilis Growth Curve')
# plt.show()

fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].semilogx(time, tot_area, marker='.', linestyle='none', alpha=0.5, markersize=15)
ax[0].set_title('B. subtilis Growth Curve semilog x')
ax[1].semilogy(time, tot_area, marker='.', linestyle='none', alpha=0.5, markersize=15)
ax[0].set_xlabel('time (min)')
ax[0].set_ylabel('Change in Area of Bacterial Footprint')
ax[1].set_xlabel('time (min)')
ax[1].set_ylabel('Change in Area of Bacterial Footprint')
ax[1].set_title('B. subtilis Growth Curve semilog y')
plt.show()
