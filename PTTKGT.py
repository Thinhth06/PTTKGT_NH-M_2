import math

INF = 10**9

# =========================
# Ví dụ dữ liệu
# =========================

n = 4  # số điểm (0 là kho)

points = [
    (0, 0),  # kho
    (1, 2),
    (4, 0),
    (2, 3)
]

# =========================
# Tính ma trận khoảng cách
# =========================

dist = [[0.0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        x1, y1 = points[i]
        x2, y2 = points[j]

        dist[i][j] = math.sqrt(
            (x1 - x2)**2 +
            (y1 - y2)**2
        )

# =========================
# Khởi tạo DP
# =========================

dp = [[INF]*n for _ in range(1 << n)]

# bắt đầu tại điểm 0
dp[1][0] = 0

# =========================
# DUYỆT MASK + CẬP NHẬT DP
# =========================

for mask in range(1 << n):

    # duyệt điểm hiện tại
    for u in range(n):

        # nếu u chưa thuộc mask → bỏ qua
        if not (mask & (1 << u)):
            continue

        # thử đi đến điểm v
        for v in range(n):

            # nếu v đã đi rồi → bỏ qua
            if mask & (1 << v):
                continue

            # tạo mask mới
            new_mask = mask | (1 << v)

            # CẬP NHẬT DP
            dp[new_mask][v] = min(
                dp[new_mask][v],
                dp[mask][u] + dist[u][v]
            )

# =========================
# TÍNH KẾT QUẢ CUỐI
# =========================

full_mask = (1 << n) - 1

answer = INF

for u in range(n):

    if u == 0:
        continue

    answer = min(
        answer,
        dp[full_mask][u] + dist[u][0]
    )

print("Chi phí nhỏ nhất:", answer)