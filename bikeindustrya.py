
from modelsa import *

wheel_light = Wheels("Wheel Light", 50, 10)
wheel_medium = Wheels("Wheel Medium", 100, 20)
wheel_heavy = Wheels("Wheel Heavy", 150, 25)

frame_aluminum = Frames("Frame Aluminum", 100, 50)
frame_carbon = Frames("Frame Carbon", 50, 100)
frame_steel = Frames("Frame Steel", 125, 150)

lightweightbikes = Manufacturer("Light Weight Bikes", 1.25)
heavydutybikes = Manufacturer("Heavy Duty Bikes", 1.25)

modela = BikeModels("Model A", lightweightbikes, wheel_light, frame_aluminum)
modelb = BikeModels("Model B", lightweightbikes, wheel_light, frame_carbon)
modelc = BikeModels("Model C", lightweightbikes, wheel_medium, frame_carbon)
modeld = BikeModels("Model D", heavydutybikes, wheel_medium, frame_aluminum)
modele = BikeModels("Model E", heavydutybikes, wheel_heavy, frame_aluminum)
modelf = BikeModels("Model F", heavydutybikes, wheel_heavy, frame_steel)

bobs_bikes = BikeShop("Bob's Bikes", 1.3, [modela, modelb, modelc, modeld, modele, modelf], 0)

paul = Customer("Paul", 200, [])
melanie = Customer("Melanie", 500, [])
rick = Customer("Rick", 1000, [])

inventory = [modela, modelb, modelc, modeld, modele, modelf]

def describe_inventory(inventory, bikeshop):
	"""Print out the current inventory, including weight and cost"""
	for i in inventory:
		shop_price = bikeshop.shop_price(i.manufacturer, bikeshop.mark_up_percent, i)
		print "Bob's bikes sells the %s which weighs %s pounds for %.2f dollars." % (i.name,i.weight(), shop_price)#*bobs_bikes.margin)

def customers_options(inventory, customer, bikeshop):
	"""Print out a customer's options given their budget"""
	print "Let's see what %s can buy with %s dollars in their pocket" % (customer.name, customer.budget)
	customer_model_options = []
	for i in inventory:
		if customer.budget >= bikeshop.shop_price(i.manufacturer, bikeshop.mark_up_percent, i):
			customer_model_options.append(i)
	print "Customer %s can buy the following bikes:" % (customer.name)
	describe_inventory(customer_model_options, bikeshop)
	


def purchase_bike(model, customer, inventory, bikeshop):
	"""Purchase the bike for a given customer"""
	shop_cost = model.manufacturer.manu_price(model.manufacturer.mark_up_percent, model)
	shop_price = bikeshop.shop_price(model.manufacturer, bikeshop.mark_up_percent, model)
	print "Alright, %s would like to buy %s for %.2f." % (customer.name, model.name, shop_price)
	if model in inventory and shop_price <= customer.budget:
		customer.budget -= shop_price
		bikeshop.profits += shop_price - shop_cost
		bobs_bikes.sell_bike(model, shop_price, customer, inventory, bobs_bikes)
		customer.bikes.append(model)
		print "The following models are left in stock: "
		describe_inventory(inventory, bikeshop)
	else:
		print model.cost()
		print "Nope, %s can't buy that guy" % (customer.name)

# Currently not using this method, but could be fun if I expanded this project.
def choose():
	"""Option for end-user to pick who they want to be shopping as"""
	choice = raw_input("Who would you like to be? Paul, Melanie, or Rick? ")
	if choice == "Paul":
		purchase_bike(modela, paul, inventory, bobs_bikes)
	elif choice == "Melanie":
		purchase_bike(modela, melanie, inventory, bobs_bikes)
	elif choice == "Rick":
		purchase_bike(modela, rick, inventory, bobs_bikes)
	else:
		print "Hmm. That person isn't here today, pick again!" 
		choose()


## Begin printing of script 
print ""
print "Let's go Bike Shopping"
print "We're walking into %s store now." % (bobs_bikes.name)
print "Lots of bikes are around, namely: "
describe_inventory(inventory, bobs_bikes)
print ""
print "Alrighty then, Melanie is up first!" 
customers_options(inventory, melanie, bobs_bikes)
purchase_bike(modela, melanie, inventory, bobs_bikes)
print ""
print "Cool. Rick is up second."
customers_options(inventory, rick, bobs_bikes)
purchase_bike(modele, rick, inventory, bobs_bikes)
print ""
print "Nice nice. Paul is last!"
customers_options(inventory, paul, bobs_bikes)
purchase_bike(modeld, paul, inventory, bobs_bikes)

print ""
print ""
print "It was a good day."
print "%s made %s in profits" % (bobs_bikes.name, bobs_bikes.profits)
print "%s bought %s" % (melanie.name, melanie.bikes[0].name)
print "%s bought %s" % (rick.name, rick.bikes[0].name)
print "%s bought %s" % (paul.name, paul.bikes[0].name)

## Test Code
#add_manu_markup(inventory, heavydutybikes)
#describe_inventory(inventory)
#mark_up_cost(heavydutybikes, 2, modela)
# choose()
#customers_options(inventory, melanie)
#customers_options(inventory, paul)
#customers_options(inventory, rick)
#purchase_bike(modela, melanie, inventory, bobs_bikes)
#purchase_bike(modelb, paul, inventory, bobs_bikes)


print "lalala the script is done"








