# Bicycle Manufacturers

# Have a name
# Produce three models of bikes each
# Have a percentage over cost they sell bikes to bike shops at
# You'll need to create two bicycle manufacturers

class Manufacturer(object):
	"""Makes different bike models and sells them at a mark-up"""
	def __init__(self, name, mark_up_percent):
		self.name = name
		self.mark_up_percent = mark_up_percent



# Bicycle Models

# Comprised (in our simplified world) of two wheels of the same type and a frame.
# Have a total weight equal to the sum of the weight of the frame and two wheels.
# Have a total cost to produce (for our purposes, that cost is the sum of the two wheels' and frame's cost to produce)
# Have a name
# Have a manufactuer

class BikeModels(object):
	"""Compiles wheels and frame to make a complete bike object"""
	def __init__(self, name, manufacturer, wheel_type, frame):
		self.name = name
		self.manufacturer = manufacturer
		self.wheel1 = wheel_type
		self.wheel2 = wheel_type
		self.frame = frame
	def weight(self):
		"""Calculate total weight of the bike"""
		self.weight = self.wheel1.weight + self.wheel2.weight + self.frame.weight
	def cost(self):
		"""calculate total cost of building the bike"""
		#print self.wheel1.cost 
		#print "wheel cost ^^"
		#print self.frame.cost 
		#print "frame cost ^^"
		self.cost = self.wheel1.cost + self.wheel2.cost + self.frame.cost
		#print self.cost 
		#print "total cost ^^"

## Why does weight work but cost doesn't? They are identical functions ##

# Frames

# Can be made of aluminunum, carbon, or steel
# Have a weight
# Have a cost for manufacturer to produce
# Even though you'll create two bicycle manufacturers, assume that all manufacturers use the same three frame types.

class Frames(object):
	"""Creates frame objects to become part of a bike"""
	def __init__(self, name, weight, cost):
		self.name = name
		self.weight = weight
		self.cost = cost


# Wheels

# Have a weight
# Have a cost for manufacturer to produce
# Have a model name
# You'll need to create a total of three wheel types
# Even though you'll create two bicycle manufacturers, assume that all manufacturers use the same three wheel types.

class Wheels(object):
	"""Creates Wheel objects to become part of a bike"""
	def __init__(self, name, weight, cost):
		self.name = name
		self.weight = weight
		self.cost = cost



# Bike Shops

# Get their inventory of bikes from manufacturers
# Sell bicycle models with a margin over price they pay to manufacturer
# Have a name
# Have an inventory
# Can see how much profit they have made on margin from selling bikes.

class BikeShop(object):
	def __init__(self, name, margin, inventory):
		self.name = name
		self.margin = margin
		self.inventory = inventory
	def profit(self):
		"""Calculate the profit the shop makes on a sale"""
		profit = margin*number_sold

	def sell_bike(self, model, price):
		"""Sell a bike and remove it from bikeshop inventory"""
		if model in self.inventory:
			del self.invetory[model]
			print model + " sold."
			print "Customer %s purchased bike %s and has %s left over" % (customer.name, model.name, leftoverbudget)
		else:
			print model + "is unavailable."


# Customers

# Have a name
# Have a fund of money to buy a bike
# Can buy and own a new bicycle

class Customer(object):
	"""Customers have a budget and go to the bike store to buy bikes"""
	def __init__(self, name, budget, can_buy):
		self.name = name
		self.budget = budget
		self.can_buy = can_buy






