def levenshtein_distance(s1, s2):
    """
    Tính khoảng cách Levenshtein giữa hai chuỗi.

    Args:
        s1: Chuỗi thứ nhất.
        s2: Chuỗi thứ hai.

    Returns:
        Khoảng cách Levenshtein giữa hai chuỗi.
    """

    m = len(s1)
    n = len(s2)

    # Khởi tạo ma trận DP
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Khởi tạo giá trị cho hàng và cột đầu tiên
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Điền vào ma trận DP
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                cost = 0
            else:
                cost = 1

            dp[i][j] = min(
                dp[i - 1][j] + 1,  # Xóa ký tự
                dp[i][j - 1] + 1,  # Thêm ký tự
                dp[i - 1][j - 1] + cost  # Thay thế ký tự
            )

    return dp[m][n]

# Nhập hai chuỗi từ bàn phím
s1 = input("Nhập chuỗi thứ nhất: ")
s2 = input("Nhập chuỗi thứ hai: ")

# Tính khoảng cách Levenshtein
distance = levenshtein_distance(s1, s2)

# In kết quả
print(f"Khoảng cách Levenshtein giữa '{s1}' và '{s2}' là {distance}")