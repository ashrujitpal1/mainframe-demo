# agents/code_generator_agent.py
from typing import Any
from langchain.agents import Agent
from langchain.prompts import PromptTemplate

class CodeGeneratorAgent(Agent):
    def __init__(self):
        self.tools = [CodeGeneratorAPITool()]
        
        self.prompt = PromptTemplate(
            template="""You are a Code Generator Agent.
            Your task is to generate code based on the given user story.
            
            User Story: {user_story}
            
            Generate the code implementation for this user story.
            """,
            input_variables=["user_story"]
        )

    async def process(self, user_story: str) -> dict[str, Any]:
        tool = self.tools[0]
        result = tool.run(user_story)
        return result
