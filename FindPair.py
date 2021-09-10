print("Find Pair")
print("Cho list có sẵn : A = [3, 6, 7, 9, 11, 12]")
int_number1 = input("Nhập vào số nguyên sum: ")
listA = [3, 6, 7, 9, 11, 12]
listB = []
int_Lenth = len(listA)
int_count = 0
int_f = 0
for i in range(int_Lenth):
    for c in range(i+1,int_Lenth):
        if listA[i]+listA[c] == int(int_number1):
            listB.insert(int_f,(listA[i],listA[c]))
            int_f += 1
        else:
            listB = []
print(listB)