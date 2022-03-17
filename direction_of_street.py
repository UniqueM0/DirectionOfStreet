"""
Start by getting the street number

If the street number is even, display eastbound

if it is not even, display westbound

finish program
"""
# when input is only one street below
# street = 12

# print("Divide: ", street / 2)
# print("Modulus", street % 2 == 0)

# if street % 2 == 0:
#     print("Eastbound")
# else: 
#     print("Westbound")

# even = (street % 2) == 0
# if street is even:
#     print("Eastbound")
# else: 
#     print("Westbound")


def calculate_street(street):
  print("Divide: ", street / 2)
  print("Modulus", street % 2 == 0)
  if street % 2 == 0:
    print("Eastbound")
  else: 
    print("Westbound")



calculate_street(12)