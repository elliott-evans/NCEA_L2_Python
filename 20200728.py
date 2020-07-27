#Questions and answers for a quiz - note that these longer list items are written on one line each to make it easy to read.
questions = ["How many bits are in a byte?",
            "True or False? A nibble is half a byte.",
            "What year was Google founded?",
            "How many zeroes are in a Googol?",
            "How many bytes are in a kilobyte?"]

answers = [["8", "eight"], ["true", "t"], ["1998", "98"], ["100", "hundred"], ["1024", "one thousand and twenty four"]]

score = 0

#Ask the user their name and welcome them to the quiz
name = input("What is your name?")
print("Welcome to the quiz, {}! There are 5 questions.".format(name))

#Use a loop to ask the questions and get the user's guess from the input
for question, answer_list in zip(questions, answers):
  guess = input(question).strip().lower()

  #Check if the user's answer is in the corresponding row
  if guess in answer_list:
    print("Correct!")
    score += 1
  else:
    print("Wrong! The correct answer was {}!".format(answer_list[0]))

print("You scored {}/5, {}".format(score, name))
