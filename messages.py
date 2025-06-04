def print_no_questions():
    print("\nNo questions available for the selected topic.")


def print_question_prompt(question, choices):
    print(f"\nQuestion: {question}")
    for idx, choice in enumerate(choices, 1):
        print(f"{idx}. {choice}")


def print_correct_answer():
    print("\u2705 Correct!\n")


def print_wrong_answer(right_answer):
    print(f"\u274C Wrong! The correct answer is: \u2705 {right_answer}\n")


def print_quiz_finish(score, total):
    print(f"\nQuiz completed! Your score: {score}/{total}")
