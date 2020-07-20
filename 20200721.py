#Write your code here
rating = int(input("please rate movie"))

if rating == 3:
  print("Pretty average huh?")
elif rating < 3:
  print("Wow, that must have been bad!")
elif rating > 3 and rating <= 5:
  print("Sounds like a great movie!")
else:
  print("I said out of 5!")
