import re

def count_chars_from_input():
    """
    Nhận chuỗi từ người dùng, đếm số lần xuất hiện của từng ký tự và trả về dictionary.
    """
    input_string = input("Nhập vào một chuỗi: ")
    char_counts = {}
    for char in input_string:
        char = char.lower()  # Xử lý hoa thường
        if 'a' <= char <= 'z':  # Chỉ xét chữ cái
            char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

result = count_chars_from_input()
print(result)