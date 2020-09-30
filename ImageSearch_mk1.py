import os
import threading
import concurrent.futures
import time
import cv2
import matplotlib.pyplot as plt
from FeatureVectors import FeatureVectors


def extractFeatureVectors(image_path):

    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (500, 500))
    featureVectors = FeatureVectors(image)
    vectors = featureVectors.getFeatureVector()

    imageName = image_path.split("/")[-1]
    return [imageName, vectors]


def ThreadedFeatureExtraction(images_list):
    features = {}
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(extractFeatureVectors, image_path)
                   for image_path in images_list]

    for f in concurrent.futures.as_completed(results):
        imageName, vectors = f.result()
        features[imageName] = vectors

    return features


if __name__ == "__main__":

    start = time.perf_counter()

    image_db_path = "Image_Database/"
    image_paths = []
    for img in os.listdir(image_db_path):
        image_paths.append(image_db_path+img)

    lists = [image_paths, image_paths, image_paths, image_paths]

    # for image in image_paths:
    #     print(extractFeatureVectors(image))

    features = ThreadedFeatureExtraction(image_paths)
    print(features)

    end = time.perf_counter()
    print(f"Time : {end-start}")
