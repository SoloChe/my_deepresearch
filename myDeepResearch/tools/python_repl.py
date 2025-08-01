import io
import sys
from .tool import Tool


class PythonREPLTool(Tool):
    def __init__(self):
        super().__init__("python_repl", "Useful for executing Python code.")
        self.locals = {}

    def __call__(self, code_string: str) -> str:
        # Create a string buffer to capture output
        output_buffer = io.StringIO()
        # Save the current stdout
        old_stdout = sys.stdout
        # Redirect stdout to the buffer
        sys.stdout = output_buffer

        try:
            # Execute the code string
            exec(code_string, {}, self.locals)
        except Exception as e:
            # Capture any exceptions
            output_buffer.write(f"Error: {e}\n")
        finally:
            # Restore the original stdout
            sys.stdout = old_stdout

        # Get the output from the buffer
        output = output_buffer.getvalue()
        output_buffer.close()
        return output


if __name__ == "__main__":
    repl = PythonREPLTool()
    code = """
x = 10
y = 20
sum = x + y
# need to print because we use stringIO to capture output
print(sum)
"""
    print(repl(code))
