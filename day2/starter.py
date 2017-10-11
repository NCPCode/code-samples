print("This can convert either pounds to kilograms or kilograms to pounds.")
convert_to = input("Do you have want to convert to pounds or kilograms?")

weight = int(input("Input weight (without unit): "))

print("Your converted weight is ")

if convert_to == "pounds":
  weight = weight * 2.20462
  print(weight, " pounds")
elif convert_to == "kilograms":
  weight = weight * 0.453592
  print(weight, " kilograms")
else:
  print("Sorry, I don't recognize that unit!")
