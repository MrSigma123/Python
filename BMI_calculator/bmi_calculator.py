# This is BMI_calculator
print("Welcome to BMI calculator!\n")
print("Enter your height in meters (i.e. 1.68):")
height = float(input())
print("Enter your weight in kilograms (i.e. 58):")
weight = int(input())

bmi = round(weight/(height ** 2), 1)

if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25.0:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30.0:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35.0:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")
