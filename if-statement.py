is_male = True
is_tall = True

if is_male and is_tall:
  print("You're a tall male")
elif is_male and not(is_tall):
  print("You're a short male")
elif not(is_male) and is_tall:
  print("You're a tall female")
else:
  print("You're female and not tall")