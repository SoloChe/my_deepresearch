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
        messages.append({"role": "system", "content": system_prompt})
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
class AnthropicClient:
    """Example Anthropic client for the React agent."""

    def __init__(self, model: str = "claude-3-sonnet-20240229"):
        """Initialize the Anthropic client.

        Args:
            api_key: Anthropic API key
            model: Model to use (default: claude-3-sonnet-20240229)
        """
        import anthropic

        anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
        self.client = anthropic.Anthropic(api_key=anthropic_api_key)
        self.model = model

    def generate(
        self,
        prompt: Union[str, List[Dict[str, str]]],
        system_prompt: str = "",
        state: State = None,
        stop: List[str] = [],
    ) -> str:
        """Generate a response from the Anthropic API.

        Args:
            prompt: The prompt to send to the API

        Returns:
            Generated text response
        """
        messages = construct_messages(prompt, system_prompt, state)
        response = self.client.messages.create(
            model=self.model,
            max_tokens=2000,
            messages=messages,
            # prevent the model from generating the observation as we want to use the tool
            stop_sequences=stop,
        )
        return response.content[0].text