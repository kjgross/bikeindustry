#wheel Light, Medium, Heavy
#Frame Aluminum, Carbon, Steel
# Each Manufacturer produceses 3 models of bike

from models import *

wheel_light = Wheels("Wheel Light", 50, 100)
wheel_medium = Wheels("Wheel Medium", 100, 75)
wheel_heavy = Wheels("Wheel Heavy", 150, 25)

frame_aluminum = Frames("Frame Aluminum", 100, 300)
frame_carbon = Frames("Frame Carbon", 50, 400)
frame_steel = Frames("Frame Steel", 125, 150)

lightweightbikes = Manufacturer("Light Weight Bikes", 5)
heavydutybikes = Manufacturer("Heavy Duty Bikes", 7)

modela = BikeModels("Model A", lightweightbikes, wheel_light, frame_aluminum)
modelb = BikeModels("Model B", lightweightbikes, wheel_light, frame_carbon)
modelc = BikeModels("Model C", lightweightbikes, wheel_medium, frame_carbon)
modeld = BikeModels("Model D", heavydutybikes, wheel_medium, frame_aluminum)
modele = BikeModels("Model E", heavydutybikes, wheel_heavy, frame_aluminum)
modelf = BikeModels("Model F", heavydutybikes, wheel_heavy, frame_steel)

bobs_bikes = BikeShop("Bob's Bikes", 20, [modela, modelb, modelc, modeld, modele, modelf])

paul = Customer("Paul", 200, [])
melanie = Customer("Melanie", 500, [])
rick = Customer("Rick", 1000, [])

inventory = [modela, modelb, modelc, modeld, modele, modelf]


def describe_inventory(inventory):
	for i in inventory:
		print "Bob's bikes sells the %s which weighs %s" % (i.name,i.weight())
	print "that's all."

def customers_options(inventory, customer):
	for i in inventory:
		if customer.budget >= i.cost:
			print "Customer %s can purchase bike: %s" % (customer.name, i.model)
		else:
			continue

# 3 customers buy bikes:
#buy the bike

# print the remaining inventory .. then move on to the next customer

def purchase_bike(model, customer, inventory):
	if model in inventory and model.cost < customer.budget:
		leftoverbudget = customer.budget - model.cost
		BikeShop.sell_bike(model, model.cost)
		describe_inventory(inventory)
	else:
		print model.cost
		print "Nope, %s can't buy that guy" % (customer.name)


print "here we go kids"
#describe_inventory(inventory)
print "ok that's cool"

# print modela.name
# print modela.wheel1.name
# print modela.frame.name
# print modela.manufacturer.name
print modela.weight
print modela.cost()

print "lets buy somethin"
purchase_bike(modela, paul, inventory)
purchase_bike(modela, rick, inventory)
print "lalala"





