print("Sorting - Sắp xếp điểm thi")
print("Cho tuple có sẵn : sort_list_last([(1, 2, 5), (9, 1, 2), (6, 4, 4), (3, 2, 3), (10, 2, 1)])")
tuple_1 = tuple([(1, 2, 5), (9, 1, 2), (6, 4, 4), (3, 2, 3), (10, 2, 1)])
print("Sắp xếp theo điểm cuối kỳ - endterm tăng dần: ",sorted(tuple_1, key=lambda x:x[2]))