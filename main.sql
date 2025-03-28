CREATE TABLE topics (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    topic_id INTEGER REFERENCES topics(id),
    question TEXT NOT NULL,
    answer TEXT NOT NULL
);


CREATE TABLE choices (
    id SERIAL PRIMARY KEY,
    question_id INTEGER REFERENCES questions(id),
    choice_text TEXT NOT NULL,
    is_correct BOOLEAN NOT NULL
);

CREATE TABLE topic_questions (
    id SERIAL PRIMARY KEY,
    module TEXT NOT NULL,
    submodule TEXT NOT NULL,
    difficulty_level INT CHECK (difficulty_level BETWEEN 1 AND 3),
    question TEXT NOT NULL,
    right_answer TEXT NOT NULL,
    wrong_answers TEXT[] NOT NULL
);