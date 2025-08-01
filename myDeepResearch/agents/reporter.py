from typing import List, Union
from ..llm.llm import OpenAIClient, AnthropicClient
from ..state.state import State
from ..prompts.utils import load_prompt


class Reporter:
    def __init__(
        self, llm_client: Union[OpenAIClient, AnthropicClient], locale: str = "en-US"
    ):
        self.system_prompt = load_prompt("reporter", {"locale": locale})
        self.llm_client = llm_client

    def report(self, state: State = None) -> List[str]:
        human_messages = []
        current_plan = state.get("current_plan")
        human_messages.append(
            {
                "role": "user",
                "content": f"# Research Requirements\n\n## Task\n\n{current_plan.title}\n\n## Description\n\n{current_plan.thought}",
            }
        )
        for observation in state.get("observations", []):
            human_messages.append(
                {
                    "role": "user",
                    "content": f"Below are some observations for the research task:\n\n{observation}",
                }
            )
        response = self.llm_client.generate(human_messages, self.system_prompt)
        return response


if __name__ == "__main__":
    reporter = Reporter(OpenAIClient(model="gpt-4.1-mini"))
    print(reporter.report())
