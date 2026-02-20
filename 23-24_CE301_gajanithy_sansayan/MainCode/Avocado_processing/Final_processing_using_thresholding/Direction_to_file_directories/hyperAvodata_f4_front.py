import spectral.io.envi as envi
from spectral import *  

avocado_f4_front  = []

day1_hdrFile_Ha1 = "/mnt/d/day1/fruit4/avo_s1_f4_front_2024-03-11_15-35-28.hdr"
day1_BinFile_Ha1 = "/mnt/d/day1/fruit4/avo_s1_f4_front_2024-03-11_15-35-28.raw"
imgDay1_Ha1 = envi.open (day1_hdrFile_Ha1, day1_BinFile_Ha1).load()
avocado_f4_front .append(imgDay1_Ha1)

day2_hdrFile_Ha1  = "/mnt/d/day2/fruit4/avo_s1_f4_front_2024-03-12_13-45-24.hdr"
day2_BinFile_Ha1 = "/mnt/d/day2/fruit4/avo_s1_f4_front_2024-03-12_13-45-24.raw"
imgDay2_Ha1 = envi.open (day2_hdrFile_Ha1 , day2_BinFile_Ha1).load()
avocado_f4_front .append(imgDay2_Ha1)

day3_hdrFile_Ha1  = "/mnt/d/day3/fruit4/avo_s1_f4_front_2024-03-13_15-27-15.hdr"
day3_BinFile_Ha1 = "/mnt/d/day3/fruit4/avo_s1_f4_front_2024-03-13_15-27-15.raw"
imgDay3_Ha1 = envi.open (day3_hdrFile_Ha1 , day3_BinFile_Ha1).load()
avocado_f4_front .append(imgDay3_Ha1)

day4_hdrFile_Ha1  = "/mnt/d/day4/fruit4/avo_s1_f4_front_2024-03-14_14-24-36.hdr"
day4_BinFile_Ha1 = "/mnt/d/day4/fruit4/avo_s1_f4_front_2024-03-14_14-24-36.raw"
imgDay4_Ha1 = envi.open (day4_hdrFile_Ha1 , day4_BinFile_Ha1).load()
avocado_f4_front .append(imgDay4_Ha1)

day5_hdrFile_Ha1  = "/mnt/d/day5/fruit4/avo_s1_f4_front_2024-03-15_13-22-43.hdr"
day5_BinFile_Ha1 = "/mnt/d/day5/fruit4/avo_s1_f4_front_2024-03-15_13-22-43.raw"
imgDay5_Ha1 = envi.open (day5_hdrFile_Ha1 , day5_BinFile_Ha1).load()
avocado_f4_front .append(imgDay5_Ha1)

day8_hdrFile_Ha1  = "/mnt/d/day8/fruit4/avo_s1_f4_front_2024-03-18_14-31-14.hdr"
day8_BinFile_Ha1 = "/mnt/d/day8/fruit4/avo_s1_f4_front_2024-03-18_14-31-14.raw"
imgDay8_Ha1 = envi.open (day8_hdrFile_Ha1 , day8_BinFile_Ha1).load()
avocado_f4_front .append(imgDay8_Ha1)

day9_hdrFile_Ha1  = "/mnt/d/day9/fruit4/avo_s1_f4_front_2024-03-19_12-46-24.hdr"
day9_BinFile_Ha1 = "/mnt/d/day9/fruit4/avo_s1_f4_front_2024-03-19_12-46-24.raw"
imgDay9_Ha1 = envi.open (day9_hdrFile_Ha1 , day9_BinFile_Ha1).load()
avocado_f4_front .append(imgDay9_Ha1)