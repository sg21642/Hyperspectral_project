import spectral.io.envi as envi
from spectral import *  

avocado_f3_front  = []

day1_hdrFile_Ha1 = "/mnt/d/day1/fruit3/avo_s1_f3_front_2024-03-11_15-18-20.hdr"
day1_BinFile_Ha1 = "/mnt/d/day1/fruit3/avo_s1_f3_front_2024-03-11_15-18-20.raw"
imgDay1_Ha1 = envi.open (day1_hdrFile_Ha1, day1_BinFile_Ha1).load()
avocado_f3_front .append(imgDay1_Ha1)

day2_hdrFile_Ha1  = "/mnt/d/day2/fruit3/avo_s1_f3_front_2024-03-12_13-44-14.hdr"
day2_BinFile_Ha1 = "/mnt/d/day2/fruit3/avo_s1_f3_front_2024-03-12_13-44-14.raw"
imgDay2_Ha1 = envi.open (day2_hdrFile_Ha1 , day2_BinFile_Ha1).load()
avocado_f3_front .append(imgDay2_Ha1)

day3_hdrFile_Ha1  = "/mnt/d/day3/fruit3/avo_s1_f3_front_2024-03-13_15-19-58.hdr"
day3_BinFile_Ha1 = "/mnt/d/day3/fruit3/avo_s1_f3_front_2024-03-13_15-19-58.raw"
imgDay3_Ha1 = envi.open (day3_hdrFile_Ha1 , day3_BinFile_Ha1).load()
avocado_f3_front .append(imgDay3_Ha1)

day4_hdrFile_Ha1  = "/mnt/d/day4/fruit3/avo_s1_f3_front_2024-03-14_14-20-30.hdr"
day4_BinFile_Ha1 = "/mnt/d/day4/fruit3/avo_s1_f3_front_2024-03-14_14-20-30.raw"
imgDay4_Ha1 = envi.open (day4_hdrFile_Ha1 , day4_BinFile_Ha1).load()
avocado_f3_front .append(imgDay4_Ha1)

day5_hdrFile_Ha1  = "/mnt/d/day5/fruit3/avo_s1_f3_front_2024-03-15_13-19-39.hdr"
day5_BinFile_Ha1 = "/mnt/d/day5/fruit3/avo_s1_f3_front_2024-03-15_13-19-39.raw"
imgDay5_Ha1 = envi.open (day5_hdrFile_Ha1 , day5_BinFile_Ha1).load()
avocado_f3_front .append(imgDay5_Ha1)

day8_hdrFile_Ha1  = "/mnt/d/day8/fruit3/avo_s1_f3_front_2024-03-18_14-27-33.hdr"
day8_BinFile_Ha1 = "/mnt/d/day8/fruit3/avo_s1_f3_front_2024-03-18_14-27-33.raw"
imgDay8_Ha1 = envi.open (day8_hdrFile_Ha1 , day8_BinFile_Ha1).load()
avocado_f3_front .append(imgDay8_Ha1)

day9_hdrFile_Ha1  = "/mnt/d/day9/fruit3/avo_s1_f3_front_2024-03-19_12-44-24.hdr"
day9_BinFile_Ha1 = "/mnt/d/day9/fruit3/avo_s1_f3_front_2024-03-19_12-44-24.raw"
imgDay9_Ha1 = envi.open (day9_hdrFile_Ha1 , day9_BinFile_Ha1).load()
avocado_f3_front .append(imgDay9_Ha1)