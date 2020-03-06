#! python3

import math

def recipe_batches(recipe, ingredients):
  # Initialize batches amount and list of keys for recipe ingredients
  batches = 0
  ingredients_keys = list(recipe.keys())

  # Iterate through ingredients in both dictionaries
  for i in range( len(ingredients_keys) ):
    rec_quantity = recipe.get( ingredients_keys[i] )
    ing_quantity = ingredients.get( ingredients_keys[i] )

    # If an ingredient is missing, make it 0
    if ing_quantity == None:
      ing_quantity = 0
    
    # Check if there are more of an ingredient than what the recipe requires
    # If so, divide the ingredient quantity by recipe quantity to find 
    # possible amount of batches for given ingredient
    if rec_quantity <= ing_quantity:
      amount = ing_quantity // rec_quantity
      # Set possible amount of batches for first pass
      if i == 0:
        batches = amount
      # If the amount is smaller than previous ingredient set possible batches to lower possibility
      elif amount < batches:
        batches = amount
    else:
      batches = 0
  
  return batches

        

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 50, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))