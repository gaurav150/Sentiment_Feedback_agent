import json
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage
from utils.helpers import load_prompt

rewrite_prompt = PromptTemplate.from_template(load_prompt("prompts/rewrite_prompt.txt"))

def rewrite_tool(llm, text: str) -> str:
    prompt = rewrite_prompt.format(text=text)
    response = llm([HumanMessage(content=prompt)])
    try:
        return json.dumps(json.loads(response.content.strip()), indent=2)
    except:
        return json.dumps({
            "rephrased": "Could not rewrite. Please try again."
        }, indent=2)
