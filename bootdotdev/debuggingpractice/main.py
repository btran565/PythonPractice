def take_magic_damage(health, resist, amp, spell_power):
    damage = spell_power * amp
    total_damage = damage - resist
    player_health = health - total_damage
    return player_health
