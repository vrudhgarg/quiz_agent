from dataclasses import dataclass
from enum import Enum

# Enum restricts question types to only these 3 options
# Prevents typos and invalid types
class QuestionType(Enum):
    MCQ = "multiple_choice"
    SHORT_ANSWER = "short_answer"
    TRUE_FALSE = "true_false"

# dataclass auto-generates __init__ and other methods
# Cleaner than writing a regular class with boilerplate
@dataclass
class Question:
    question_type: QuestionType # What kind of question (MCQ, short answer, or true/false)    
    question_text: str # The actual question text shown to user
    correct_answer: str # The correct answer for evaluation
    options: list # Answer choices - only used for MCQ (e.g., ["Paris", "London", "Berlin"])
    explanation: str # Why this answer is correct - shown after user answers
