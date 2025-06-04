from database import get_connection


def create_topic(topic_name):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO topics (name) VALUES (%s) RETURNING id;", (topic_name,)) # noqa
            topic_id = cur.fetchone()[0]
            conn.commit()
            return topic_id
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()


def list_topics():
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT id, name FROM topics;")
        topics = cur.fetchall()
    conn.close()
    return topics
