import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib.widgets as widgets

plt.ion()  # Enable interactive mode
matplotlib.use("TkAgg")  # Use the TkAgg backend (replace with another backend if needed)

def onselect(eclick, erelease):
    if eclick.ydata > erelease.ydata:
        eclick.ydata, erelease.ydata = erelease.ydata, eclick.ydata
    if eclick.xdata > erelease.xdata:
        eclick.xdata, erelease.xdata = erelease.xdata, eclick.xdata
    ax.set_ylim(erelease.ydata, eclick.ydata)
    ax.set_xlim(eclick.xdata, erelease.xdata)
    fig.canvas.draw()

fig = plt.figure()
ax = fig.add_subplot(111)
filename = "./1_office.jpg"
im = Image.open(filename)
arr = np.asarray(im)
plt_image = plt.imshow(arr)
rect = widgets.RectangleSelector(ax, onselect, interactive=True)

plt.show()  # Do not use block=True