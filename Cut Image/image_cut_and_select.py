import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector
from PIL import Image
import os

filename = 'position of cropped image.txt' 
logFile = open('./' + filename, 'w')
logFile.write('image\tevent\n')

# Function to be executed after selection
def onselect(eclick, erelease):
    # Obtain (xmin, xmax, ymin, ymax) values
    extent = rect_selector.extents
    logFile.write(str(img) +'\t'+ str(extent) + '\n')
    print("Extents: ", extent)

    # Crop the image using the selected region
    cropped_image = image.crop((extent[0], extent[2], extent[1], extent[3]))

    # Save the cropped image
    cropped_image.save('./{}_cropped_image2.jpg'.format(img))
    
    # Display the cropped image
    plt.figure()
    plt.imshow(cropped_image)
    plt.title('Cropped Image')
    plt.show()

image_path = './'
imgname = ['1_office','3_office','21_city'] 
for img in imgname:
    # Load an example image
      # Replace with the path to your image
    image = Image.open(image_path + img + '.png')
    
    
    # Plot the original image
    fig, ax = plt.subplots()
    fig.set_size_inches(10.666666666666666, 8, forward=True)
    ax.imshow(image)
    
    plt.title('Original Image')
    
    
    
    # Define a RectangleSelector at given axes ax.
    # It calls a function named 'onselect' when the selection is completed.
    # Rectangular box is drawn to show the selected region.
    rect_selector = RectangleSelector(ax, onselect, button=[1])
    rectprops={'visible': False}
    
    # Display the plot
    plt.show()
    plt.pause(6)
    plt.close()
    plt.close(fig)


logFile.close()