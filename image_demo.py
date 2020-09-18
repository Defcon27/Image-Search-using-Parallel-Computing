import os
import cv2
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plotRGBDistribution(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (100, 100))

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

    sns.displot(df, x="Intensity", hue="color",
                kind="kde", fill=True, palette=["C0", "C2", "tomato"])
