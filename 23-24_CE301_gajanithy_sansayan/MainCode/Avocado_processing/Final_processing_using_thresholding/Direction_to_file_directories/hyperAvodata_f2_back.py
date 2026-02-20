import spectral.io.envi as envi
from spectral import *  

avocado_f2_back = []

day1_hdrFile_Ha1 = "/mnt/d/day1/fruit2/avo_s1_f2_back_2024-03-11_15-14-12.hdr"
day1_BinFile_Ha1 = "/mnt/d/day1/fruit2/avo_s1_f2_back_2024-03-11_15-14-12.raw"
imgDay1_Ha1 = envi.open (day1_hdrFile_Ha1, day1_BinFile_Ha1).load()
avocado_f2_back.append(imgDay1_Ha1)

day2_hdrFile_Ha1  = "/mnt/d/day2/fruit2/avo_s1_f2_back_2024-03-12_13-41-32.hdr"
day2_BinFile_Ha1 = "/mnt/d/day2/fruit2/avo_s1_f2_back_2024-03-12_13-41-32.raw"
imgDay2_Ha1 = envi.open (day2_hdrFile_Ha1 , day2_BinFile_Ha1).load()
avocado_f2_back.append(imgDay2_Ha1)

day3_hdrFile_Ha1  = "/mnt/d/day3/fruit2/avo_s1_f2_back_2024-03-13_15-17-30.hdr"
day3_BinFile_Ha1 = "/mnt/d/day3/fruit2/avo_s1_f2_back_2024-03-13_15-17-30.raw"
imgDay3_Ha1 = envi.open (day3_hdrFile_Ha1 , day3_BinFile_Ha1).load()
avocado_f2_back.append(imgDay3_Ha1)

day4_hdrFile_Ha1  = "/mnt/d/day4/fruit2/avo_s1_f2_back_2024-03-14_14-17-21.hdr"
day4_BinFile_Ha1 = "/mnt/d/day4/fruit2/avo_s1_f2_back_2024-03-14_14-17-21.raw"
imgDay4_Ha1 = envi.open (day4_hdrFile_Ha1 , day4_BinFile_Ha1).load()
avocado_f2_back.append(imgDay4_Ha1)

day5_hdrFile_Ha1  = "/mnt/d/day5/fruit2/avo_s1_f2_back_2024-03-15_13-15-51.hdr"
day5_BinFile_Ha1 = "/mnt/d/day5/fruit2/avo_s1_f2_back_2024-03-15_13-15-51.raw"
imgDay5_Ha1 = envi.open (day5_hdrFile_Ha1 , day5_BinFile_Ha1).load()
avocado_f2_back.append(imgDay5_Ha1)

day8_hdrFile_Ha1  = "/mnt/d/day8/fruit2/avo_s1_f2_back_2024-03-18_14-25-18.hdr"
day8_BinFile_Ha1 = "/mnt/d/day8/fruit2/avo_s1_f2_back_2024-03-18_14-25-18.raw"
imgDay8_Ha1 = envi.open (day8_hdrFile_Ha1 , day8_BinFile_Ha1).load()
avocado_f2_back.append(imgDay8_Ha1)

day9_hdrFile_Ha1  = "/mnt/d/day9/fruit2/avo_s1_f2_back_2024-03-19_12-42-01.hdr"
day9_BinFile_Ha1 = "/mnt/d/day9/fruit2/avo_s1_f2_back_2024-03-19_12-42-01.raw"
imgDay9_Ha1 = envi.open (day9_hdrFile_Ha1 , day9_BinFile_Ha1).load()
avocado_f2_back.append(imgDay9_Ha1)