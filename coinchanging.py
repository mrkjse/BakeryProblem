# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 13:41:20 2019

Author: David Wright
https://bitbucket.org/trebsirk/algorithms/src/master/coinchanging.py

"""

def change(n, coins_available, coins_so_far):
	if sum(coins_so_far) == n:
		yield coins_so_far
	elif sum(coins_so_far) > n:
		pass
	elif coins_available == []:
		pass
	else:
		for c in change(n, coins_available[:], coins_so_far+[coins_available[0]]):
			yield c
		for c in change(n, coins_available[1:], coins_so_far):
			yield c

if __name__ == '__main__':
	n = 15
	coins = [3, 5, 10, 25]

	solutions = [s for s in change(n, coins, [])]
	for s in solutions:
		print(s)

	print('optimal solution:', min(solutions, key=len))