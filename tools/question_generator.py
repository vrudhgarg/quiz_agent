from smolagents import Tool
import json
import litellm


class QuestionGeneratorTool(Tool):
    # Tool identifier
    name = "question_generator"
    
    # Agent reads this to know when to use this tool
    description = "Generates quiz questions from lecture notes content. Returns questions in JSON format."
    
    # What arguments this tool accepts
    inputs = {
        "content": {
            "type": "string",
            "description": "The lecture notes text to generate questions from"
        },
        "num_questions": {
            "type": "integer", 
            "description": "Number of questions to generate"
        },
        "question_type": {
            "type": "string",
            "description": "Type of questions: 'mcq', 'short_answer', or 'true_false'"
        }
    }
    
    # What this tool returns
    output_type = "string"

    def forward(self, content: str, num_questions: int, question_type: str) -> str:
        """Generate questions from content using local LLM."""
        

        # Build the prompt for the LLM
        prompt = f"""Based on the following lecture notes, generate {num_questions} {question_type} questions.

LECTURE NOTES:
{content}

Return ONLY valid JSON in this exact format:
{{
    "questions": [
        {{
            "question_text": "Your question here",
            "correct_answer": "The correct answer text",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "explanation": "Why this is correct"
        }}
    ]
}}

IMPORTANT RULES:
- For multiple_choice: options must be 4 meaningful choices related to the question, not "A", "B", "C", "D". The correct_answer must match one of the options exactly.
- For true_false: options should be ["True", "False"]. correct_answer should be "True" or "False".
- For short_answer: options should be an empty list [].
"""
        
        # Call local Ollama model
        response = litellm.completion(
            model="ollama/qwen2.5:7b",
            messages=[{"role": "user", "content": prompt}]
        )
        
        # Extract the text response
        return response.choices[0].message.content