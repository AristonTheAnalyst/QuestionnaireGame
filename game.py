# Initialize empty variables
name = ""
score = 0
question_number = 3
questions = [
    {"question" : "What is the national bird of New Zealand?",
     "options" : ["Pukeko", "Hedgehog", "Raccoon", "Kiwi"],
     "correct_answer" : "Kiwi"
     },
    {"question" : "What supermarket has recently changed their trade name to ""Woolworths"" ",
     "options" : ["New World", "Pak N Save", "Barro", "Countdown"],
     "correct_answer" : "Countdown"
     },
    {"question" : "What is New Zealand's premier rugby team?",
     "options" : ["All Whites", "All Greys", "All Kiwis", "All Blacks"],
     "correct_answer" : "All Blacks"
     }
]

# # Welcome
# print("Welcome!")

# # Ask name and Store name
# name = input("What is your name?\n")
# print("Welcome to the questionnaire game, "+name)
# print("\nLets get started!")

for i in range(question_number):
    print(questions[i-1]["question"])
    print("What questions")

# Are there questions left?
# - Needs a list of questions (Maybe a dictionary, or create a class?)

# Randomly select unasked question until X questions have been asked, or if there are no more questions left.

    # Player answers

    # Cases for correct, incorrect and invalid answers

# Announce game score, and closing message, ask the player if they want to play again