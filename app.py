import os
import json
import streamlit as st
from dotenv import load_dotenv
from agents.agent_executor import agent_executor
from tools.sentiment_tool import sentiment_tool
from tools.rewrite_tool import rewrite_tool
from langchain.chat_models import ChatOpenAI

# Load .env
load_dotenv()

# Setup
llm = ChatOpenAI(temperature=0.3, model="gpt-3.5-turbo")

st.set_page_config(page_title="Sentiment Feedback Agent", page_icon="💬")
st.title("💬 Sentiment Feedback Agent with Rewrite")
st.markdown("Enter a comment. It will show sentiment feedback and rephrase if needed.")

user_input = st.text_area("Your comment:", height=150)

if st.button("Analyze and Rewrite"):
    if user_input.strip():
        with st.spinner("Analyzing..."):
            result = sentiment_tool(llm, user_input)
            data = json.loads(result)

            st.success(f"Sentiment: **{data['sentiment']}**")
            st.info(f"Feedback: {data['feedback']}")

            if data["sentiment"] == "NEGATIVE":
                with st.spinner("Rewriting for positive tone..."):
                    rewrite_result = rewrite_tool(llm, user_input)
                    rewrite_data = json.loads(rewrite_result)
                    st.subheader("💡 Rephrased:")
                    st.success(rewrite_data["rephrased"])
    else:
        st.warning("Please enter some text.")
