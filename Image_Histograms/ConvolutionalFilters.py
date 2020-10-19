import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


class ConvolutionFilter():

    def __init__(self, image):
        self.image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

        self.sharpen = np.array(([0, -1, 0],
                                 [-1,  5, -1],
                                 [0, -1, 0]))

        self.sobelX = np.array([[-1, 0, 1],
                                [-2, 0, 2],
                                [-1, 0, 1]])

        self.sobelY = np.array(([-1, -2, -1],
                                [0,  0,  0],
                                [1,  2,  1]))

        self.laplacian = np.array(([0,  1, 0],
                                   [1, -4, 1],
                                   [0,  1, 0]))

    def __convolution(self, image_roi, kernel):
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
        image = self.image
        filtered_image = np.zeros(image.shape)

        for row in range(1, len(image)-1):
            for col in range(1, len(image[row])-1):

                pixels = image[row-1:row+2, col-1:col+2]
                pixel_kernel = (pixels * kernel).sum()
                if pixel_kernel > 0:
                    filtered_image[row, col] = pixel_kernel % 255
                else:
                    filtered_image[row, col] = 0

        return filtered_image

    def applySharpen(self):
        kernel = self.sharpen

        filtered_image = self.__applyFilter(kernel)
        return filtered_image

    def applySobelX(self):
        kernel = self.sobelX

        filtered_image = self.__applyFilter(kernel)
        return filtered_image

    def applySobelY(self):
        kernel = self.sobelY

        filtered_image = self.__applyFilter(kernel)
        return filtered_image

    def applyLaplacian(self):
        kernel = self.laplacian

        filtered_image = self.__applyFilter(kernel)
        return filtered_image

    def applyCannyEdge(self):

        filtered_image = cv2.Canny(self.image, 50, 240)
        return filtered_image
