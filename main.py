from input_module import read_input
from distance_module import create_distance_matrix, print_distance_matrix
from cost import calculate_cost
from all_paths import tsp_bruteforce   # file của Kiên

def main():
    names = ["Kho",  "Quận 1", "Quận 3", "Quận 4", "Quận 5", "Quận 6",  "Quận 8", "Quận 10"]

    # -------------------------
    # MODULE INPUT
    # -------------------------
    nodes = read_input("data.txt")

    print("\n===== DANH SÁCH ĐỊA ĐIỂM =====")
    for node in nodes:
      print(f"{names[node.id]} | (toa do)=({node.x},{node.y}) | time=({node.earliest}-{node.latest}) | service={node.service_time}")

    # -------------------------
    # MODULE DISTANCE
    # -------------------------
    matrix = create_distance_matrix(nodes)

    print("\n===== MA TRẬN KHOẢNG CÁCH =====")
    print_distance_matrix(matrix)

    # -------------------------
    # CHẠY PHẦN KIÊN
    # -------------------------
    best_path, best_cost = tsp_bruteforce(nodes, matrix)

    print("\n=========================")
    print("KẾT QUẢ TỐI ƯU")
    route_str = " → ".join(names[i] for i in best_path)
    print("Path:", route_str)


    print("\n=========================")
    print("KIỂM TRA BẰNG COST ")

    # bỏ điểm đầu và cuối (0)
    path_for_cost = best_path[1:-1]

    cost = calculate_cost(path_for_cost, matrix)

    print("Cost (chỉ khoảng cách):", cost)


if __name__ == "__main__":
    main()
# sds

