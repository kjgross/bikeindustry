# Bicycle Manufacturers
class Manufacturer(object):
	"""Makes different bike models and sells them at a mark-up"""
	def __init__(self, name, mark_up_percent):
		self.name = name
		self.mark_up_percent = mark_up_percent
	def manu_price(self, mark_up_percent, model):
		pricemanu = model.cost()
		pricemanu *= mark_up_percent
		#print "It's gonna cost the shop %s" % (pricemanu)
		return pricemanu


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
	def __init__(self, name, mark_up_percent, inventory, profits):
		self.name = name
		self.mark_up_percent = mark_up_percent
		self.inventory = inventory
		self.profits = profits


	def shop_price(self, manufacturer, mark_up_percent, model):
		"""Calculate the price after adding in shop's markup"""
		costshop = manufacturer.manu_price(manufacturer.mark_up_percent, model)
		priceshop = mark_up_percent*costshop
		#print "It's gonna cost you %s" % (priceshop)
		return priceshop

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
	def __init__(self, name, budget, bikes):
		self.name = name
		self.budget = budget
		self.bikes = bikes






