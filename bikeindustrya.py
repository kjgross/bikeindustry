
from models import *

wheel_light = Wheels("Wheel Light", 50, 10)
wheel_medium = Wheels("Wheel Medium", 100, 20)
wheel_heavy = Wheels("Wheel Heavy", 150, 30)

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

bobs_bikes = BikeShop("Bob's Bikes", 1.20, [modela, modelb, modelc, modeld, modele, modelf], 0)

paul = Customer("Paul", 200)
melanie = Customer("Melanie", 500)
rick = Customer("Rick", 1000)

inventory = [modela, modelb, modelc, modeld, modele, modelf]

def describe_inventory(inventory):
	"""Print out the current inventory, including weight and cost"""
	for i in inventory:
		#bobs_bikes.margin_calc(i, bobs_bikes.margin)
		print "Bob's bikes sells the %s which weighs %s pounds for %s dollars." % (i.name,i.weight(), i.cost())#*bobs_bikes.margin)

def customers_options(inventory, customer):
	"""Print out a customer's options given their budget"""
	print "Let's see what %s can buy with %s dollars in their pocket" % (customer.name, customer.budget)
	customer_model_options = []
	for i in inventory:
		if customer.budget >= i.cost()*bobs_bikes.margin:
			customer_model_options.append(i)
		else:
			continue
	print "Customer %s can buy the following bikes:" % (customer.name)
	describe_inventory(customer_model_options)
	


def purchase_bike(model, customer, inventory, bikeshop):
	"""Purchase the bike for a given customer"""
	print "Alright, %s would like to buy %s." % (customer.name, model.name)
	if model in inventory and model.cost() <= customer.budget:
		customer.budget -= model.cost()
		bikeshop.profits += model.cost()
		bobs_bikes.sell_bike(model, model.cost(), customer, inventory, bobs_bikes)
		print "The following models are left in stock: "
		describe_inventory(inventory)
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

def manumarks(manufacturer, mark_up_percent, model):
	manufacturer.mark_up_cost(mark_up_percent, model)
	print "OK!"


## Begin printing of script 

print "Let's go Bike Shopping"
print "We're walking into %s store now." % (bobs_bikes.name)
print "Lot's of bikes are around, namely: "
describe_inventory(inventory)
print "Alrighty then, Melanie is up first!"
customers_options(inventory, melanie)
purchase_bike(modela, melanie, inventory, bobs_bikes)
print "Cool. Rick is up second."
customers_options(inventory, rick)
purchase_bike(modele, rick, inventory, bobs_bikes)
print "Nice nice. Paul is last!"
customers_options(inventory, paul)
purchase_bike(modelc, paul, inventory, bobs_bikes)


print "dooone"
manumarks(heavydutybikes, 2, modeld)

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


## To Do:

# Handle cost so that both manufacturer's and shop's mark ups are included
	## The bicycle shop should charge its customers 20% over its cost for buying the bikes 
	## from the manufacturers.






