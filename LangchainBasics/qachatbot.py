# """" 
# Simple Langchain Streamlite App with Groq 
# A beginner-friendly version focusing on core concept 
# """

# import streamlit as st
# from langchain.chat_models import init_chat_model
# from langchain_groq import ChatGroq
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.messages import HumanMessage, AIMessage
# from langchain_core.prompts import ChatPromptTemplate
# import os


# ## Page Config

# st.set_page_config(page_title="Simple Langchain Chatbot with Groq" , page_icon="🚀")


# # Title
# st.title("🚀 Simple Langchain Chatbot with Groq")
# st.markdown("Learn Langchain basics with Groq's ultra-fast inferences!")



# with st.sidebar:
#     st.header("Setting")
    
#     ## API key input
#     api_key = st.text_input("Enter your Groq API Key", type="password" , help = "Get your API key from https://groq.com/dashboard/api-keys")

#     ## Model Selection Dropdown 
# model_name=st.selectbox(
#     "Model ", 
#     ["llama2-8b-8192" , "llama-3.1-8b-instant"], 
#     index =0
# ) 

# #clear Button

# if st.button("Clear Conversation"):
#     st.session_state.messages = []
#     st.rerun()


# #Initialize the chat history

# if "messages" not in st.session_state:
#     st.session_state.messages = []


# ##Initialize LLM
# @st.cache_resource
# def get_chain(api_key, model_name):
#     if not api_key:
#         return None
    
#     ##Initialize the Groq Chat Model
#     llm=ChatGroq(groq_api_key=api_key, 
#              model_name=model_name,
#              temperature=0.7,
#              streaming=True)
    

#     ## Create prompt template

#     prompt = ChatPromptTemplate.from_messages([
#         ("system", "You are a helpful assistant that answers questions based on the conversation history."),
#         ("user", "{Question}")
#     ])



#     ## create chain
#     chain=prompt| llm | StrOutputParser()
#     return chain

# ## get chain

# chain= get_chain(api_key, model_name)

# if not chain:
#     st.warning("Please enter your Groq API Key to start the conversation.")
#     st.markdown("[Get your API key from Groq Dashboard](https://groq.com/dashboard/api-keys)")
# else:
#     ##Display the chat messages
#     for message in st.session_state.messages:
#         with st.chat_message(message["role"]):
#             st.write(message["content"])


#     ## chat input 
#     if question := st.chat_input("Ask me anything!"):

#         # Add user message to chat history
#         st.session_state.messages.append({"role": "user", "content": question})
#         with st.chat_message("user"):
#             st.write(question)
        
#         # Generate response
# with st.chat_message("assistant"):
#     message_placeholder = st.empty()
#     full_response = ""

#     try:
#         # Stream response from Groq
#         for chunk in chain.stream({"question": question}):
#             full_response += chunk
#             message_placeholder.markdown(full_response + "▌")

#         message_placeholder.markdown(full_response)

#         # Add to history
#         st.session_state.messages.append(
#             {"role": "assistant", "content": full_response}
#         )

#     except Exception as e:
#         st.error(f"Error: {str(e)}")


# ## Examples

# st.markdown("---")
# st.markdown("### 💡 Try these examples:")
# col1, col2 = st.columns(2)

# with col1:
#     st.markdown("- What is LangChain?")
#     st.markdown("- Explain Groq's LPU technology")

# with col2:
#     st.markdown("- How do I learn programming?")
#     st.markdown("- Write a haiku about AI")


# # Footer
# st.markdown("---")
# st.markdown("Built with LangChain & Groq | Experience the speed! ⚡")




""" 
Simple Langchain Streamlit App with Groq 
A beginner-friendly version focusing on core concepts
"""

import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


# Page Config
st.set_page_config(
    page_title="Simple Langchain Chatbot with Groq",
    page_icon="🚀"
)

# Title
st.title("🚀 Simple Langchain Chatbot with Groq")
st.markdown("Learn LangChain basics with Groq's ultra-fast inference!")

# Sidebar
with st.sidebar:
    st.header("Settings")

    # API key input
    api_key = st.text_input(
        "Enter your Groq API Key",
        type="password",
        help="Get your API key from https://console.groq.com/keys"
    )

# Model Selection
model_name = st.selectbox(
    "Select Model",
    ["llama-3.1-8b-instant",
        "llama-3.3-70b-versatile",
        "gemma2-9b-it"],
    index=0
)

# Clear Conversation Button
if st.button("Clear Conversation"):
    st.session_state.messages = []
    st.rerun()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize LLM
@st.cache_resource
def get_chain(api_key, model_name):

    if not api_key:
        return None

    # Initialize Groq Model
    llm = ChatGroq(
        groq_api_key=api_key,
        model_name=model_name,
        temperature=0.7,
        streaming=True
    )

    # Prompt Template
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are a helpful AI assistant."
        ),
        ("user", "{question}")
    ])

    # Create Chain
    chain = prompt | llm | StrOutputParser()

    return chain

# Get chain
chain = get_chain(api_key, model_name)

if not chain:
    st.warning("Please enter your Groq API Key.")
    st.stop()

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
if question := st.chat_input("Ask me anything!"):

    # Add user message
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.write(question)

    # Assistant response
    with st.chat_message("assistant"):

        message_placeholder = st.empty()
        full_response = ""

        try:
            # Stream response
            for chunk in chain.stream({"question": question}):

                full_response += chunk

                message_placeholder.markdown(
                    full_response + "▌"
                )

            message_placeholder.markdown(full_response)

            # Save assistant response
            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": full_response
                }
            )

        except Exception as e:
            st.error(f"Error: {str(e)}")

# Examples
st.markdown("---")
st.markdown("### 💡 Try these examples:")

col1, col2 = st.columns(2)

with col1:
    st.markdown("- What is LangChain?")
    st.markdown("- Explain Groq's LPU technology")

with col2:
    st.markdown("- How do I learn programming?")
    st.markdown("- Write a haiku about AI")

# Footer
st.markdown("---")
st.markdown(
    "Built with LangChain & Groq | Experience the speed! ⚡"
)