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

# Load an example phase image.
im_phase = skimage.io.imread('data/HG105_images/noLac_phase_0004.tif')
im_fl = skimage.io.imread('data/HG105_images/noLac_FITC_0004.tif')
#
# # Display side-by-side
# with sns.axes_style('dark'):
#     fig, ax = plt.subplots(1, 2, figsize=(9.5, 8))
#     ax[0].imshow(im_phase, cmap=plt.cm.viridis)
#     ax[1].imshow(im_fl, cmap=plt.cm.viridis)

# Structuring element
selem = skimage.morphology.square(3)

# Perform median filter
im_phase_filt = skimage.filters.median(im_phase, selem)
im_fl_filt = skimage.filters.median(im_fl, selem)
# Apply a gaussian blur with a 50 pixel radius.
im_phase_gauss = skimage.filters.gaussian(im_phase_filt, 50.0)

# Show the two images side-by-side
with sns.axes_style('dark'):
    fig, ax = plt.subplots(1,2, figsize=(9.5,8))
    ax[0].imshow(im_phase_filt, cmap=plt.cm.viridis)
    ax[1].imshow(im_phase_gauss, cmap=plt.cm.viridis)

# Convert the median-filtered phase image to a float64
im_phase_float = skimage.img_as_float(im_phase_filt)

# Subtract our gaussian blurred image from the original.
im_phase_sub = im_phase_float - im_phase_gauss

# Show our original image and background subtracted image side-by-side.
with sns.axes_style('dark'):
    fig, ax = plt.subplots(1, 2, figsize=(9.5, 8))
    ax[0].imshow(im_phase_float, cmap=plt.cm.viridis)
    ax[1].imshow(im_phase_sub, cmap=plt.cm.viridis)

# Indices of subimage
slc = np.s_[0:450, 50:500]

# Look at subimage
with sns.axes_style('dark'):
    plt.imshow(im_phase_sub[slc], cmap=plt.cm.gray)

# Compute Otsu threshold value for median filtered image
thresh_otsu = skimage.filters.threshold_otsu(im_phase_sub)

# Construct thresholded image
im_bw = im_phase_sub < thresh_otsu

# Clear border with 5 pixel buffer
im_bw = skimage.segmentation.clear_border(im_bw, buffer_size=5)

# Display images
plt.close('all')
with sns.axes_style('dark'):
    fig, ax = plt.subplots(2, 2, figsize=(9.5, 8))
    ax[0,0].imshow(im_phase_sub, cmap=plt.cm.gray)
    ax[0,1].imshow(im_bw, cmap=plt.cm.gray)
    ax[1,0].imshow(im_phase_sub[slc], cmap=plt.cm.gray)
    ax[1,1].imshow(im_bw[slc], cmap=plt.cm.gray)

# Label binary image; background kwarg says value in im_bw to be background
im_labeled, n_labels = skimage.measure.label(
                            im_bw, background=0, return_num=True)

# See result (one of the few times it's ok to use rainbow colormap!)
plt.close('all')
with sns.axes_style('dark'):
    # plt.imshow(im_labeled, cmap=plt.cm.rainbow)
    plt.imshow(im_labeled, cmap=plt.cm.Spectral_r)

# Show number of regions
print('Number of individual regions = ', n_labels)



# Extract region props
im_props = skimage.measure.regionprops(im_labeled, intensity_image=im_fl_filt)
#Visualize
im_props
im_props[0].area

#Show single cells in plot based on their number that was assigned.
plt.imshow(im_labeled==1) # something is off here and doesnt work....
plt.imshow(im_labeled==5)
plt.imshow(im_labeled==6)

# Show zoomed in image
plt.close('all')
with sns.axes_style('dark'):
    plt.imshow(im_phase_filt[slc], cmap=plt.cm.gray)


# Make a filtered black and white image
im_bw_filt = im_labeled > 0

# Define cutoff size
cutoff = 300

# Loop through image properties and delete small objects
n_regions = 0
for prop in im_props:
    if prop.area < cutoff:
        im_bw_filt[im_labeled==prop.label] = 0
    else:
        n_regions += 1

# Look at result
plt.close('all')
with sns.axes_style('dark'):
    plt.imshow(im_bw_filt, cmap=plt.cm.gray)

# Show number of regions
print('Number of individual regions = ', n_regions)

# # Extract region props
# im_props = skimage.measure.regionprops(im_labeled, intensity_image=im_fl_filt)
#
# # Show zoomed in image
# plt.close('all')
# with sns.axes_style('dark'):
#     plt.imshow(im_phase_filt[slc], cmap=plt.cm.gray)
