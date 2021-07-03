import numpy as np

point_num = 8
data = [0] * point_num

##データの並び替えを行う（偶数と奇数に分ける）

data_order = [0] * point_num
stage = int(np.log2(point_num))
for k in range(stage) :
    
    m = 0
    for n in range(int(point_num/ 2**(k + 1))) :
        for i in range(2**k) :
            m += 1
        
        for i in range(2**k) :
            data_order[m] = data_order[m] + int(point_num / 2**(k + 1))
            m += 1


for k in range(point_num): #作った順番にデータを並び替え
    data[k] = data[data_order[k]]
