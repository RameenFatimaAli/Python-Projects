questions = [
    "Which planet is known as the Red Planet?",
    "What is the largest organ in the human body?",
    "Which gas do plants use to perform photosynthesis?",
    "What is the currency of Japan?"
]

answers = ["Mars", "Skin", "Carbon dioxide", "Yen"]


def ask_question(question, correct_answer, current_amount):
    print(question)
    options = "\n".join([f"{index + 1}. {answer}" for index, answer in enumerate(correct_answer)])
    print(options)

    user_answer = input("Type the answer (1, 2, 3, 4): ")

    if user_answer == str(correct_answer.index(correct_answer) + 1):
        return current_amount + 10, True
    else:
        print(f"Nice try but WRONG ANSWER. Better luck next time. You won ${current_amount}")
        return current_amount, False


def main():
    print("\t\t\tWelcome to the game \"Kaun Banega Crorepati\"")
    print("Press 0 (zero) to continue: ")

    user_input = int(input())

    if user_input == 0:
        current_amount = 0
        print(f"Current amount in your account: ${current_amount}")
        print("For every right answer to each question, $10 will be added to your account.")
        print("The game ends when you give a wrong answer.")

        start_game = input("Are you ready to start the questionnaire? Type YES: ")

        if start_game == "YES":
            for index, question in enumerate(questions):
                current_amount, is_correct = ask_question(question, answers[index], current_amount)

                if not is_correct:
                    break

            print("\t\t\tWELL DONE")
            print(f"\t\t\tYOU WON ${current_amount}")
            print("Game Ended!!!!!")

        else:
            print("Invalid input\n!!!!!GAME ENDED!!!!!")
    else:
        print("Invalid input")
        print("!!!!!GAME ENDED!!!!!")


if __name__ == "__main__":
    main()
