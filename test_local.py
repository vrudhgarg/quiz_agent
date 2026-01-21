from smolagents import CodeAgent, LiteLLMModel

# Connect to local Ollama
model = LiteLLMModel(model_id = "ollama/qwen2.5:7b")

agent = CodeAgent(tools =[], model=model)

result = agent.run("What is 25 * 37? Calculate it step by step.")
print(result)