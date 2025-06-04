from database import get_connection


def add_question(topic_id, module, submodule, difficulty, question, right_answer, wrong_answers): # noqa
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO topic_questions
                (module, submodule, difficulty_level, question, right_answer, wrong_answers, topic_id) # noqa
                VALUES (%s, %s, %s, %s, %s, %s, %s);
            """, (module, submodule, difficulty, question, right_answer, wrong_answers, topic_id))
            conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()


def fetch_random_questions(topic_id, num_questions=5):
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("""
            SELECT id, question, right_answer, wrong_answers
            FROM topic_questions
            WHERE topic_id = %s
            ORDER BY RANDOM()
            LIMIT %s;
        """, (topic_id, num_questions))
        questions = cur.fetchall()
    conn.close()
    return questions
