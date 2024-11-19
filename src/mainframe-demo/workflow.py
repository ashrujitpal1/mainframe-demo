# workflow/graph.py
from code_generator_agent import CodeGeneratorAgent
from java_code_formatter_agent import JavaCodeFormatterAgent
from langgraph.graph import Graph
from typing import Dict, Any

from user_story_agent import UserStoryAgent

async def create_workflow(topic: str):
    # Initialize agents
    user_story_agent = UserStoryAgent()
    code_generator_agent = CodeGeneratorAgent()
    java_formatter_agent = JavaCodeFormatterAgent()

    # Define the graph
    workflow = Graph()

    # Add nodes
    workflow.add_node("generate_user_stories", user_story_agent.process)
    workflow.add_node("generate_code", code_generator_agent.process)
    workflow.add_node("format_code", java_formatter_agent.process)

    # Define edges
    @workflow.edge("generate_user_stories", "generate_code")
    async def process_user_stories(user_stories: Dict[str, Any]) -> Dict[str, Any]:
        results = []
        for story in user_stories['stories']:
            code_result = await code_generator_agent.process(story)
            results.append(code_result)
        return {'code_generations': results}

    @workflow.edge("generate_code", "format_code")
    async def prepare_code_formatting(code_results: Dict[str, Any]) -> Dict[str, Any]:
        return {'files': code_results['code_generations']}

    # Set the entry point
    workflow.set_entry_point("generate_user_stories")

    # Execute the workflow
    result = await workflow.run({"topic": topic})
    return result
