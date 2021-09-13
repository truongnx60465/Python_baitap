import math
import collections

print("Function - Chỉ số thống kê mô tả")
print("Cho list có sẵn : A = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]")
A = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10,1,1,1]
check_lengthA = len(A)
int_number = 0
mode_A = 0
max = 0
int_number_Check = int(check_lengthA/2)
print("Độ dài list A: ",check_lengthA)
int_average_A = sum(A)/len(A)
print("Trung bình list A mean: ",round(int_average_A,3))
# Số điểm xuất hiện nhiều nhất
max = 0
res = A[0]
for i in A:
    freq = A.count(i)
    if freq > max:
        max = freq
        res = i
print ("Trong lớp A, học viên đạt Điểm số nhiều nhất là điểm: "+ str(res))

if check_lengthA % 2 == 0 :
    median = (A[int_number_Check-1]+A[int_number_Check])/2
    print("Dãy số A là chẵn")
    print("Median A là : ",median)

else :
    int_number = math.ceil(check_lengthA/2)
    print("Dãy số A là lẻ")
    median = math.ceil(check_lengthA/2)
    print("Median A là : ",A[median-1])
    for i in range(check_lengthA):
        pass