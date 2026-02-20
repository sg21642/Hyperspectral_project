import spectral.io.envi as envi
from spectral import *


# path for the day 1 dataset
P_x =14; P_y = 14; rSize = 2

Mango_Front_data = []

day1_hdrFile_f1 = "/home/sayan/ce301/read_file/day1/mango_day_1_m3_01_front.hdr"
day1_BinFile_f1 = "/home/sayan/ce301/read_file/day1/mango_day_1_m3_01_front.bin"
imgDay1_front1 = envi.open (day1_hdrFile_f1, day1_BinFile_f1).load()
Mango_Front_data.append(imgDay1_front1[P_y:P_y+rSize,P_x:P_x+rSize, :])

day2_hdrFile_f1  = "/home/sayan/ce301/read_file/day2/mango_day_2_m3_01_front.hdr"
day2_BinFile_f1 = "/home/sayan/ce301/read_file/day2/mango_day_2_m3_01_front.bin"
imgDay2_front1 = envi.open (day2_hdrFile_f1 , day2_BinFile_f1).load()
Mango_Front_data.append(imgDay2_front1[P_y:P_y+rSize,P_x:P_x+rSize, :])

day3_hdrFile_f1  = "/home/sayan/ce301/read_file/day3/mango_day_3_m3_01_front.hdr"
day3_BinFile_f1 = "/home/sayan/ce301/read_file/day3/mango_day_3_m3_01_front.bin"
imgDay3_front1 = envi.open (day3_hdrFile_f1 , day3_BinFile_f1).load()
Mango_Front_data.append(imgDay3_front1[P_y:P_y+rSize,P_x:P_x+rSize, :])

day4_hdrFile_f1  = "/home/sayan/ce301/read_file/day4/mango_day_4_m3_01_front.hdr"
day4_BinFile_f1 = "/home/sayan/ce301/read_file/day4/mango_day_4_m3_01_front.bin"
imgDay4_front1 = envi.open (day4_hdrFile_f1 , day4_BinFile_f1).load()
Mango_Front_data.append(imgDay4_front1[P_y:P_y+rSize,P_x:P_x+rSize, :])

day5_hdrFile_f1  = "/home/sayan/ce301/read_file/day5/mango_day_5_m3_01_front.hdr"
day5_BinFile_f1 = "/home/sayan/ce301/read_file/day5/mango_day_5_m3_01_front.bin"
imgDay5_front1 = envi.open (day5_hdrFile_f1 , day5_BinFile_f1).load()
Mango_Front_data.append(imgDay5_front1[P_y:P_y+rSize,P_x:P_x+rSize, :])

day7_hdrFile_f1  = "/home/sayan/ce301/read_file/day7/mango_day_7_m3_01_front.hdr"
day7_BinFile_f1 = "/home/sayan/ce301/read_file/day7/mango_day_7_m3_01_front.bin"
imgDay7_front1 = envi.open (day7_hdrFile_f1 , day7_BinFile_f1).load()
Mango_Front_data.append(imgDay7_front1[P_y:P_y+rSize,P_x:P_x+rSize, :])

day8_hdrFile_f1  = "/home/sayan/ce301/read_file/day8/mango_day_8_m3_01_front.hdr"
day8_BinFile_f1 = "/home/sayan/ce301/read_file/day8/mango_day_8_m3_01_front.bin"
imgDay8_front1 = envi.open (day8_hdrFile_f1 , day8_BinFile_f1).load()
Mango_Front_data.append(imgDay8_front1[P_y:P_y+rSize,P_x:P_x+rSize, :])

day9_hdrFile_f1  = "/home/sayan/ce301/read_file/day9/mango_day_9_m3_01_front.hdr"
day9_BinFile_f1 = "/home/sayan/ce301/read_file/day9/mango_day_9_m3_01_front.bin"
imgDay9_front1 = envi.open (day9_hdrFile_f1 , day9_BinFile_f1).load()
Mango_Front_data.append(imgDay9_front1[P_y:P_y+rSize,P_x:P_x+rSize, :])

day10_hdrFile_f1  = "/home/sayan/ce301/read_file/day10/mango_day_10_m3_01_front.hdr"
day10_BinFile_f1 = "/home/sayan/ce301/read_file/day10/mango_day_10_m3_01_front.bin"
imgDay10_front1 = envi.open (day10_hdrFile_f1 , day10_BinFile_f1).load()
Mango_Front_data.append(imgDay10_front1[P_y:P_y+rSize,P_x:P_x+rSize, :])

day11_hdrFile_f1  = "/home/sayan/ce301/read_file/day11/mango_day_11_m3_01_front.hdr"
day11_BinFile_f1 = "/home/sayan/ce301/read_file/day11/mango_day_11_m3_01_front.bin"
imgDay11_front1 = envi.open (day11_hdrFile_f1 , day11_BinFile_f1).load()
Mango_Front_data.append(imgDay11_front1[P_y:P_y+rSize,P_x:P_x+rSize, :])

day12_hdrFile_f1  = "/home/sayan/ce301/read_file/day12/mango_day_12_m3_14_front.hdr"
day12_BinFile_f1 = "/home/sayan/ce301/read_file/day12/mango_day_12_m3_14_front.bin"
imgDay12_front1 = envi.open (day12_hdrFile_f1 , day12_BinFile_f1).load()
Mango_Front_data.append(imgDay12_front1[P_y:P_y+rSize,P_x:P_x+rSize, :])