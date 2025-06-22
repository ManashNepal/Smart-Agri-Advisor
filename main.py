from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
import asyncio
from dotenv import load_dotenv 
from uuid import uuid4
from agents.crop_selector_agent.agent import crop_selector_agent
from agents.weather_risk_agent.agent import weather_risk_agent
from google.genai import types

load_dotenv()

APP_NAME = "Smart Agri Advisor"
SESSION_ID = str(uuid4())
USER_ID = "manash_nepal10"

async def main():
    session_service = InMemorySessionService()

    session = session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID
    )

    print("===SESSION CREATED===")
    print(f"Session ID: {SESSION_ID}")

    runner = Runner(
        app_name=APP_NAME,
        agent = weather_risk_agent,
        session_service=session_service
    )

    while True:
        user_input = input("You: ")

        if "exit" in user_input.lower():
            break 
            
            

        user_message = types.Content(
            role="user",
            parts=[types.Part(text=user_input)]
        )

        for event in runner.run(user_id=USER_ID, session_id=SESSION_ID, new_message=user_message):
            if event.is_final_response():
                if event.content and event.content.parts:
                    print(f"Agent: {event.content.parts[0].text}")
                    

asyncio.run(main())


