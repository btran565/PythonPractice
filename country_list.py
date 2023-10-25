country_list = ['canada', 'mexico', 'england', 'china']
print(country_list)

last_visited = country_list.pop()
print(f"For my recent vacation, I visited " + last_visited.title() + "\n")

country_list.append('usa')
country_list.append('austrailia')

cancelled = country_list.pop(-2)
print(f"I changed my mind and won't be visiting the {cancelled.upper()}")

print(country_list)