import os
import multiprocessing
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
    return vectors


def ThreadedFeatureExtraction(image_db_path, images_list):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(extractFeatureVectors, image_db_path+image)
                   for image in images_list]

    for f in concurrent.futures.as_completed(results):
        print(f.result())


start = time.perf_counter()

image_db_path = "Image_Database/"
image_paths = []
for img in os.listdir(image_db_path):
    image_paths.append(img)

for image in image_paths:
    print(extractFeatureVectors(image_db_path + image))
#ThreadedFeatureExtraction(image_db_path, image_paths)


end = time.perf_counter()
print(f"Time : {end-start}")
