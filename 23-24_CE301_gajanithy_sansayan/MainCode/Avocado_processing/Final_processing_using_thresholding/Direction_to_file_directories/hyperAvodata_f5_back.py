import spectral.io.envi as envi
from spectral import *  

avocado_f5_back = []

day1_hdrFile_Ha1 = "/mnt/d/day1/fruit5/avo_s1_f5_back_2024-03-11_15-51-42.hdr"
day1_BinFile_Ha1 = "/mnt/d/day1/fruit5/avo_s1_f5_back_2024-03-11_15-51-42.raw"
imgDay1_Ha1 = envi.open (day1_hdrFile_Ha1, day1_BinFile_Ha1).load()
avocado_f5_back.append(imgDay1_Ha1)

day2_hdrFile_Ha1  = "/mnt/d/day2/fruit5/avo_s1_f5_back_2024-03-12_13-48-03.hdr"
day2_BinFile_Ha1 = "/mnt/d/day2/fruit5/avo_s1_f5_back_2024-03-12_13-48-03.raw"
imgDay2_Ha1 = envi.open (day2_hdrFile_Ha1 , day2_BinFile_Ha1).load()
avocado_f5_back.append(imgDay2_Ha1)

day3_hdrFile_Ha1  = "/mnt/d/day3/fruit5/avo_s1_f5_back_2024-03-13_15-29-39.hdr"
day3_BinFile_Ha1 = "/mnt/d/day3/fruit5/avo_s1_f5_back_2024-03-13_15-29-39.raw"
imgDay3_Ha1 = envi.open (day3_hdrFile_Ha1 , day3_BinFile_Ha1).load()
avocado_f5_back.append(imgDay3_Ha1)

day4_hdrFile_Ha1  = "/mnt/d/day4/fruit5/avo_s1_f5_back_2024-03-14_14-26-42.hdr"
day4_BinFile_Ha1 = "/mnt/d/day4/fruit5/avo_s1_f5_back_2024-03-14_14-26-42.raw"
imgDay4_Ha1 = envi.open (day4_hdrFile_Ha1 , day4_BinFile_Ha1).load()
avocado_f5_back.append(imgDay4_Ha1)

day5_hdrFile_Ha1  = "/mnt/d/day5/fruit5/avo_s1_f5_back_2024-03-15_13-24-53.hdr"
day5_BinFile_Ha1 = "/mnt/d/day5/fruit5/avo_s1_f5_back_2024-03-15_13-24-53.raw"
imgDay5_Ha1 = envi.open (day5_hdrFile_Ha1 , day5_BinFile_Ha1).load()
avocado_f5_back.append(imgDay5_Ha1)

day8_hdrFile_Ha1  = "/mnt/d/day8/fruit5/avo_s1_f5_back_2024-03-18_14-35-59.hdr"
day8_BinFile_Ha1 = "/mnt/d/day8/fruit5/avo_s1_f5_back_2024-03-18_14-35-59.raw"
imgDay8_Ha1 = envi.open (day8_hdrFile_Ha1 , day8_BinFile_Ha1).load()
avocado_f5_back.append(imgDay8_Ha1)

day9_hdrFile_Ha1  = "/mnt/d/day9/fruit5/avo_s1_f5_back_2024-03-19_12-48-25.hdr"
day9_BinFile_Ha1 = "/mnt/d/day9/fruit5/avo_s1_f5_back_2024-03-19_12-48-25.raw"
imgDay9_Ha1 = envi.open (day9_hdrFile_Ha1 , day9_BinFile_Ha1).load()
avocado_f5_back.append(imgDay9_Ha1)