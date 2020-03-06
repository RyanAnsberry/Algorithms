#! python3

import argparse

def find_max_profit(prices):
  # Ensure list contains at least 2 stock prices to compute
  if len(prices) < 2:
    return -1
  
  # Initialize min_price_so_far and max_profit_so_far and index for the max profit

  min_price_so_far = prices[0]
  max_profit_so_far = 0
  max_profit_index = 0

  # Find max profit
  # Start with 2nd element to allow for at least one buy option
  for i in range(1, len(prices)-1 ):
    if prices[i] > max_profit_so_far:
      max_profit_so_far = prices[i]
      max_profit_index = i

  # Find min_price_so_far that exist Before max_profit_so_far in given list
  for i in range( 0, max_profit_index ):
    if prices[i] < min_price_so_far:
      min_price_so_far = prices[i]

  # Calculate difference between max_profit_so_far - min_price_so_far
  max_profit = max_profit_so_far - min_price_so_far

  # Return difference as max_profit
  return max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))