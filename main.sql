-- CREATE TABLE topics (
--     id SERIAL PRIMARY KEY,
--     name TEXT UNIQUE NOT NULL
-- );


-- CREATE TABLE questions (
--     id SERIAL PRIMARY KEY,
--     topic_id INTEGER REFERENCES topics(id),
--     question TEXT NOT NULL,
--     answer TEXT NOT NULL
-- );


-- CREATE TABLE choices (
--     id SERIAL PRIMARY KEY,
--     question_id INTEGER REFERENCES questions(id),
--     choice_text TEXT NOT NULL,
--     is_correct BOOLEAN NOT NULL
-- );


-- CREATE TABLE topic_questions (
--     id SERIAL PRIMARY KEY,
--     module TEXT NOT NULL,
--     submodule TEXT NOT NULL,
--     difficulty_level INT CHECK (difficulty_level BETWEEN 1 AND 3),
--     question TEXT NOT NULL,
--     right_answer TEXT NOT NULL,
--     wrong_answers TEXT[] NOT NULL
-- );
-- -- 

-- INSERT INTO topic_questions (module, submodule, difficulty_level, question, right_answer, wrong_answers)
-- VALUES ('General Knowledge', 'Geography', 2, 
--         'What is the capital of Cameroon?', 'Yaoundé', ARRAY['Abuja', 'Paris', 'Windhoek']);


-- SELECT EXISTS (
--     SELECT 1 FROM information_schema.tables 
--     WHERE table_name = 'Geography_questions'
-- );


-- SELECT id, question, 
--        array_append(wrong_answers, right_answer) AS choices
-- FROM topic_questions
-- ORDER BY RANDOM()
-- LIMIT 1;

-- Create table for topics
CREATE TABLE topics (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

-- Create table for questions
CREATE TABLE topic_questions (
    id SERIAL PRIMARY KEY,
    module TEXT NOT NULL,
    submodule TEXT NOT NULL,
    difficulty_level INT CHECK (difficulty_level BETWEEN 1 AND 3),
    question TEXT NOT NULL,
    right_answer TEXT NOT NULL,
    wrong_answers TEXT[] NOT NULL,
    topic_id INTEGER REFERENCES topics(id) ON DELETE CASCADE
);

-- Optional: You could create a separate choices table if you want to store choices separately (Not needed if storing as arrays in topic_questions)
CREATE TABLE choices (
    id SERIAL PRIMARY KEY,
    question_id INTEGER REFERENCES topic_questions(id) ON DELETE CASCADE,
    choice_text TEXT NOT NULL,
    is_correct BOOLEAN NOT NULL
);

-- Insert some sample data for testing purposes (you can modify these as needed)
INSERT INTO topics (name) VALUES ('General Knowledge'), ('Geography');

-- Sample question for General Knowledge / Geography
INSERT INTO topic_questions (module, submodule, difficulty_level, question, right_answer, wrong_answers, topic_id)
VALUES 
('General Knowledge', 'Geography', 2, 'What is the capital of Cameroon?', 'Yaoundé', ARRAY['Abuja', 'Paris', 'Windhoek'], 1);
