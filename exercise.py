from config import config
import psycopg2 as pg
import random

def connect_db():
    return pg.connect(**config)

def get_topics():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM topics;")  # Adjusted to fetch topic names
    topics = cur.fetchall()
    cur.close()
    conn.close()
    return topics

def get_random_questions(topic_id, num_questions=5):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT id, question, right_answer, wrong_answers
        FROM topic_questions
        WHERE topic_id = %s
        ORDER BY RANDOM()
        LIMIT %s;
    """, (topic_id, num_questions))
    questions = cur.fetchall()
    cur.close()
    conn.close()
    return questions

def add_topic():
    topic_name = input("\nEnter the new topic name: ")
    conn = connect_db()
    cur = conn.cursor()

    try:
        cur.execute("INSERT INTO topics (name) VALUES (%s) RETURNING id;", (topic_name,))
        topic_id = cur.fetchone()[0]
        conn.commit()
        print(f"\nTopic '{topic_name}' added successfully with ID {topic_id}!")
    except pg.IntegrityError:
        conn.rollback()
        print("\nTopic already exists!")
    finally:
        cur.close()
        conn.close()

def add_question():
    topics = get_topics()

    if not topics:
        print("\nNo topics found! Please add a topic first.")
        return

    print("\nAvailable Topics:")
    for tid, name in topics:
        print(f"{tid}. {name}")

    try:
        topic_id = int(input("\nEnter topic ID to add a question: "))  # noqa
    except ValueError:
        print("Invalid topic ID! Please enter a valid number.")
        return

    module = input("Enter module name: ")
    submodule = input("Enter submodule name: ")
    difficulty = int(input("Enter difficulty level (1-3): "))
    question = input("Enter the question: ")
    right_answer = input("Enter the correct answer: ")
    wrong_answers = [input(f"Enter wrong answer {i+1}: ") for i in range(3)]

    conn = connect_db()
    cur = conn.cursor()

    try:
        cur.execute("""
            INSERT INTO topic_questions (module, submodule, difficulty_level, question, right_answer, wrong_answers, topic_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
        """, (module, submodule, difficulty, question, right_answer, wrong_answers, topic_id))  # Corrected to include topic_id
        conn.commit()
        print("\nQuestion added successfully!")
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()


def take_quiz():
    topics = get_topics()  # Fetch available topics

    if not topics:
        print("No topics available.")
        return

    print("\nAvailable Topics:")
    for tid, name in topics:
        print(f"{tid}. {name}")  # Display topic ID and name

    try:
        topic_id = int(input("\nEnter the topic ID to take a quiz: "))
        # Check if the entered topic ID exists
        if not any(tid == topic_id for tid, _ in topics):
            print("Invalid topic ID. Please select a valid topic.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Now fetch questions for the selected topic ID
    questions = get_random_questions(topic_id, num_questions=5)

    if not questions:
        print("No questions available for this topic.")
        return

    score = 0
    for qid, question, right_answer, wrong_answers in questions:
        choices = wrong_answers + [right_answer]
        random.shuffle(choices)  # Shuffle the choices

        print(f"\nQuestion: {question}")
        for idx, choice in enumerate(choices, 1):
            print(f"{idx}. {choice}")  # Display shuffled choices

        try:
            answer = int(input("Your answer (1-{}): ".format(len(choices))))
            if choices[answer - 1] == right_answer:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong. The correct answer is: {right_answer}")
        except (ValueError, IndexError):
            print("Invalid input. Skipping question.")
            continue

    print(f"\nQuiz completed! Your score: {score}/{len(questions)}")
