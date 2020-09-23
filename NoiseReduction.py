import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


class NoiseReduction():

    def __init__(self, image):
        pass

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
