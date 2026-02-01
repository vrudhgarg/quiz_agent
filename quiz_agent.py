from smolagents import CodeAgent, LiteLLMModel
from tools.document_parser import DocumentParserTool
from tools.question_generator import QuestionGeneratorTool
from tools.answer_evaluator import AnswerEvaluatorTool

# Create the local LLM model
model = LiteLLMModel(model_id = "ollama/qwen2.5:7b")

parser = DocumentParserTool()
generator = QuestionGeneratorTool()
evaluator = AnswerEvaluatorTool()

# Create the agent with all tools
agent = CodeAgent(
    tools = [parser, generator, evaluator],
    model = model
)

# Test it
result = agent.run("What tools do you have available?")
print(result)