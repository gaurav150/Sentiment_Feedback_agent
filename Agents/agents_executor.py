from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI
from tools.sentiment_tool import sentiment_tool
from tools.rewrite_tool import rewrite_tool

llm = ChatOpenAI(temperature=0.3, model="gpt-3.5-turbo")

tools = [
    Tool(
        name="SentimentFeedbackTool",
        func=lambda text: sentiment_tool(llm, text),
        description="Analyzes text sentiment and gives feedback."
    ),
    Tool(
        name="RewriteNegativeCommentTool",
        func=lambda text: rewrite_tool(llm, text),
        description="Rewrites harsh or negative comments into polite, constructive ones."
    )
]

agent_executor = initialize_agent(
    tools=tools,
    llm=llm,
    agent="chat-zero-shot-react-description",
    verbose=False
)
