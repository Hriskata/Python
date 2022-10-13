import time

def new_game():
    guesses = []
    number_q = 1
    correct_guesses = 0

    for key in questions:
        print("-------------------")
        print("Question number ", number_q)
        print(key)
        for i in options[number_q - 1]:
            print(i)
        guess = None
        while guess not in options_to_answer:
            guess = input("Enter A,B,C or D : ").upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        number_q += 1
    display_score(correct_guesses, guesses)


# ---------------------
def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0


# ---------------------
def display_score(correct_guesses, guesses):
    print("---------------------")
    print("RESULTS")
    print("---------------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    print("Score: " + str(correct_guesses) + " points")


# ---------------------
def play_again():
    response = input("Do you want play again: (yes/no): ").lower()
    if response == "yes":
        return True
    else:
        return False
# ---------------------


questions = {
    "Кога е създадена България ?:": "A",
    "question_2 ?:": "B",
    "question_3 ?:": "C",
    "question_4 ?:": "A",
}

options_to_answer = ["A", "B", "C", "D"]

options = [["A - 681", "B - 1210", "C - 870", "D - 756"],
           ["A - 1", "B - 2", "C - 3", "D - 4"],
           ["A - 1", "B - 2", "C - 3", "D - 4"],
           ["A - 1", "B - 2", "C - 3", "D - 4"]]

new_game()

while play_again():
    new_game()

print("Good bye!")
for seconds in range(3, 0, -1):
    time.sleep(1)
