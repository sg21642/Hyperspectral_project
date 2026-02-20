# Imager Reading and Documentations
The Imager which will be used to record spectral data is the Specim fx10e. In order to record the spectral data, there should be an established connectivity between the imager and a PC. There are series of background reading done during week 3-5 of the imager and it operation. This is done by reading the manuals of the Spacim fx10e image, Lumo Scanner (pre installed software) and SpecimSDK. 

## Imager connectivity operation
Spectral imager uses digital imaging with spectroscopy to detect spectral information in image pixels.Imager has a wide range of wavelength than other cameras. This is due to its capability to measure spectral data in various different bands.The Spacim fx10e is connected to a PC via ethernet and once powered on it can be controlled by the pc through a software development kit or Scanner. This imager has operating range of 400 to 1000 nm with Camera link. Camera link is communication standard which ensures large number of data can be transferred at a faster timing. The imager is mounter with two halogen lights and a tray bellow to hold the objects for recording. the halogen lights are to record data under halogen spectrum. there are also other spectrums which the data can be recorded as sunlight illumination and LED illumination.

There are lED indicator are embedded into the camera to indicate the imager operation. 
* LED not lit -> power off
* LED blinking green in start up -> starting
* LED stable green -> power on , not recording
* LED blinking green -> power on and recording

The imager has an inbuilt correction handle which records images at the desired way according to the controller of the pc. The image has define region of interest which outputs as the desired data and the recording can be simultaneous.The maximum the imager can record at the resolution 1312 x 1082, but an optimal resolution for data recording is 1024 x 1024 or below.

## Software development kit
the imager data can be mitigated by a software development kit. The imager is supported with SpecSensor SDK by Specim. This SDK is a C based API which can use its own libraries to record spectral data by operating the imager. THe SDK sends commands to the camera with out a GUI. The data is recorded, and transferred to a file system.
There are several complication to using the SDK. 
1. It is time consuming process of wring program in c to acquire data resulting in less time to be spent on the analysis.
2. The SDK is given with the imager purchase but the SDK has to be verified with the licensing to be ready to operate.
3. It is bind to a single computer, meaning the data acquisition is not possible on other machine over the same network.

This simplifies the reason it will not be used in this project.

## Lumo scanner and operation
The imager also come with a pre built scanner which can be installed on multiple machines and used.The scanner has three interfaces which define the da ta acquisitions:
Setup -> configures the imager and set preference on the data
Adjust -> the viewing format so the user can adjust the data 
Capture -> Export data to the PC

The scanner is best fit to be used as it reduces the time constraints and easy handling of recording data.

## Image Data
The Image data outputted by the image is ENVI file formatted.ENVI stands for Environment for Visualizing Images, which is a common file standard for image processing. The ENVI format outputs two files:
1. a header file which holds all the image definition information like number of bands.
2. a raw file (usually a binary file) which holds the information of the image in binary.
These file is to be merged together to create the image. This can be done in multiple. On this project these files are opened and loads the image with spectral python (envi package). 
The image data is outputted by the imager in large size. This is due to high resolution image is defined in the the files. the higher the resolution, the larger the size the file is. A normal data can be at the size of 50000 kb at least. This also means the higher resolution the image is the more accurate the wavelength information is.

## Images access issue & Risk assessment 
The project faces a massive backlog due the delays in the gaining access to imager. The imager is an expensive piece of equipment and the operation should approached with care. It is stated that there should be a risk assessment to be signed off before providing the access to the imager. The spectral imager is currently hidden in an lab. There has been a risk assessment has been made to be signed off, but the university want to place more stricter measures when using this imager.
There has been a constant chasing since week 2 onwards by the Student and the supervisor but all in vain as the imager access still not processed and pushed to an unknown date.The imager operation is essential as the pre recorded data acquired is very low in resolution and conflict over the integrity of the project. There are series of reading has been done on the imager operation which all referred to the imager and scanner manuals. 

The current state is that imager reading has been completed and imager operation is ready to be commenced.The current plan is to work on analysis 1 and keep chapter 2 (image operation) and chapter 3 (data recording) to be pushed to a later date. 


During Phase 2, imager access has been granted as the issue has been taken to the view of the CSEE head of school and the imager formalities has been sorted towards the end of semester 2 and a data set has been recorded. when an evaluation of the imager system has been granted, there was limitation of the imager access as facility is made ready for the open day event. This made the study to be conducted only for a single day.

## References
 [1] Specim Oy. "Specim FX10 - Reference Manual 2.1." Oulu, Finland: Specim Oy.

 [2]Specim Oy. "Labscanner 40x20 User Guide Version 1.1" Oulu, Finland: Specim Oy.

 [3]Specim Oy. "Lumo Scanner - User Guide 1.2" Oulu, Finland: Specim Oy.

 [4]Specim Oy. "SpecSensor SDK 1.2" Oulu, Finland: Specim Oy.

 Any of these resources can be given on request as they are not a published source.
