def calculate_experience_points(level):
    xp_temp = 0
    xp_total = 0
    for i in range(1, level+1):
        xp_temp = (i-1) * 5
        xp_total += xp_temp
    return xp_total

