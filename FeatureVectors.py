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

    def getFeatureVector(self):
        featureVectors = []
        meanIntensity = self.__getMeanIntensity()
        stdIntensity = self.__getStdIntensity()

        featureVectors = meanIntensity+stdIntensity
        return featureVectors
