"""
Lab 4.5
"""
from random import randint
from math import sqrt



def max(a, b):
  if a > b:
    return a
  else:
    return b


def area_of_triangle(b, h):
  area = b * h / 2
  return area


def roll_dN(n):
  roll = randint(1, n)
  return roll 


def is_negative(num):
  if num < 0:
    return True
  else:
    return False


def three_d6():
  roll1 = roll_dN(6)
  roll2 = roll_dN(6)
  roll3 = roll_dN(6)

  sum = roll1 + roll2 + roll3
  return sum


def binet(n):

  phi = (1 + sqrt(5)) / 2
  phi_hat = (1 - sqrt(5)) / 2

  F_n = (1 / sqrt(5)) * (phi ** n - phi_hat ** n)
  return round(F_n)


def is_banana(str):
  if str == "banana":
    return True
  else:
    return False


def divisible_by_7(n):
  if n % 7 == 0:
    return True
  else:
    return False


# If you see "None" as your output it almost always means you left out a return function