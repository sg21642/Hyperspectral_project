# Hyperspectral Fruit Ripeness Detection

Final Year Dissertation Project  
BEng Computers with Electronics  
University of Essex  

Author: Sansayan Gajanithy  
Supervisor: Dr Adrian Clark  

---

## Project Overview

This project investigates the use of hyperspectral imaging to measure the ripeness of avocados.

Hyperspectral imaging captures information across multiple wavelengths of the electromagnetic spectrum (400–1000 nm). Unlike normal RGB images, hyperspectral data provides detailed spectral signatures that allow subtle changes in fruit maturity to be detected.

The objective of this project is to:

- Record hyperspectral data of avocados
- Process spectral information
- Measure reflectance changes across ripening stages
- Classify avocados as:
  - Unripe
  - Perfectly Ripe
  - Overripe

The system uses spectral analysis and threshold-based classification to determine fruit maturity.

---

## How the System Works

1. Hyperspectral data is captured using a Specim FX10e imager.
2. The data is exported into Python for analysis.
3. The avocado is segmented from the background using masking techniques.
4. Mean reflectance values are calculated across selected spectral bands.
5. Thresholding is applied to classify the ripeness stage.

As the avocado ripens, reflectance values decrease in specific wavelength ranges.  
This measurable decline is used to determine maturity.

---

## Technologies Used

- Python 3
- Spectral Python (SPy)
- NumPy
- OpenCV
- Matplotlib
- SciPy
- Jupyter Notebook

---

## Installation

Clone the repository:

```bash
git clone https://github.com/sg21642/Hyperspectral_project.git
cd Hyperspectral_project
