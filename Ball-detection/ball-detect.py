#!/usr/bin/env python

import sys

# Import OpenCV and Numpy
import cv2
import numpy as np

def houghCircle(image):
    # Convert image to grayscale.
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    # Perform Canny edge detection.
    threshold1 = 50
    threshold2 = 150

    dImage = cv2.Canny(gray, threshold1, threshold2)
    # Use Hough Transform for detecting circles to detect the sign.

    ball = cv2.HoughCircles(dImage, cv2.HOUGH_GRADIENT, dp = 1, minDist = 20, param1 = 50, param2 = 12, minRadius = 4, maxRadius = 6)

    # Draw the circle back on the original image.
    if ball is not None:
        ball = np.uint16(np.around(ball))  # Process only if circles are found
        for circle in ball[0, :]:
            center = (circle[0], circle[1])  # Center coordinates
            radius = circle[2]              # Radius of the circle
            # Draw circle center
            cv2.circle(image, center, 3, (0, 255, 0), -1)
            # Draw circle outline
            cv2.circle(image, center, radius, (255, 0, 0), 2)
    else:
        print("No circles detected")
    
    # Display the image.
    cv2.imshow('Canny', dImage)
    cv2.imshow('Hough Circle Transform', image)



def main():
    # Load original images
    imageB = cv2.imread('match.JPG')

    # Run individual edge segmentation functions

    houghCircle(imageB)
    cv2.waitKey(0)
    

if __name__ == '__main__':
    main()