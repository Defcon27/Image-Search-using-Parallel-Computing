import os
import sys
import threading
import concurrent.futures
import time
import cv2
import matplotlib.pyplot as plt
from FeatureVectors import FeatureVectors
from QuerySearch import QuerySearch


def extractFeatureVectors(image_path):
    # Extracts feature vectors for input image

    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (500, 500))
    featureVectors = FeatureVectors(image)
    vectors = featureVectors.getFeatureVector()

    imageName = image_path.split("/")[-1]
    return [imageName, vectors]


def ThreadedFeatureExtraction(images_list):
     # Performing feature extraction of databse images using multithreading

    features = {}
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(extractFeatureVectors, image_path)
                   for image_path in images_list]

    for f in concurrent.futures.as_completed(results):
        imageName, vectors = f.result()
        features[imageName] = vectors

    return features


def getImg(img):
    image_db_path = "Image_Database/"
    image = cv2.imread(image_db_path+img)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image


def ImageSearch(queryImage):
    # Performs Image Search using Query image

    image_db_path = "Image_Database/"
    image_paths = []
    for img in os.listdir(image_db_path):
        image_paths.append(image_db_path+img)

    features = ThreadedFeatureExtraction(image_paths)

    queryImage_path = image_db_path+queryImage
    imageName, queryVector = extractFeatureVectors(queryImage_path)

    search = QuerySearch(queryVector, features)

    results = search.performSearch()
    results.sort(key=lambda res: res[1])

    return results
