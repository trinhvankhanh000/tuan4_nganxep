from collections import deque

def sliding_window_max(nums, k):
    if not nums or k == 0:
        return []

    result = []  # Danh sách lưu kết quả
    dq = deque()  # Deque để lưu chỉ số của phần tử trong cửa sổ trượt

    for i in range(len(nums)):
        # Loại bỏ phần tử không còn trong cửa sổ k phần tử
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        # Loại bỏ các phần tử nhỏ hơn nums[i] từ cuối deque
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)  # Thêm chỉ số hiện tại vào deque

        # Bắt đầu ghi nhận giá trị lớn nhất sau khi đủ k phần tử
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

# Dữ liệu đầu vào
num_list = [2, 4, 6, 1, -14, 12, 17, 15, 32, 3]
k = 2

# Gọi hàm và in kết quả
output = sliding_window_max(num_list, k)
print("Output:", output)
