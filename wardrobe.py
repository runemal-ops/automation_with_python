wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for elements in wardrobe:
	for color in wardrobe[elements]:
		print("{} {}".format(color, elements))