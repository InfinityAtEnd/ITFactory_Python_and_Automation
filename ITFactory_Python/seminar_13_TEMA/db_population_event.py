from db_initialization import *

# this file only has been run ONCE !!!
# add products
p1 = Products(name="Banane", price=2, quantity=300)
p2 = Products(name="Mere", price=3, quantity=300)
p3 = Products(name="Pere", price=4, quantity=300)
p4 = Products(name="Cirese", price=6, quantity=300)
p5 = Products(name="kiwi", price=12, quantity=300)
session.add(p1)
session.add(p2)
session.add(p3)
session.add(p4)
session.add(p5)

session.commit()