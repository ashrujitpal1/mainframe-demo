# agents/java_code_formatter_agent.py
import os
from langchain.agents import Agent
from langchain.prompts import PromptTemplate
from langchain.llms import Ollama

class JavaCodeFormatterAgent(Agent):
    def __init__(self):
        
        self.prompt = PromptTemplate(
            template="""You are a Java Code Formatter Agent.
            Format and organize the following Java code into appropriate files and packages.
            
            Code: {code}
            
            Organize the code into proper Java files with correct package structure.
            """,
            input_variables=["code"]
        )

    def write_java_file(self, package_name: str, class_name: str, content: str):
        # Create package directory structure
        package_path = package_name.replace('.', '/')
        os.makedirs(f"output/{package_path}", exist_ok=True)
        
        # Write Java file
        file_path = f"output/{package_path}/{class_name}.java"
        with open(file_path, 'w') as f:
            f.write(content)

    async def process(self, code_content: Dict[str, Any]) -> None:
        for file_info in code_content['files']:
            self.write_java_file(
                file_info['package'],
                file_info['class_name'],
                file_info['content']
            )
