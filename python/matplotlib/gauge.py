import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm # colormap
from matplotlib.patches import Circle, Wedge, Rectangle

def setWhitePlot():
    plt.rcParams['axes.facecolor'] = 'white'
    plt.rcParams['figure.facecolor'] = 'white'
    plt.rcParams['font.size'] = 10
    plt.rcParams['toolbar'] = 'None'


def calculateDegreeRange(n):
    start = np.linspace(0,180,n+1, endpoint=True)[0:-1]
    end = np.linspace(0,180,n+1, endpoint=True)[1::]
    mid_points = start + ((end-start)/2.)
    return np.c_[start, end], mid_points

def rot_text(ang):
    rotation = np.degrees(np.radians(ang) * np.pi / np.pi - np.radians(90))
    return rotation

def addPatches(ax, ang_range, colors):
    """ Plot the sectors and the arcs   """
    patches = []
    for ang, c in zip(ang_range, colors):
        # sectors
        patches.append(Wedge((0.,0.), .4, *ang, facecolor='w', lw=2))
        # arcs
        patches.append(Wedge((0.,0.), .4, *ang, width=0.10, facecolor=c, lw=2, alpha=0.5))

    [ax.add_patch(p) for p in patches]

def setLabels(ax, mid_points, labels):
    """ Set the labels   """

    for mid, lab in zip(mid_points, labels):
        ax.text(0.35 * np.cos(np.radians(mid)),
                0.35 * np.sin(np.radians(mid)),
                lab,
                horizontalalignment='center',
                verticalalignment='center',
                fontsize=12,
                fontweight='bold',
                rotation = rot_text(mid))

def addArrow(ax, min, max, value):
    """ Plot gauging arrow   """
    pos = 180 * value/(max-min)

    # Axes.arrow(x, y, dx, dy, **kwargs)
    # kwargs: width, head_width, head_length, shape, overhang,
    ax.arrow(0, 0, 0.225 * np.cos(np.radians(pos)), 0.225 * np.sin(np.radians(pos)),
             width=0.03, head_width=0.09, head_length=0.1, fc='k', ec='k')

    ax.add_patch(Circle((0, 0), radius=0.02, facecolor='k'))
    ax.add_patch(Circle((0, 0), radius=0.01, facecolor='w', zorder=11))

def getColorsArray(color_code, n_labels):
    if isinstance(color_code, str):
        cmap = cm.get_cmap(color_code, n_labels)
        cmap = cmap(np.arange(n_labels))
        colors = cmap[::-1,:].tolist()

    return colors

def gauge(labels, min, max, value):
    n_labels = len(labels)


    setWhitePlot()
    fig, ax = plt.subplots()

    colors = getColorsArray('jet_r', n_labels)
    ang_range, mid_points = calculateDegreeRange(n_labels)
    addPatches(ax, ang_range, colors)
    setLabels(ax, mid_points, labels)
    addArrow(ax, min, max, value)


    # Remove frame and ticks, and makes axis equal and tight
    ax.set_frame_on(False)
    ax.axes.set_xticks([])
    ax.axes.set_yticks([])
    ax.axis('equal')
    plt.show()

labels = ["low", "can get higher", "okish", "should get lower", "high"]
gauge(labels, min=0, max=10, value=1)
