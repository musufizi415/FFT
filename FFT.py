import numpy as np
import copy

point_num = 8 #任意（2^nのみ）
data = [2, 6, 9, 1, 9, 25, 23, 10] ##任意


data_int = data_int = copy.copy(data) #data整数部
data_img = [0] * point_num #data虚数部

print(np.fft.fft(data))    #比較用

##データの並び替えを行う（偶数と奇数に分ける）

data_order = [0] * point_num
level = int(np.log2(point_num))
for k in range(level) :
    
    m = 0
    big_cycle = point_num/ 2**(k + 1)
    small_cycle = 2**k

    for n in range(int(big_cycle)) :

        m += small_cycle
        
        for i in range(small_cycle) :
            data_order[m] = data_order[m] + int(big_cycle)
            m += 1


for k in range(point_num): #作った順番にデータを並び替え
    data[k] = data_int[data_order[k]]
    #print(data_order[k])
    

data_int = copy.copy(data)



###バタフライ演算部
stage = int(np.log2(point_num))
PI = np.pi
for k in range(stage):#stage

    m = 0
    big_cycle = point_num/ 2**(k + 1)
    small_cycle = 2**k
    data_int_copy=copy.copy(data_int)
    data_img_copy=copy.copy(data_img)

    #####バタフライ演算内W（回転子）をかける
    for n in range(int(big_cycle)) :

        m += small_cycle
        
        for i in range(small_cycle) :
            
            data_int_copy[m] = data_int[m] * np.cos(-i * 2 * PI / 2**(k + 1)) - data_img[m] * np.sin(-i * 2 * PI / 2**(k + 1))
            data_img_copy[m] = data_img[m] * np.cos(-i * 2 * PI / 2**(k + 1)) + data_int[m] * np.sin(-i * 2 * PI / 2**(k + 1))
            m += 1

    ####バタフライ演算内足し算引き算
    j = 0
    for n in range(int(big_cycle)) :

        for i in range(small_cycle) :
            data_int[j] = data_int_copy[j] + data_int_copy[j + small_cycle]
            data_img[j] = data_img_copy[j] + data_img_copy[j + small_cycle]
            j += 1
        for i in range(small_cycle) :
            data_int[j] = data_int_copy[j - small_cycle] - data_int_copy[j]
            data_img[j] = data_img_copy[j - small_cycle] - data_img_copy[j]
            j += 1

for (inte, img) in zip(data_int, data_img):
    print ('{0} + {1} i' .format(inte, img))