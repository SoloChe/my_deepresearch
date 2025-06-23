from typing import Callable, Any


class Tool:
    """Tool that the agent can use."""

    def __init__(self, name: str, description: str):
        """Initialize a tool.

        Args:
            name: Name of the tool
            description: Description of what the tool does
        """
        self.name = name
        self.description = description
