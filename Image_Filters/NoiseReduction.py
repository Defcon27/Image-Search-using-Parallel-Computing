import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


class NoiseReduction():
    """Converts input image to grayscale and reduces noise in the image"""

    def __init__(self, image):
        self.image = image

        self.smallBlur = np.ones((7, 7), dtype="float") * (1.0 / (7 * 7))

        self.largeBlur = np.ones((21, 21), dtype="float") * (1.0 / (21 * 21))

    def __convolution(self, image_roi, kernel):
        # This function convolves the input kernel on the input image region of interest 

        kernel_dimension = len(kernel)
        pixel_sum = 0

        for i in range(kernel_dimension):
            for j in range(kernel_dimension):
                pixel_kernel_value = image_roi[i, j]*kernel[i, j]
                pixel_sum = pixel_sum+pixel_kernel_value

        if pixel_sum < 0:
            return 0
        else:
            return pixel_sum % 255

    def __applyFilter(self, kernel):
        """ Returns convolved image 
        Applies the input convolution filter onto the image 
        """

        image = self.image
        kernel_dimension = len(kernel)
        kernel_margin = kernel_dimension//2
        filtered_image = np.zeros(image.shape)

        for row in range(kernel_margin, len(image)-kernel_margin):
            for col in range(kernel_margin, len(image[row])-kernel_margin):

                pixels = image[row-kernel_margin:row+kernel_margin+1,
                               col-kernel_margin:col+kernel_margin+1]
                pixel_kernel = (pixels * kernel).sum()
                if pixel_kernel > 0:
                    filtered_image[row, col] = pixel_kernel % 255
                else:
                    filtered_image[row, col] = 0

        return filtered_image

    def applySmallBlur(self):
        """Returns image applied with small blur filter"""

        kernel = self.smallBlur
        image = self.image
        blured_image = cv2.filter2D(image, -1, kernel)
        return blured_image

    def applyLargeBlur(self):
        """Returns image applied with large blur filter"""

        kernel = self.largeBlur
        image = self.image
        blured_image = cv2.filter2D(image, -1, kernel)
        return blured_image

    def applyGaussianBlur(self):
        """Returns image applied with Gaussian blur filter"""

        image = self.image
        filtered_image = cv2.GaussianBlur(image, (9, 9), 0)
        return filtered_image
