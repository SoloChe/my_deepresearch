# nanoDeepResearch
Copied from [nanoDeepResearch](https://github.com/liyuan24/nanoDeepResearch) for the purpose of learning. Added `uv` for managing the virtual environment. 

You can use 

`uv sync` 

to synchronize the environment. For testing,

`uv run python -m myDeepResearch.main --query "your query here" ` 

Some API keys are required to run the project, such as openai, tavily and jina. You can 

`export API_KEY="your_key"` 

to set the environment variable.

## TODO
1. Preparing the MCP for tool use.
