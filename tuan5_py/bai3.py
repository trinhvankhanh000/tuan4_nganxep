import re

def dem_tu_trong_file(duong_dan_file):
    """
    Đọc file txt, đếm số lượng từ xuất hiện và trả về dictionary.

    Args:
        duong_dan_file: Đường dẫn đến file txt.

    Returns:
        Dictionary với key là từ và value là số lần xuất hiện của từ đó.
    """

    dem_tu_dict = {}
    try:
        with open(duong_dan_file, 'r', encoding='utf-8') as file:  # Xử lý encoding nếu cần
            for dong in file:
                # Loại bỏ ký tự không phải chữ và số, chuyển thành chữ thường
                dong = re.sub(r'[^a-zA-Z0-9\s]', '', dong).lower()  
                cac_tu = dong.split()  # Tách dòng thành các từ
                for tu in cac_tu:
                    dem_tu_dict[tu] = dem_tu_dict.get(tu, 0) + 1
    except FileNotFoundError:
        return "Không tìm thấy file."  # Hoặc xử lý lỗi tùy ý
    return dem_tu_dict

# Nhập đường dẫn file từ bàn phím
duong_dan_file = input("Nhập đường dẫn đến file txt: ")

ket_qua = dem_tu_trong_file(duong_dan_file)
print(ket_qua)