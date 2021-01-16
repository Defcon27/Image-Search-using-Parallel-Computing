import cv2
import numpy as np
from Image_Filters.NoiseReduction import NoiseReduction
from Image_Filters.ConvolutionalFilters import ConvolutionFilter


class FeatureVectors():
    """Extracts various feature vectors from image """

    def __init__(self, image):
        self.filter = NoiseReduction(image)
        self.image = self.filter.applyGaussianBlur()

    def __getMeanIntensity(self):
        # Returns the mean intensity of image

        meanIntensity = []
        for channel in range(3):
            channel_mean = np.average(self.image[:, :, channel])
            meanIntensity.append(round(channel_mean, 5))

        return meanIntensity

    def __getStdIntensity(self):
        # Returns the standard deviation of intensity of image

        stdIntensity = []
        for channel in range(3):
            channel_std = np.std(self.image[:, :, channel])
            stdIntensity.append(round(channel_std, 5))

        return stdIntensity

    def __getRGBHistogramVector(self):
        # Returns the 3-D(RGB) Histogram vector of image

        histogram_3d = cv2.calcHist([self.image], [0, 1, 2], None,
                                    [12, 12, 12], [0, 256, 0, 256, 0, 256])
        histogram_3d = histogram_3d.ravel()
        RGBHistogram = list(histogram_3d)

        return RGBHistogram

    def __getHuMoments(self):
        # Returns Hu-Moments vector of image

        filter = ConvolutionFilter(self.image)
        canny_filtered = filter.applyCannyEdge()
        canny_huMoments = cv2.HuMoments(cv2.moments(canny_filtered)).flatten()
        huVector = list(canny_huMoments.ravel())
        return huVector

    def getFeatureVector(self):
        """ Return a python list of complete feature vectors
        Extracts Statistics, 3-D Histogram, HuMoments from image and appends into single list
        """

        featureVectors = []
        meanIntensity = self.__getMeanIntensity()
        stdIntensity = self.__getStdIntensity()
        rgbHistogram = self.__getRGBHistogramVector()
        huVectors = self.__getHuMoments()

        colorVectors = meanIntensity+stdIntensity+rgbHistogram
        featureVectors = colorVectors+huVectors
        return featureVectors
