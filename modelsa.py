# Bicycle Manufacturers
class Manufacturer(object):
	"""Makes different bike models and sells them at a mark-up"""
	def __init__(self, name, mark_up_percent):
		self.name = name
		self.mark_up_percent = mark_up_percent
	def mark_up_cost(self, mark_up_percent, model):
		print "I'm doing a manu markup"
		price = model.cost()
		price *= mark_up_percent
		print "It's gonna cost you %s" % (price)
		return price


# Bicycle Models
class BikeModels(object):
	"""Compiles wheels and frame to make a complete bike object with a weight and cost of each part"""
	def __init__(self, name, manufacturer, wheel_type, frame):
		self.name = name
		self.manufacturer = manufacturer
		self.wheel1 = wheel_type
		self.wheel2 = wheel_type
		self.frame = frame
	def weight(self):
		"""Calculate total weight of the bike"""
		return self.wheel1.weight + self.wheel2.weight + self.frame.weight
	def cost(self):
		"""calculate total cost of building the bike"""
		return self.wheel1.cost + self.wheel2.cost + self.frame.cost

# Frames
class Frames(object):
	"""Creates frame objects to become part of a bike"""
	def __init__(self, name, weight, cost):
		self.name = name
		self.weight = weight
		self.cost = cost

# Wheels
class Wheels(object):
	"""Creates Wheel objects to become part of a bike"""
	def __init__(self, name, weight, cost):
		self.name = name
		self.weight = weight
		self.cost = cost

# Bike Shops
class BikeShop(object):
	def __init__(self, name, margin, inventory, profits):
		self.name = name
		self.margin = margin
		self.inventory = inventory
		self.profits = profits

	def profit(self):
		"""Calculate the profit the shop makes on a sale"""
		profits = margin*number_sold

	def sell_bike(self, model, price, customer, inventory, bikeshop):
		"""Sell a bike and remove it from bikeshop inventory"""
		if model in self.inventory:
			print "Good news, we've got it. %s sold." % (model.name)
			print "Customer %s purchased bike %s and has %s dollars left over" % (customer.name, model.name, customer.budget)
			print "Store %s now has a profit of %s" % (bikeshop.name, bikeshop.profits)
			inventory.remove(model)
####### this line works when it's just inventory.remove(i).. but not with "return self.lalal".. why?
		else:
			print " Unfortunately, %s is unavailable." % (model)


# Customers
class Customer(object):
	"""Customers have a budget and go to the bike store to buy bikes"""
	def __init__(self, name, budget):
		self.name = name
		self.budget = budget






