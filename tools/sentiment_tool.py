import json
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage
from utils.helpers import load_prompt

sentiment_prompt = PromptTemplate.from_template(load_prompt("prompts/sentiment_prompt.txt"))

def sentiment_tool(llm, text: str) -> str:
    prompt = sentiment_prompt.format(text=text)
    response = llm([HumanMessage(content=prompt)])
    try:
        return json.dumps(json.loads(response.content.strip()), indent=2)
    except:
        return json.dumps({
            "sentiment": "UNKNOWN",
            "feedback": "Could not process sentiment."
        }, indent=2)
