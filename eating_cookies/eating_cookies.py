#! python3

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  # base case
  if n == 0:
    if cache != None:
      cache[n] = 1
    return 1

  # Check cache
  if cache != None and cache[n] != 0:
    return cache[n]
  
  # Initialize total ways counter
  total_ways = 0

  # 3 cookies at once
  if n >= 3:
    total_ways += eating_cookies(n-3, cache)
  # 2 cookies at once
  if n >= 2:
    total_ways += eating_cookies(n-2, cache)
  # 1 cookie at a time
  if n >= 1:
    total_ways += eating_cookies(n-1, cache)

  # Cache total ways at n
  if cache != None:
    cache[n] = total_ways

  return total_ways


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')