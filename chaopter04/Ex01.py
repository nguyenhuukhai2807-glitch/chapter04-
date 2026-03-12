def tinh_toan_tuple(t):
    tong = sum(t)
    lon_nhat = max(t)
    nho_nhat = min(t)

    return tong, lon_nhat, nho_nhat


# Ví dụ
numbers = (3, 7, 1, 9, 4)
tong, max_val, min_val = tinh_toan_tuple(numbers)

print("Tổng:", tong)
print("Lớn nhất:", max_val)
print("Nhỏ nhất:", min_val)