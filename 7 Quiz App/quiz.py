# ----------------------------------------
# Quiz Application
# ----------------------------------------

# Quiz Questions
quiz = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Pune", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which language is primarily used for Data Science?",
        "options": ["A. Python", "B. Java", "C. C++", "D. PHP"],
        "answer": "A"
    },
    {
        "question": "Who developed Python?",
        "options": ["A. Dennis Ritchie", "B. James Gosling", "C. Guido van Rossum", "D. Elon Musk"],
        "answer": "C"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. define", "C. def", "D. fun"],
        "answer": "C"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. <!-- -->", "C. #", "D. **"],
        "answer": "C"
    }
]


# ----------------------------
# Run Quiz
# ----------------------------
def run_quiz():

    score = 0

    print("=" * 45)
    print("        PYTHON QUIZ APPLICATION")
    print("=" * 45)

    for index, question in enumerate(quiz, start=1):

        print(f"\nQuestion {index}: {question['question']}")

        for option in question["options"]:
            print(option)

        while True:
            answer = input("Enter your answer (A/B/C/D): ").upper()

            if answer in ["A", "B", "C", "D"]:
                break
            else:
                print("Invalid option! Please enter A, B, C or D.")

        if answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

    return score


# ----------------------------
# Show Correct Answers
# ----------------------------
def show_answers():

    print("\nCorrect Answers:")

    for index, question in enumerate(quiz, start=1):
        print(f"{index}. {question['answer']}")


# ----------------------------
# Main Program
# ----------------------------
def main():

    while True:

        score = run_quiz()

        print("\n" + "=" * 45)
        print(f"Final Score: {score}/{len(quiz)}")
        print("=" * 45)

        show_answers()

        choice = input("\nPlay Again? (y/n): ").lower()

        if choice != "y":
            print("\nThank you for playing!")
            break


if __name__ == "__main__":
    main()