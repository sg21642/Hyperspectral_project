# Analysis 1
It is decide that the analysis one should export mango spectral data files and plot information and a GIF animation should be drawn. Mango dat has been selected as it is less in size of 2.2 GB and it sufficient for analysis 1 as it focus on experimentation. Only then Avocado data to be used after the winter in machine learning analysis
## Exporting Spectral Data 
The spectral data is exported into spectral python using the envi call through spectral library.
ENVI stands for “Environment for Visualizing Images”, a common file format for image processing of spectral data
        * The spectral data are in envi format and include two files:
                1. Header file (.hdr) -> metadata which contains definitions of the image
                2. Binary file (.bin) -> contains the pixels values as binaries
Clear pathways of these files are provided to the program which envi opens and loads the image into an array object.
Example:
``` python
# path for the day 1 dataset
day1_hdrFile = "/home/sayan/ce301/read_file/day1/mango_day_1_m3_01_front.hdr"
day1_BinFile = "/home/sayan/ce301/read_file/day1/mango_day_1_m3_01_front.bin"

# using envi to import the and reading data
imgDay1 = envi.open (day1_hdrFile, day1_BinFile).load()
```
## Using matplotlib and K-means[1] to plot information
Python uses matplotlib to plot per pixel spectral.
The information plotted using matplotlib are cluster of wavelengths for a specific region of the image.
Image regions are specified by defining a pixel and extending the region:
The cluster of wavelengths is processed through K-Means.

K-means is an algorithm used in machine learning data analysis.
1. It is initialised with the number of cluster to identify data
2. Figures out groups of clusters and assigns each cluster to the nearest centroid, which is the mean value 
3. Returns the centroids.
```python 
(a, a1) = kmeans(Mango_Front_data[0],5,100)
```

![Image spectral clusters](https://miro.medium.com/v2/resize:fit:640/format:webp/0*AYHo5J8MUmngdjxa)
![Image spectral clusters with K-means centroids](https://miro.medium.com/v2/resize:fit:640/format:webp/0*vf08X44o0XgHVXvv)
   
The returned data is then plotted using matplotlib with y = reflectance and x =wavelength.clusters


## Animation (GIF)
It is decided that an animation of GIF should be programmed to visualise day by day of the spectral data. This is done trough matplotlib animation frame work which creates sub plots and merges the data drawn. 
## observation 
In observation it is visible through the animation the mango data is that as the fruit ripens the wavelength's reflectance level goes down. This is a positive result as it is a clear indication that program work with spectral data. Also the general structure of the graph data remained the same.
### Accuracy:
Although this graph-based animation made a positive reading of the expected data, there could be more accurate and finite tests can be implemented. 
The test data of the mangos are 64 x 64 pixels, which are very low in resolution. 
As mentioned earlier Higher spectral resolution allows for more detailed and accurate identification of spectra.
The mango data analysis is an earlier experiment and in analysis 2 it will be shifted to avocado data.
Once the imager access issue is solved, the own recorded data used will be in high resolution.


## References
[1] Author(s): A. Sachan Title: "Understanding K-means Clustering in Machine Learning" URL: https://towardsdatascience.com/understanding-k-means-clustering-in-machine-learning-6a6e67336aa1