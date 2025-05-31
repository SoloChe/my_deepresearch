import os 
from typing import List, Dict, Union
from ..state.state import State

def construct_messages(
    prompt: Union[str, List[Dict[str, str]]],
    system_prompt: str = "",
    state: State = None,
) -> List[Dict[str, str]]:
    messages = []
    if system_prompt:
        messages.append( )
    if isinstance(prompt, list):
        messages.extend(prompt)
    elif prompt:
        messages.append({"role": "user", "content": prompt})
    if state:
        for message in state.get("messages", []):
            messages.append(message)
    return messages

class OpenAIClient:
    """Example OpenAI client for the React agent."""

    def __init__(self, model: str = "gpt-4.1-mini"):
        """Initialize the OpenAI client.

        Args:
            api_key: OpenAI API key
            model: Model to use (default: gpt-4)
        """
        import openai

        openai_api_key = os.getenv("OPENAI_API_KEY")
        self.client = openai.OpenAI(api_key=openai_api_key)
        self.model = model

    def generate(
        self,
        prompt: Union[str, List[Dict[str, str]]],
        system_prompt: str = "",
        state: State = None,
        stop: List[str] = [],
    ) -> str:
        """Generate a response from the OpenAI API.

        Args:
            prompt: The prompt to send to the API

        Returns:
            Generated text response
        """
        messages = construct_messages(prompt, system_prompt, state)
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            # prevent the model from generating the observation as we want to use the tool
            stop=stop,
        )
        return response.choices[0].message.content