import random
from question_service import fetch_random_questions
from topic_service import list_topics
import messages


def take_quiz():
    topics = list_topics()

    if not topics:
        print("No topics available.")
        return

    print("\nAvailable Topics:")
    for tid, name in topics:
        print(f"{tid}. {name}")

    try:
        topic_id = int(input("\nEnter the topic ID to take a quiz: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    questions = fetch_random_questions(topic_id)

    if not questions:
        messages.print_no_questions()
        return

    score = 0
    for _, question, right_answer, wrong_answers in questions:
        choices = wrong_answers + [right_answer]
        random.shuffle(choices)

        messages.print_question_prompt(question, choices)

        try:
            answer = int(input(f"Your answer (1-{len(choices)}): "))
            if choices[answer - 1] == right_answer:
                messages.print_correct_answer()
                score += 1
            else:
                messages.print_wrong_answer(right_answer)
        except (ValueError, IndexError):
            print("Invalid input. Moving to next question.")

    messages.print_quiz_finish(score, len(questions))
