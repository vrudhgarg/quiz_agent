from dataclasses import dataclass
from enum import Enum
import json

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

    @classmethod
    # cls refers to the class itself (Question). It's like self, but for the class
    def from_json(cls, json_string: str) -> list["Question"]:
        """Parse JSON string from LLM into list of Question objects."""
        
        # Remove ```json wrapper if present
        text = json_string.strip()
        if text.startswith("```json"):
            text = text[7:]
        if text.startswith("```"):
            text = text[3:]
        if text.endswith("```"):
            text = text[:-3]
        text = text.strip()
        
        # Parse JSON string into Python dict
        data = json.loads(text)
        
        # Convert each dict to Question object
        questions = []
        for q in data["questions"]:
            questions.append(cls(
                question_type=QuestionType.MCQ,  # Default for now
                question_text=q["question_text"],
                correct_answer=q["correct_answer"],
                options=q.get("options", []),
                explanation=q.get("explanation", "")
            ))
        
        return questions
