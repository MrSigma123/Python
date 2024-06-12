# Leap year checker
print("Welcome to leap year checker! Enter the year to be checked: ")
year = int(input())

leap = bool(0)
if year % 4 == 0:
  leap = 1
  if year % 100 == 0:
    leap = 0
    if year % 400 == 0:
      leap = 1
else:
  leap = 0

if leap == 1:
  print(f"The year {year} is a leap year")
else:
  print(f"The year {year} is not a leap year")
  
  
