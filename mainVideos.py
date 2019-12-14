class DoughFactory(object):
    def get_dough(self):
        return "insecticide treated wheat dough"

class Pizza(DoughFactory):
    def order_pizza(self, *toppings):
        print("Getting dough")
        dough = super().get_dough()
        print("Making pie with %s" % dough)
        for topping in toppings:
            print("Adding: %s" % topping)

class OrganicDoughFactory(DoughFactory):
    def get_dough(self):
        return "pure untreated wheat dough"

class OrganicPizza(Pizza, OrganicDoughFactory):
    pass

#Pizza().order_pizza("Pepperoni", "Bell Pepper")
print("")
#OrganicPizza().order_pizza("Sausage", "Mushroom") #prints "Making pie with pure untreated wheat dough" though inherits from 'Pizza' which inherits from 'DoughFactory'
# which should print "insecticide treated wheat dough" because of "super()" call in Pizza. Why is that?
# It's because inherited call to overridden method "get_dough"

'''
  Inheritance "diamond" diagram

      DoughFactory
    /            \
  Pizza           OrganicDoughFactory
    \            /
     OrganicPizza

'''

'''
  Another inheritance "diamond" diagram

  Poet           Writer
    \            /
     Multitalented

'''

class Poet:
    def __init__(self):
        pass
    def write(self):
        print("Write poems")

class Writer:
    def __init__(self):
        pass
    def write(self):
        print("Write stories")

class Multitalented(Poet, Writer):
    pass

multitalented = Multitalented()
multitalented.write() # writes whatever parameter in inheritance is first