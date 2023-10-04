def calculate_triangle_area(x1, y1, x2, y2, x3, y3):
    return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

num_triangles = int(input())

triangle_areas = []

for _ in range(num_triangles):
    x1, y1, x2, y2, x3, y3 = map(float, input().split())
    area = calculate_triangle_area(x1, y1, x2, y2, x3, y3)
    triangle_areas.append(area)

print(' '.join(map(str, triangle_areas)))
