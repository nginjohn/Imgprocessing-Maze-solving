# Imgprocessing-Maze-solving OpenCV

To find the shortesh path by using Morphological Transforms. 

## Tools Used

  - OpenCV 3.4.2
  - Python 2.7



### Contours
Contours can be explained simply as a curve joining all the continuous points (along the boundary), having same color or intensity. The contours are a useful tool for shape analysis and object detection and recognition.

### Dilation
Dilation is one of the two basic operators in the area of mathematical morphology, the other being erosion. It is typically applied to binary images, but there are versions that work on grayscale images. The basic effect of the operator on a binary image is to gradually enlarge the boundaries of regions of foreground pixels (i.e. white pixels, typically). Thus areas of foreground pixels grow in size while holes within those regions become smaller.

### Erosion
Erosion is the second morphological operator. It is also applied to binary images. The basic effect of the operator on a binary image is to erode away the boundaries of regions of foreground pixels (i.e. white pixels, typically). Thus areas of foreground pixels shrink in size, and holes within those areas become larger.

The dilation of A by the structuring element B is defined by


>>>dilation = cv2.dilate(thresh, kernel, iterations=1)


The erosion of A by B is also given by the expression
>>>erosion = cv2.erode(dilation, kernel, iterations=1)


# Find differences between two images
>>>diff = cv2.absdiff(dilation, erosion)

# splitting the channels of maze
>>>b, g, r = cv2.split(img)
>>>mask_inv = cv2.bitwise_not(diff)


6. In order to display the solution on the original maze image, first divide the original maze
into r, g, b components. The bitwise and r and g components of the originl maze using the
mask created in the last step. This step will remove the red and blue components from the 

image portion of the maze solution. The last one is to merge all the components and we
will use the green marked solution. masking out the blue and red from the solved path

>>>r = cv2.bitwise_and(r, r, mask=mask_inv)

>>>b = cv2.bitwise_and(b, b, mask=mask_inv)

# then solution will be shown by green color.
>>>res = cv2.merge((b, g, r)
