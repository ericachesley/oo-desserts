"""
Tests for desserts.py
=====================

  >>> from desserts import Cupcake

Class Attributes
----------------

`Cupcake` has a class attribute called `cache`:

  >>> Cupcake.cache
  {}

Instance Methods
----------------

Can initialize a `Cupcake` with name, flavor, price:

  >>> c = Cupcake('Strawberry Fields', 'strawberry', 5.0)
  >>> c.name
  'Strawberry Fields'
  >>> c.flavor
  'strawberry'
  >>> c.price
  5.0

Quantity starts at 0:

  >>> c.qty
  0

Cupcake is added to `Cupcake.cache`:

  >>> Cupcake.cache
  {'Strawberry Fields': <Cupcake name="Strawberry Fields" qty=0>}

Can add more cupcakes:

  >>> c.add_stock(10)
  >>> c.qty
  10

Can sell cupcakes:

  >>> c.sell(1)
  >>> c.qty
  9

`self.qty` never goes below 0:

  >>> c.sell(11)
  >>> c.qty
  0

Print apology if sold out:

  >>> c.sell(1)
  Sorry, these cupcakes are sold out

Static Methods
--------------

Scale a recipe:

  >>> Cupcake.scale_recipe([('flour', 1), ('sugar', 3)], 10)
  [('flour', 10), ('sugar', 30)]

Method can be called on the instance too:

  >>> c.scale_recipe([('flour', 1), ('sugar', 3)], 10)
  [('flour', 10), ('sugar', 30)]

Class Methods
-------------

Return a cupcake by its name:

  >>> Cupcake.get('Strawberry Fields')
  <Cupcake name="Strawberry Fields" qty=0>

Or print if it doesn't exist:

  >>> Cupcake.get('Devil\'s Food Cake')
  Sorry, that cupcake doesn't exist


Tests for desserts.py -- brownie
=====================

  >>> from desserts import Brownie

Class Attributes
----------------

`Cupcake` has a class attribute called `cache`:

  >>> Cupcake.cache
  {'Strawberry Fields': <Cupcake name="Strawberry Fields" qty=0>}

Instance Methods
----------------

Can initialize a `Brownie` with name, price:

  >>> b = Brownie('Chocolate Goodness', 3.0)
  >>> b.name
  'Chocolate Goodness'
  >>> b.flavor
  'chocolate'
  >>> b.price
  3.0

Quantity starts at 0:

  >>> b.qty
  0

Cupcake is added to `Cupcake.cache`:

  >>> Cupcake.cache
  {'Strawberry Fields': <Cupcake name="Strawberry Fields" qty=0>, 'Chocolate Goodness': <Brownie name="Chocolate Goodness" qty=0>}

Can add more cupcakes:

  >>> b.add_stock(12)
  >>> b.qty
  12

Can sell cupcakes:

  >>> b.sell(4)
  >>> b.qty
  8

`self.qty` never goes below 0:

  >>> b.sell(11)
  >>> b.qty
  0

Print apology if sold out:

  >>> b.sell(3)
  Sorry, these cupcakes are sold out

Static Methods
--------------

Scale a recipe:

  >>> Brownie.scale_recipe([('flour', 1), ('sugar', 3)], 10)
  [('flour', 10), ('sugar', 30)]

Method can be called on the instance too:

  >>> b.scale_recipe([('flour', 1), ('sugar', 3)], 10)
  [('flour', 10), ('sugar', 30)]

Class Methods
-------------

Return a cupcake by its name:

  >>> Brownie.get("Chocolate Goodness")
  <Brownie name="Chocolate Goodness" qty=0>

Or print if it doesn't exist:

  >>> Brownie.get('Devil\'s Food Cake')
  Sorry, that cupcake doesn't exist
