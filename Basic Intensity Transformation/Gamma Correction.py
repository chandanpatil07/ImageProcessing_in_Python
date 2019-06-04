
"""
Image Data Analysis Using Numpy & OpenCV

author: Chandan Patil
email:  chandan.patil0007@gmail.com
Please feel free to use and modify this, but keep the above information. Thanks!
"""


# read details on blog post

import imageio
import numpy as np
import matplotlib.pyplot as plt

pic = imageio.imread('<image location>')
gamma = 2.2
original = ((pic/255) ** (1/gamma))

plt.imshow(original)
