import sys
import io

INF = sys.maxsize   # Giá trị vô cùng lớn

def init_data():
    """
    MIỀN: Khởi tạo dữ liệu cho Bitmask DP (Case Study 2)
    Mục đích: Đọc input → xây dựng ma trận dist → khởi tạo bảng dp
    """
    n = int(input().strip())                    # Số địa điểm (n <= 20)
    
    # Đọc ma trận khoảng cách dist[n][n]
    dist = []
    for _ in range(n):
        row = list(map(int, input().strip().split()))
        dist.append(row)
    
    # Tạo bảng DP: dp[1<<n][n]
    dp = [[INF] * n for _ in range(1 << n)]
    
    # Khởi tạo trạng thái ban đầu
    dp[1 << 0][0] = 0
    
    return n, dist, dp


# ======================== TEST NHANH (có thể xóa sau) ========================
if __name__ == "__main__":
    # Test nhanh với dữ liệu cứng (không cần file input.txt)
    test_input = """4
0 10 15 20
10 0 35 25
15 35 0 30
20 25 30 0
"""
    # Chuyển test_input thành stdin
    sys.stdin = io.StringIO(test_input)
    
    n, dist, dp = init_data()
    
    print("✅ Khởi tạo thành công!")
    print(f"n = {n}")
    print(f"dist[0][1] = {dist[0][1]}  # phải ra 10")
    print(f"dp[1][0] = {dp[1][0]}      # phải ra 0")