import cv2
import numpy as np



filename = '5x5'
img = cv2.imread(filename+'.png')
cv2.imshow('1.Maze', img)
cv2.moveWindow('1.Maze',50,200)




# Binary conversion
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Inverting thresholding will give us a binary image with a white wall and a black background.
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV) 
cv2.imwrite(filename+'/1. Threshold1.jpg', thresh)
cv2.imshow('2.Threshold 1', thresh)
cv2.moveWindow('2.Threshold 1',415,200)

# Contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2:]
dc = cv2.drawContours(thresh, contours, 0, (255, 255, 255), 5)
cv2.imwrite(filename+'/2. Contours1.jpg', dc)
cv2.imshow('3.Contours 1', dc)
cv2.moveWindow('3.Contours 1',780,200)

dc = cv2.drawContours(dc, contours, 1, (0,0,0) , 5)
cv2.imwrite(filename+'/3. Contours2.jpg', dc)
cv2.imshow('4.Contours 2', dc)
cv2.moveWindow('4.Contours 2',1145,200)

ret, thresh = cv2.threshold(dc, 240, 255, cv2.THRESH_BINARY)
cv2.imwrite(filename+'/4. Threshold2.jpg', thresh)
cv2.imshow('5.Threshold 2', thresh)
cv2.moveWindow('5.Threshold 2',1510,200)


ke = 19
kernel = np.ones((ke, ke), np.uint8)

# Dilate
'''
Dilation is one of the two basic operators in the field of mathematical morphology, and the other is erosion.
It is usually applied to binary images, but there are some versions available for grayscale images.
The basic effect of the operator on binary images is to gradually enlarge the boundaries of foreground pixel regions (usually white pixels).
Therefore, the size of the foreground pixel increases, and the holes in these areas become smaller.
'''

dilation = cv2.dilate(thresh, kernel, iterations=1)
cv2.imwrite(filename+'/5. Dilation.jpg', dilation)
cv2.imshow('6.Dilation', dilation)
cv2.moveWindow('6.Dilation',740,412)

# Erosion
'''
Erosion is a form of the second operator.
It also applies to binary images.
The basic effect of the operator on binary images is to eliminate the boundaries of foreground pixel areas (usually white pixels).
Therefore, the area of ​​foreground pixels is reduced, and the holes in these areas become large.
'''

erosion = cv2.erode(dilation, kernel, iterations=1)
cv2.imwrite(filename+'/6. Erosion.jpg', erosion)
cv2.imshow('7.Erosion', erosion)
cv2.moveWindow('7.Erosion',1105,410)

# Find differences between two images
diff = cv2.absdiff(dilation, erosion)
cv2.imwrite(filename+'/7. Difference.jpg', diff)
cv2.imshow('8.Difference', diff)
cv2.moveWindow('8.Difference',470,650)
# splitting the channels of maze
b, g, r = cv2.split(img)
mask_inv = cv2.bitwise_not(diff)
cv2.imwrite(filename+'/8. Mask.jpg', mask_inv)
cv2.imshow('9.Mask', mask_inv)
cv2.moveWindow('9.Mask',835,650)

# In order to display the solution on the original maze image, first divide the original maze into r, g, b components.
# Now create a mask by inverting the diff image.
# The bitwise and r and g components of the original maze using the mask created in the last step.
# This step will remove the red and green components from the image portion of the maze solution.
# The last one is to merge all the components and we will use the blue marked solution.

# masking out the green and red color from the solved path
r = cv2.bitwise_and(r, r, mask=mask_inv)
b = cv2.bitwise_and(b, b, mask=mask_inv)

res = cv2.merge((b, g, r))
cv2.imwrite(filename+'/9. SolvedMaze.jpg', res)
cv2.imshow('10.Solved Maze', res)
cv2.moveWindow('10.Solved Maze',1200,650)


cv2.waitKey(0)
cv2.destroyAllWindows()
