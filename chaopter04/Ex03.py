def kiem_tra_key(dic, key):
    if key in dic:
        print("Key tồn tại trong dictionary")
    else:
        print("Key không tồn tại")


# Ví dụ
data = {"a": 1, "b": 2, "c": 3}

kiem_tra_key(data, "b")
kiem_tra_key(data, "d")