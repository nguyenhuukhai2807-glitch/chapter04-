def diem_trung_binh(ds_sinh_vien):
    tong = sum(ds_sinh_vien.values())
    so_sv = len(ds_sinh_vien)
    return tong / so_sv


# Ví dụ
sinh_vien = {
    "An": 8,
    "Bình": 7,
    "Chi": 9
}

print("Điểm trung bình:", diem_trung_binh(sinh_vien))