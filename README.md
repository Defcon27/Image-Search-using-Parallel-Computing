# CRISPR--CBIR-based-Rapid-Image-Seach-using-Parallel-Computing


[![GitHub last commit](https://img.shields.io/github/last-commit/Defcon27/Rapid-Image-Search-using-Parallel-Computing?label=Last%20commit&color=green&logo=git&logoColor=white&style=flat)](https://github.com/Defcon27/Data-Analysis-of-Indian-Automobile-dataset-using-Machine-Learning-in-R)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Defcon27/Rapid-Image-Search-using-Parallel-Computing?label=Code%20size&logo=python&logoColor=white&style=flat)
![GitHub repo size](https://img.shields.io/github/repo-size/Defcon27/Rapid-Image-Search-using-Parallel-Computing?label=Repo%20size&color=red&logo=github&logoColor=white&style=flat)
![GitHub stars](https://img.shields.io/github/stars/Defcon27/Rapid-Image-Search-using-Parallel-Computing?label=Stars&logo=github&style=flat)
![GitHub issues](https://img.shields.io/github/issues/Defcon27/Rapid-Image-Search-using-Parallel-Computing?label=Issues&color=yellow&logo=github&style=flat)


#### CRISPR is a CBIR(Content Based Image Search) based Image Search application that is capable of retrieving similar images of query image input from a database of images. This system uses the concept of parallel computing to speed up the search thus reducing the time required to retrieve the images. 

## ABSTRACT
<p align="justify">
With the massive  growth of the internet, people can gain access to a massive amount of information. Due to this retrieving the information of interest becomes very difficult. If focused on visual information, the internet contains several kinds of images and other visual information, such as videos, movies in various formats such as JPG, PNG, BMP and even GIF. Hence there is a need for such an image search engine using which the related and exact images can be searched. Content-based image retrieval seeks to find
methods to index, browse, and query large image databases by using meaningful feature extraction and comparison methods for images. CBIR system uses feature extraction which is the process of obtaining the most relevant information from the original image and represent it in a reduced representation of a set of features like texture, shape using algorithms which process the image data and store them.<br>
But to implement such kind of algorithms in real-world applications we need the algorithm to be executed in the least time possible so as to increase the performance of the system. This speed-up of performance can be achieved since feature extraction and comparison of visual features used for the content-based image retrieval can be realized by using the concept of parallel computing. Since the algorithms dealing with the extraction process are huge and complex, with the help of parallelization this heavy process can be divided into multiple smaller tasks and execute them at the same time. The main purpose of parallelization is to provide simultaneous execution of two or more parts of the program to utilize the CPU resources to the maximum increasing CPU utilization. This helps the program to run faster, smoother, and much efficient in resource utilization. Thus, the implementation of parallelization in image search could greatly reduce the retrieval time and improve the performance of retrieval system which is critical in any search applications. Since users usually work with a huge number of images, it is important to achieve the highest performance possible from that code. To achieve this, we make use of parallelization.
</p>

<br>

## INTRODUCTION
<p align="justify">
Huge collection of digital images is collected due to the improvement in the digital storage media, image capturing devices like scanners, web cameras, digital cameras and rapid development in internet. Due to these reasons there is a need to implement new programs in such a that it gives the best performance using the same resources as before and at the same time reducing the time to retrieve images from the system. Image retrieval is achieved through low level features that are extracted from the images by the extraction algorithm and then these features are represented in a form called feature vector. These feature vectors are calculated statistical values like standard deviation. Similarity is measured to rank the images by calculating the distance between the query image feature vector and feature vectors of database images. Since this algorithm performs various number of computations in order to obtain the feature vectors for the image it usually executes the computation sequentially and finally obtain the required results. This method works but in order to increase the CPU utilization of the multi-processor systems to the maximum and to reduce the computation time we can make use of multithreading. 
With the help of multithreading heavy processes can be divided into multiple threads and execute them at the same time. With the application of multithreading into this process instead of sequentially computing the data, each thread can take a particular function assigned to them and these threads execute simultaneously and when joined gives back the result of the computation assigned to them. Here in this method each thread can handle the calculation of various tasks like data extraction, histogram refinement, calculation of feature vectors and finally produces the results of the computation simultaneously at the same making the process execution a whole lot faster since computation is performed in parallel rather than serial execution. Thus, have achieved the goal of improving the performance of the system with the use of multithreading to enable efficient and fast execution of the program.
</p>

<p><br></p>


## PROPOSED ARCHITECTURE
<p align="middle"> <img align="right" src='Docs/achitecture.png' width=40%/> <p>


