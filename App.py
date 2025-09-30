from socket import timeout
from dotenv import load_dotenv
load_dotenv()
import os
os.getenv("OPENAI_API_KEY")
from openai import OpenAI
import streamlit as st
import requests
import json

weather_api_key = os.getenv("WEATHER_API_KEY")
weather_base_url = os.getenv("WEATHER_BASE_URL")

#Create openAI client
client = OpenAI()

#Create UI using Streamlit
st.title("Weather Assistant")

#Weather tool
tools = [
    {
        "type":"function",
        "function":{
            "name":"get_weather_info",
            "description":"Give weather related information for city/state/country",
            "parameters": {
                "type":"object",
                "properties": {
                    "location":{
                        "type":"string",
                        "description":"This could be city, state or country like Mumbai, Maharashtra or India"
                    }
                },
                "required":["location"]
            }
        }
    }
]

#Function - get_weather_info
def get_weather_info(location):


    params = {
        "q":json.loads(location)["location"],
        "appid":weather_api_key,
        "units":"metrics"
    }
    weather_api_response = requests.get(weather_base_url,params=params,timeout=20)

    return weather_api_response.content.decode("utf-8")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    if not ("tool_calls" in message or message["role"] == "tool"):
        with st.chat_message(message["role"]) :
            st.markdown(message["content"])

if prompt := st.chat_input("What's up"):
    with st.chat_message("user"):
        st.markdown(prompt)


    user_input_message = {"role":"user", "content": prompt}
    st.session_state.messages.append(user_input_message)  

    #openAI call
    response = client.chat.completions.create(model = "gpt-4o-mini",
    messages=st.session_state.messages, tools=tools)

    
    if response.choices[0].message.tool_calls:
        tool_call_msg=response.choices[0].message
        st.session_state.messages.append({"role":tool_call_msg.role,"content": tool_call_msg.content, "tool_calls":tool_call_msg.tool_calls})
        for tool_call in response.choices[0].message.tool_calls:
            #tool_call = response.choices[0].message.tool_calls[0]
            function_name = tool_call.function.name
            arg = tool_call.function.arguments
            if function_name == "get_weather_info":
                result = get_weather_info(arg)
                st.session_state.messages.append({"role":"tool","tool_call_id":tool_call.id,"content":result})
        response=client.chat.completions.create(model="gpt-4o-mini",messages=st.session_state.messages)


    final_response = response.choices[0].message.content

    with st.chat_message("assistant"):
        st.markdown(final_response)

    st.session_state.messages.append({"role":"assistant", "content": final_response})