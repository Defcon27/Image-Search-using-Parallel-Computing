import os
import time
import cv2
import matplotlib.pyplot as plt


image_db_path = "Image_Database/"
for img in os.listdir(image_db_path):

    image = cv2.imread(image_db_path+img)
    image = cv2.resize(image, (1000, 1000))
    image_y = image.shape[0]
    image_x = image.shape[1]

    # plt.imshow(image)
    # plt.show()

    tot_inten = 0
    for y in range(image_y):
        for x in range(image_x):
            #print(image[y, x])
            tot_inten += image[y, x][1]

    print(tot_inten/(image_y*image_x))


# img = cv2.imread("Image_Database/100000.jpg")
# plt.imshow(img)
# plt.show()
