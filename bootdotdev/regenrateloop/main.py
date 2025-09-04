def regenerate(current_health, max_health, enemy_distance):
    while current_health < max_health and enemy_distance > 3:   #dont quite understand 'and' vs '&' for conditional
        current_health += 1
        enemy_distance -= 2
    
    return current_health
