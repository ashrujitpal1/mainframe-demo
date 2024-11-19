# tools/api_tools.py
import requests
from langchain.tools import BaseTool
from typing import Dict, Any

class UserStoryAPITool(BaseTool):
    name = "user_story_generator"
    description = "Generates user stories by calling an external API"

    def _run(self, topic: str) -> Dict[str, Any]:
        try:
            response = requests.post(
                "http://localhost:5002/generate",
                json={"topic": topic}
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            raise Exception(f"Error calling User Story API: {str(e)}")

class CodeGeneratorAPITool(BaseTool):
    name = "code_generator"
    description = "Generates code by calling an external API"

    def _run(self, user_story: str) -> Dict[str, Any]:
        try:
            response = requests.post(
                "http://localhost:5003/generate",
                json={"user_story": user_story}
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            raise Exception(f"Error calling Code Generator API: {str(e)}")
