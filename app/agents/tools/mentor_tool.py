from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import tool
from langchain.tools import StructuredTool
from langchain_experimental.utilities import PythonREPL
from typing import Annotated


def mentor_introduction_fn(mentor_name: str, mentorship_name: str, student_name: str)-> str:
    """ Give context about a mentor and their students """
    message = f"Hello, {student_name}. I am {mentor_name}. I am a mentor in {mentorship_name}. I am here to help you with any questions you have."

    return message

mentor_introduction_tool = StructuredTool.from_function(mentor_introduction_fn)


tavily_tool = TavilySearchResults(max_results=5)

repl = PythonREPL()


@tool
def python_repl_tool(
    code: Annotated[str, "The python code to execute to generate your chart."],
):
    """Use this to execute python code and do math. If you want to see the output of a value,
    you should print it out with `print(...)`. This is visible to the user."""
    try:
        result = repl.run(code)
    except BaseException as e:
        return f"Failed to execute. Error: {repr(e)}"
    result_str = f"Successfully executed:\n```python\n{code}\n```\nStdout: {result}"
    return result_str
