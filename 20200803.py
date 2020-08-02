# English to Maori dictionary
WORD_LIST = {'apple':'aporo','chair':'turu','pen':'pene','hello':'kia ora','goodbye':'ka kite'}

# Menu function
def menu():
    print("Type: \n",
          "'1' to view menu\n",
          "'2' to see word list\n",
          "'3' to translate a word\n",
          "'4' to end program")

# Show word list function
def show_list():
    for word, translation in WORD_LIST.items():
        print("{} = {}".format(word, translation))

# Translation function
def translate(word):
  if word in WORD_LIST:
    translation = WORD_LIST[word]
    print("{} in Maori is {}".format(word.capitalize(), translation))
  else:
    print("Sorry that word is not in the dictionary")
    
translate('apple')
