"""Dessert classes."""


class Cupcake:
    """A cupcake."""

    cache = {}

    def __init__(self, name, flavor, price):
      self.name = name
      self.flavor = flavor
      self.price = price
      self.qty = 0
      Cupcake.cache[self.name] = self


    def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<Cupcake name="{self.name}" qty={self.qty}>'


    def add_stock(self, amount):

      self.qty += int(amount)


    def sell(self, amount):

      if self.qty == 0:
        print('Sorry, these cupcakes are sold out')
        return

      if self.qty >= amount:
        self.qty -= amount
      else:
        self.qty = 0


    @staticmethod
    def scale_recipe(ingredients, amount):

      new_ingredients = []
      for ingredient in ingredients:
        new_ingredients.append((ingredient[0], ingredient[1]*amount))
      return new_ingredients


    @classmethod
    def get(cls, name):
      for cupcake_name in cls.cache:
        if cupcake_name == name:
          return cls.cache[cupcake_name]

      print("Sorry, that cupcake doesn't exist")


class Brownie(Cupcake):

  def __init__(self, name, price):
    super().__init__(name, 'chocolate', price)


  def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<Brownie name="{self.name}" qty={self.qty}>'



if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
