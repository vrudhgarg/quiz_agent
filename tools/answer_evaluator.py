from smolagents import Tool
import litellm
class AnswerEvaluatorTool(Tool):
    # Tool identifer
    name = "answer_evaluator"

    # Agents reads the following to know when to use the tool
    description = "Evaluates if a user's answer is correct by comparing it with the correct answer."

    # What argument this tool accepts
    inputs = {
        "user_answer" : {
            "type": "string",
            "description": "The answer provided by the user"
        },
        "correct_answer" : {
            "type": "string",
            "description": "The correct answer to compare against"

        },
        "question_type": {
            "type": "string",
            "description": "Type of question: 'mcq', 'true_false', or 'short_answer'"

        }
    }

    # What this tool returns
    output_type = "string"

    def forward(self, user_answer : str, correct_answer : str, question_type: str) -> str:
        ''' Evaluates the user answer'''

        # Basic cleaning for the answer
        user_clean = user_answer.strip().lower()
        correct_clean = correct_answer.strip().lower()

        # MCQ and True/False: simple string matching
        if question_type in ["mcq", "multiple_choice", "true_false"]:
            if user_clean == correct_clean:
                return "correct"
            
            else:
                return "incorrect"

        # Use LLM to evaluate
        if question_type in ["short_answer", "short"]:
            return self._evaluate_short_answer(user_clean, correct_clean)

        return "unknown question type"


    def _evaluate_short_answer(self, user_answer, correct_answer):
        """ Use LLM to evaluate short answer"""
        prompt = f"""Compare the user's answer to the correct answer.
        
        Correct answer: {correct_answer}
        User's answer: {user_answer}

        Is the user's answer correct? They don't need to match exactly - check if the meaning is the same.

        Reply with ONLY one word: "correct" or "incorrect"
        """

        response = litellm.completion(
            model = "ollama/qwen2.5:7b",
            messages = [{"role" : "user", "content" : prompt}]
        )

        result = response.choices[0].message.content.strip().lower()

        if "correct" in result and "incorrect" not in result:
            return "correct"
        else:
            return "incorrect"


