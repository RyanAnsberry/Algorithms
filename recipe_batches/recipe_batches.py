#! python3

import math

def recipe_batches(recipe, ingredients):
  # Create a list of all dict keys for recipe
  recipe_list = list(recipe.keys())

  # Iterate through list of recipe ingredients
  # for each key, divide ingredients value by recipe value
  # Batches = dividen




if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))