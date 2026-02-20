import spectral.io.envi as envi
from spectral import *  

avocado_f3_back  = []

day1_hdrFile_Ha1 = "/mnt/d/day1/fruit3/avo_s1_f3_back_2024-03-11_15-21-07.hdr"
day1_BinFile_Ha1 = "/mnt/d/day1/fruit3/avo_s1_f3_back_2024-03-11_15-21-07.raw"
imgDay1_Ha1 = envi.open (day1_hdrFile_Ha1, day1_BinFile_Ha1).load()
avocado_f3_back .append(imgDay1_Ha1)

day2_hdrFile_Ha1  = "/mnt/d/day2/fruit3/avo_s1_f3_back_2024-03-12_13-43-07.hdr"
day2_BinFile_Ha1 = "/mnt/d/day2/fruit3/avo_s1_f3_back_2024-03-12_13-43-07.raw"
imgDay2_Ha1 = envi.open (day2_hdrFile_Ha1 , day2_BinFile_Ha1).load()
avocado_f3_back .append(imgDay2_Ha1)

day3_hdrFile_Ha1  = "/mnt/d/day3/fruit3/avo_s1_f3_back_2024-03-13_15-21-59.hdr"
day3_BinFile_Ha1 = "/mnt/d/day3/fruit3/avo_s1_f3_back_2024-03-13_15-21-59.raw"
imgDay3_Ha1 = envi.open (day3_hdrFile_Ha1 , day3_BinFile_Ha1).load()
avocado_f3_back .append(imgDay3_Ha1)

day4_hdrFile_Ha1  = "/mnt/d/day4/fruit3/avo_s1_f3_back_2024-03-14_14-19-18.hdr"
day4_BinFile_Ha1 = "/mnt/d/day4/fruit3/avo_s1_f3_back_2024-03-14_14-19-18.raw"
imgDay4_Ha1 = envi.open (day4_hdrFile_Ha1 , day4_BinFile_Ha1).load()
avocado_f3_back .append(imgDay4_Ha1)

day5_hdrFile_Ha1  = "/mnt/d/day5/fruit3/avo_s1_f3_back_2024-03-15_13-20-25.hdr"
day5_BinFile_Ha1 = "/mnt/d/day5/fruit3/avo_s1_f3_back_2024-03-15_13-20-25.raw"
imgDay5_Ha1 = envi.open (day5_hdrFile_Ha1 , day5_BinFile_Ha1).load()
avocado_f3_back .append(imgDay5_Ha1)

day8_hdrFile_Ha1  = "/mnt/d/day8/fruit3/avo_s1_f3_back_2024-03-18_14-28-40.hdr"
day8_BinFile_Ha1 = "/mnt/d/day8/fruit3/avo_s1_f3_back_2024-03-18_14-28-40.raw"
imgDay8_Ha1 = envi.open (day8_hdrFile_Ha1 , day8_BinFile_Ha1).load()
avocado_f3_back .append(imgDay8_Ha1)

day9_hdrFile_Ha1  = "/mnt/d/day9/fruit3/avo_s1_f3_back_2024-03-19_12-43-20.hdr"
day9_BinFile_Ha1 = "/mnt/d/day9/fruit3/avo_s1_f3_back_2024-03-19_12-43-20.raw"
imgDay9_Ha1 = envi.open (day9_hdrFile_Ha1 , day9_BinFile_Ha1).load()
avocado_f3_back .append(imgDay9_Ha1)