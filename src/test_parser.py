from parsers.python_parser import PythonParser

parser = PythonParser()

result = parser.parse(
    "src/executors/tool_executor.py"
)

print(result)