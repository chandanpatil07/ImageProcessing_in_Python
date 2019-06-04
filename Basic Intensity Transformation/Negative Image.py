
"""
Image Data Analysis Using Numpy & OpenCV

uthor: Chandan Patil
email:  chandan.patil0007@gmail.com
Please feel free to use and modify this, but keep the above information. Thanks!
"""

# read details on blog post

import imageio
import matplotlib.pyplot as plt

pic = imageio.imread('<image location>')
plt.figure(figsize = (6,6))
plt.imshow(255 - pic);
