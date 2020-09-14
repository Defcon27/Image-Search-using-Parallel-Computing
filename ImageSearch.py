import os
import multiprocessing
import threading
import concurrent.futures
import time
import cv2
import matplotlib.pyplot as plt


def avgIntensity(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (1000, 1000))
    image_y = image.shape[0]
    image_x = image.shape[1]

    tot_intensity = 0
    for y in range(image_y):
        for x in range(image_x):
            tot_intensity += image[y, x][1]

    avg = (tot_intensity/(image_y*image_x))
    return avg


start = time.perf_counter()


image_db_path = "Image_Database/"
image_paths = []
for img in os.listdir(image_db_path):
    image_paths.append(image_db_path+img)

# for image in image_paths:
#     print(avgIntensity(image))
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(avgIntensity, image_path)
               for image_path in image_paths]

    for f in concurrent.futures.as_completed(results):
        print(f.result())


end = time.perf_counter()
print(f"Time : {end-start}")
