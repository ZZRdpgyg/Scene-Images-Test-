# ZZR
Here are the image-related tests for my 2 PhD 7T - fMRI project 
Images test (python & Matlab):
1. image similarity test (structural similarity index model):
   SSIM test folder: 1. imgrey.py: transfer colourful image to grey-scale
                      2. rename.py: rename the image file name if needed
                       3. msr_similiarity.py: SSIM image similarity test (pixel lineup and density)
                         4. heatmap.py: plot results, store results in an array and calculate min max mean median values
2. image similarity test (spatial envelope):
   Spatial envelop test: 1. similarity test.m: test gist similarity and plot heat map.
    
3. image selection task (behavioural task to crop the familiar part from an image)&Match code:
   1. image_cut_and_select.py: select the part of the image (10s duration then next picture)
   2. match.py: show the location and scale of the cropped image on the original image 
5. Brightness and contrast adjustment 
6. image crop code (e.g crop 1/4 lower right part of the image)
