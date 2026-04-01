import itertools

names = ["Kho", "Quận 1", "Quận 3", "Quận 4", "Quận 5", "Quận 6", "Quận 8", "Quận 10"]

def calculate_route(nodes, dist_matrix, path):
    time = 0
    total_distance = 0

    for i in range(len(path) - 1):
        current = nodes[path[i]]
        next_node = nodes[path[i+1]]

        travel_time = dist_matrix[current.id][next_node.id]
        time += travel_time

        if time < next_node.earliest:
            time = next_node.earliest

        # 👉 bật lại nếu cần đúng đề
        # if time > next_node.latest:
        #     return float('inf')

        time += next_node.service_time
        total_distance += travel_time

    return total_distance


def tsp_bruteforce(nodes, dist_matrix):
    n = len(nodes)
    all_nodes = list(range(n))

    start = 0
    other_nodes = all_nodes[1:]

    best_cost = float('inf')
    best_path = None

    all_routes = []   # ✅ lưu toàn bộ tuyến hợp lệ

    print("\n🔍 Một số tuyến đường:")

    max_print = 10
    count = 0

    for perm in itertools.permutations(other_nodes):
        path = [start] + list(perm) + [start]

        cost = calculate_route(nodes, dist_matrix, path)

        if cost != float('inf'):
            # ✅ lưu route
            all_routes.append((path, cost))

            # in demo
            if count < max_print:
                route_str = " → ".join(names[i] for i in path)
                print(f"Path: {route_str} | Cost: {cost:.2f}")
                count += 1

        # tìm best
        if cost < best_cost:
            best_cost = cost
            best_path = path

    # =========================
    # XỬ LÝ DANH SÁCH TUYẾN
    # =========================
    print("\n Tổng số tuyến hợp lệ:", len(all_routes))

    # sắp xếp theo cost tăng dần
    all_routes.sort(key=lambda x: x[1])

    print("\n Top 5 tuyến tốt nhất:")
    for i in range(min(5, len(all_routes))):
        path, cost = all_routes[i]
        route_str = " → ".join(names[j] for j in path)
        print(f"{i+1}. {route_str} | Cost: {cost:.2f}")

    return best_path, best_cost