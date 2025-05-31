from typing import List, Union
from ..llm.llm import OpenAIClient, AnthropicClient
from ..prompts.planner_model import Plan
from ..state.state import State
from ..prompts.utils import load_prompt


class Planner:
    def __init__(
        self,
        llm_client: Union[OpenAIClient, AnthropicClient],
        max_step_num: int = 3,
        locale: str = "en-US",
    ):
        self.system_prompt = load_prompt(
            "planner", {"max_step_num": max_step_num, "locale": locale}
        )
        self.llm_client = llm_client

    def plan(self, query: str, state: State = None) -> List[str]:
        response = self.llm_client.generate(query, self.system_prompt, state)
        # parse the response with pydantic
        return Plan.model_validate_json(response)


if __name__ == "__main__":
    planner = Planner(OpenAIClient(model="gpt-4.1-mini"))
    print(
        planner.plan(
            "what is the ratio between the area of the largest and smallest states in the US?"
        )
    )
