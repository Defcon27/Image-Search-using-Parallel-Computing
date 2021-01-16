import cv2
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plotRGBDistribution(image, axis):
    # Plots RGB distribution using Histogram of input image

    df = pd.DataFrame()
    df["Intensity"] = image[:, :, 0].ravel()
    df["color"] = "b"
    df2 = pd.DataFrame()
    df2["Intensity"] = image[:, :, 1].ravel()
    df2["color"] = "g"
    df3 = pd.DataFrame()
    df3["Intensity"] = image[:, :, 2].ravel()
    df3["color"] = "r"
    df = df.append(df2)
    df = df.append(df3)

    sns.histplot(df, x="Intensity", bins=256, hue="color",
                 element="step", palette=["C0", "C2", "tomato"], ax=axis)
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Pixel Count")


def plotGrayDistribution(image, axis):
    # Plots Gray Intensity distribution using Histogram of input image

    sns.histplot(image.ravel(), bins=256, element="step",
                 color="dimgray", ax=axis)
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Pixel Count")


def plotConvolveDistribution(image, bins, axis):
    # Plots Gray Intensity distribution using Histogram of input convolved image

    sns.histplot(image.ravel(), bins=bins, element="step",
                 color="dimgray", ax=axis)
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Pixel Count")
