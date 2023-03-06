from house import House

house_one = House("bungalow", "white", "sheila","1", "curved")
house_two = House("flat", "blue", "wendy","1", "triangularbase")
house_three = House("masionnette", "red", "wafula","1", "flatbase")

print(house_one.owner, house_one.roof, house_one.kitchen)
print(house_two.owner, house_two.make, house_two.color)
print(house_three.owner,house_three.color, house_three.roof)