# Python weight convertor

weight = float(input("Enter your weight: "))
unit = input("Kilogram or Pounds ? (K / L): ")

if unit == "K":
    weight = weight * 2.205
    print(weight)
    unit = "Lbs."
    print(f"Your weight is: {round(weight, 2)} {unit} ")
elif unit == "L":
    weight = weight / 2.205
    print(weight)
    unit = "Kgs."
    print(f"Your weight is: {round(weight, 2)} {unit}")
else:
    print(f"{unit} is not a valid input")
