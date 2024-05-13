country_list = ['canada', 'mexico', 'england', 'china']
print(country_list)

for country in country_list[:2]:
	print(country)

travel_list = country_list[:]	#copies country list to the new travel list
print(travel_list)

country_list.append('japan')
travel_list.append('russia')

print(country_list)
print(travel_list)
