import cv2
import numpy as np


class FeatureVectors():

    def __init__(self, image):
        self.image = image

    def __getMeanIntensity(self):
        meanIntensity = []
        for channel in range(3):
            channel_mean = np.average(self.image[:, :, channel])
            meanIntensity.append(round(channel_mean, 5))

        return meanIntensity

    def __getStdIntensity(self):
        stdIntensity = []
        for channel in range(3):
            channel_std = np.std(self.image[:, :, channel])
            stdIntensity.append(round(channel_std, 5))

        return stdIntensity

    def __getRGBHistogramVector(self):
        histogram_3d = cv2.calcHist([self.image], [0, 1, 2], None,
                                    [8, 8, 8], [0, 256, 0, 256, 0, 256])
        histogram_3d = histogram_3d.ravel()
        RGBHistogram = list(histogram_3d)

        return RGBHistogram

    def getFeatureVector(self):
        featureVectors = []
        meanIntensity = self.__getMeanIntensity()
        stdIntensity = self.__getStdIntensity()
        rgbHistogram = self.__getRGBHistogramVector()

        colorVectors = meanIntensity+stdIntensity+rgbHistogram
        featureVectors = colorVectors
        return featureVectors
