import spectral.io.envi as envi
from spectral import *


# path for the day 1 dataset
P_x =14; P_y = 14; rSize = 2

Mango_Back_data = []

day1_hdrFile_b1 = "/home/sayan/ce301/mango_data_back/day1/mango_day_1_m3_01_back.hdr"
day1_BinFile_b1 = "/home/sayan/ce301/mango_data_back/day1/mango_day_1_m3_01_back.bin"
imgDay1_back1 = envi.open (day1_hdrFile_b1, day1_BinFile_b1).load()
Mango_Back_data.append(imgDay1_back1[P_y:P_y+rSize,P_x:P_x+rSize, :])

day2_hdrFile_b1 = "/home/sayan/ce301/mango_data_back/day2/mango_day_2_m3_01_back.hdr"
day2_BinFile_b1 = "/home/sayan/ce301/mango_data_back/day2/mango_day_2_m3_01_back.bin"
imgDay2_back1 = envi.open (day2_hdrFile_b1 , day2_BinFile_b1).load()
Mango_Back_data.append(imgDay2_back1[P_y:P_y+rSize,P_x:P_x+rSize, :])

day3_hdrFile_b1 = "/home/sayan/ce301/mango_data_back/day3/mango_day_3_m3_01_back.hdr"
day3_BinFile_b1 = "/home/sayan/ce301/mango_data_back/day3/mango_day_3_m3_01_back.bin"
imgDay3_back1 = envi.open (day3_hdrFile_b1 , day3_BinFile_b1).load()
Mango_Back_data.append(imgDay3_back1[P_y:P_y+rSize,P_x:P_x+rSize, :])

day4_hdrFile_b1 = "/home/sayan/ce301/mango_data_back/day4/mango_day_4_m3_01_back.hdr"
day4_BinFile_b1 = "/home/sayan/ce301/mango_data_back/day4/mango_day_4_m3_01_back.bin"
imgDay4_back1 = envi.open (day4_hdrFile_b1 , day4_BinFile_b1).load()
Mango_Back_data.append(imgDay4_back1[P_y:P_y+rSize,P_x:P_x+rSize, :])

day5_hdrFile_b1 = "/home/sayan/ce301/mango_data_back/day5/mango_day_5_m3_01_back.hdr"
day5_BinFile_b1 = "/home/sayan/ce301/mango_data_back/day5/mango_day_5_m3_01_back.bin"
imgDay5_back1 = envi.open (day5_hdrFile_b1 , day5_BinFile_b1).load()
Mango_Back_data.append(imgDay5_back1[P_y:P_y+rSize,P_x:P_x+rSize, :])

day7_hdrFile_b1 = "/home/sayan/ce301/mango_data_back/day7/mango_day_7_m3_01_back.hdr"
day7_BinFile_b1 = "/home/sayan/ce301/mango_data_back/day7/mango_day_7_m3_01_back.bin"
imgDay7_back1 = envi.open (day7_hdrFile_b1 , day7_BinFile_b1).load()
Mango_Back_data.append(imgDay7_back1[P_y:P_y+rSize,P_x:P_x+rSize, :])

day8_hdrFile_b1 = "/home/sayan/ce301/mango_data_back/day8/mango_day_8_m3_01_back.hdr"
day8_BinFile_b1 = "/home/sayan/ce301/mango_data_back/day8/mango_day_8_m3_01_back.bin"
imgDay8_back1 = envi.open (day8_hdrFile_b1 , day8_BinFile_b1).load()
Mango_Back_data.append(imgDay8_back1[P_y:P_y+rSize,P_x:P_x+rSize, :])

day9_hdrFile_b1 = "/home/sayan/ce301/mango_data_back/day9/mango_day_9_m3_01_back.hdr"
day9_BinFile_b1 = "/home/sayan/ce301/mango_data_back/day9/mango_day_9_m3_01_back.bin"
imgDay9_back1 = envi.open (day9_hdrFile_b1 , day9_BinFile_b1).load()
Mango_Back_data.append(imgDay9_back1[P_y:P_y+rSize,P_x:P_x+rSize, :])

day10_hdrFile_b1 = "/home/sayan/ce301/mango_data_back/day10/mango_day_10_m3_01_back.hdr"
day10_BinFile_b1 = "/home/sayan/ce301/mango_data_back/day10/mango_day_10_m3_01_back.bin"
imgDay10_back1 = envi.open (day10_hdrFile_b1 , day10_BinFile_b1).load()
Mango_Back_data.append(imgDay10_back1[P_y:P_y+rSize,P_x:P_x+rSize, :])

day11_hdrFile_b1 = "/home/sayan/ce301/mango_data_back/day11/mango_day_11_m3_01_back.hdr"
day11_BinFile_b1 = "/home/sayan/ce301/mango_data_back/day11/mango_day_11_m3_01_back.bin"
imgDay11_back1 = envi.open (day11_hdrFile_b1 , day11_BinFile_b1).load()
Mango_Back_data.append(imgDay11_back1[P_y:P_y+rSize,P_x:P_x+rSize, :])

day12_hdrFile_b1 = "/home/sayan/ce301/mango_data_back/day12/mango_day_12_m3_14_back.hdr"
day12_BinFile_b1 = "/home/sayan/ce301/mango_data_back/day12/mango_day_12_m3_14_back.bin"
imgDay12_back1 = envi.open (day12_hdrFile_b1 , day12_BinFile_b1).load()
Mango_Back_data.append(imgDay12_back1[P_y:P_y+rSize,P_x:P_x+rSize, :])