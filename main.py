from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from dotenv import load_dotenv 
from uuid import uuid4
from agents.crop_selector_agent.agent import crop_selector_agent
from agents.weather_risk_agent.agent import weather_risk_agent
from agents.crop_selector_agent.agent import crop_selector_agent
from agents.fertilizer_plan_agent.agent import fertilizer_plan_agent
from agents.weather_risk_agent.agent import weather_risk_agent
from google.genai import types
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

load_dotenv()

class InputFormat(BaseModel):
    user_input : str
    agent_name : str

APP_NAME = "Smart Agri Advisor"
SESSION_ID = str(uuid4())
USER_ID = "manash_nepal10"

@app.post("/chat")
async def generate_content(data : InputFormat):
    session_service = InMemorySessionService()



    if data.agent_name == "crop_selector_agent":
        agent = crop_selector_agent
    elif data.agent_name == "fertilizer_plan_agent":
        agent = fertilizer_plan_agent
    elif data.agent_name == "weather_risk_agent":
        agent = weather_risk_agent

    await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID
    )

    runner = Runner(
        app_name=APP_NAME,
        agent = agent,
        session_service=session_service
    )

    while True:
        user_input = data.user_input

        if "exit" in user_input.lower():
            break 
            
            

        user_message = types.Content(
            role="user",
            parts=[types.Part(text=user_input)]
        )

        agent_output = ""
        for event in runner.run(user_id=USER_ID, session_id=SESSION_ID, new_message=user_message):
            if event.is_final_response():
                if event.content and event.content.parts:
                    agent_output = event.content.parts[0].text
        
        return {
            "response" : agent_output
        }
                    



