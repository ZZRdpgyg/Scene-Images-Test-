import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector
from PIL import Image

# Function to be executed after selection
def onselect(eclick, erelease):
    # Obtain (xmin, xmax, ymin, ymax) values
    extent = rect_selector.extents
    print("Extents: ", extent)

    # Crop the image using the selected region
    cropped_image = image.crop((extent[0], extent[2], extent[1], extent[3]))

    # Display the cropped image
    plt.figure()
    plt.imshow(cropped_image)
    plt.title('Cropped Image')
    plt.show()

# Load an example image
image_path = './1_office.jpg'  # Replace with the path to your image
image = Image.open(image_path)

# Plot the original image
fig, ax = plt.subplots()
fig.set_size_inches(16, 12, forward=True)
ax.imshow(image)
plt.title('Original Image')

# Define a RectangleSelector at given axes ax.
# It calls a function named 'onselect' when the selection is completed.
# Rectangular box is drawn to show the selected region.
rect_selector = RectangleSelector(ax, onselect,  button=[1])
rectprops={'visible': False}

# Display the plot
plt.show()
plt.savefig('1_office_select.png',rect_selector)