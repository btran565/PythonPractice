def area_sum(rectangles):
    sum = 0
    for i in range(0, len(rectangles)):
        area = rectangles[i]["height"] * rectangles[i]["width"]
        sum += area
    return sum
