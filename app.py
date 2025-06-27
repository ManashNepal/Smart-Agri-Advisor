import streamlit as st
import requests

st.set_page_config(page_title="Smart Agri Advisor", page_icon=":corn:")

st.title("Smart Agri Advisor :potted_plant:")

st.write(
    "> Empowering farmers and agri-enthusiasts with personalized insights, smart recommendations, and up-to-date market intelligence.  \n"
    "> *Grow smarter, harvest better—your digital companion for modern agriculture.*"
)

user_choice = st.selectbox(label="Pick a service", options=["None", "Crop Selection", "Fertilizer Planning", "Weather Risk Assessment", "Market Price Assessment"])

if user_choice == "Crop Selection":
    st.subheader("Select state and season")
    state = st.selectbox(
        label="Where are you from?", 
        options=[
        'Assam', 'Karnataka', 'Kerala', 'Meghalaya', 'West Bengal',
        'Puducherry', 'Goa', 'Andhra Pradesh', 'Tamil Nadu', 'Odisha',
        'Bihar', 'Gujarat', 'Madhya Pradesh', 'Maharashtra', 'Mizoram',
        'Punjab', 'Uttar Pradesh', 'Haryana', 'Himachal Pradesh',
        'Tripura', 'Nagaland', 'Chhattisgarh', 'Uttarakhand', 'Jharkhand',
        'Delhi', 'Manipur', 'Jammu and Kashmir', 'Telangana',
        'Arunachal Pradesh', 'Sikkim'
        ]
    )

    season = st.selectbox(
        label="Pick a season",
        options=[
        'Whole Year', 'Kharif', 'Rabi', 'Autumn',
        'Summer', 'Winter'
        ]
    )

    if st.button(label="Generate",key="crop_select_button"):
        with st.spinner("Generating..."):
            response = requests.post(
                "https://smart-agri-advisor.onrender.com/chat",
                json={
                    "user_input": f"I am from {state}. Can you suggest me some crops I can plant in {season} season.",
                    "agent_name": "crop_selector_agent"
                }
            )

            if response.status_code == 200:
                data = response.json()
                agent_output = data["response"]
            else:
                agent_output = f"API error: {response.status_code}"
            
            st.subheader("Crop Suggestion:", divider=True)
            st.write(agent_output)

elif user_choice == "Fertilizer Planning":
    st.subheader("Select state and season")
    crop = st.selectbox(
        label="Pick a crop", 
        options=[
        'Arecanut', 'Arhar/Tur', 'Castor seed', 'Coconut ', 'Cotton(lint)',
        'Dry chillies', 'Gram', 'Jute', 'Linseed', 'Maize', 'Mesta',
        'Niger seed', 'Onion', 'Osther  Rabi pulses', 'Potato',
        'Rapeseed &Mustard', 'Rice', 'Sesamum', 'Small millets',
        'Sugarcane', 'Sweet potato', 'Tapioca', 'Tobacco', 'Turmeric',
        'Wheat', 'Bajra', 'Black pepper', 'Cardamom', 'Coriander',
        'Garlic', 'Ginger', 'Groundnut', 'Horse-gram', 'Jowar', 'Ragi',
        'Cashewnut', 'Banana', 'Soyabean', 'Barley', 'Khesari', 'Masoor',
        'Moong(Green Gram)', 'Other Kharif pulses', 'Safflower',
        'Sannhamp', 'Sunflower', 'Urad', 'Peas & beans (Pulses)',
        'other oilseeds', 'Other Cereals', 'Cowpea(Lobia)',
        'Oilseeds total', 'Guar seed', 'Other Summer Pulses', 'Moth'
        ]
    )

    season = st.selectbox(
        label="Pick a season",
        options=[
        'Whole Year', 'Kharif', 'Rabi', 'Autumn',
        'Summer', 'Winter'
        ]
    )

    if st.button(label="Generate",key="fertilizer_plan_button"):
        with st.spinner("Generating..."):
            response = requests.post(
                "https://smart-agri-advisor.onrender.com/chat",
                json={
                    "user_input": f"Can you suggest some fertilizer planning for the crop: {crop} in the season: {season}.",
                    "agent_name": "fertilizer_plan_agent"
                }
            )

            if response.status_code == 200:
                data = response.json()
                agent_output = data["response"]
            else:
                agent_output = f"API error: {response.status_code}"

            st.subheader("Ferilizer Suggestion:", divider=True)
            st.write(agent_output)

elif user_choice == "Weather Risk Assessment":
    state = st.selectbox(
        label="Where are you from?", 
        options=[
        'Assam', 'Karnataka', 'Kerala', 'Meghalaya', 'West Bengal',
        'Puducherry', 'Goa', 'Andhra Pradesh', 'Tamil Nadu', 'Odisha',
        'Bihar', 'Gujarat', 'Madhya Pradesh', 'Maharashtra', 'Mizoram',
        'Punjab', 'Uttar Pradesh', 'Haryana', 'Himachal Pradesh',
        'Tripura', 'Nagaland', 'Chhattisgarh', 'Uttarakhand', 'Jharkhand',
        'Delhi', 'Manipur', 'Jammu and Kashmir', 'Telangana',
        'Arunachal Pradesh', 'Sikkim'
        ]
    )
    if st.button(label="Generate",key="weather_risk_button"):
        with st.spinner("Generating..."):
            response = requests.post(
                url="https://smart-agri-advisor.onrender.com/chat",
                json={
                    "user_input": f"I am from {state}. Can you suggest if I can do plantation at the moment considering the weather?",
                    "agent_name": "weather_risk_agent"
                }
            )

            if response.status_code == 200:
                data = response.json()
                agent_output = data["response"]
            else:
                agent_output = f"API error: {response.status_code}"            

            st.subheader("Weather-based Suggestion:", divider=True)
            st.write(agent_output)

elif user_choice == "Market Price Assessment":
    state = st.selectbox(
        label="Where are you from?", 
        options=[
        'Assam', 'Karnataka', 'Kerala', 'Meghalaya', 'West Bengal',
        'Puducherry', 'Goa', 'Andhra Pradesh', 'Tamil Nadu', 'Odisha',
        'Bihar', 'Gujarat', 'Madhya Pradesh', 'Maharashtra', 'Mizoram',
        'Punjab', 'Uttar Pradesh', 'Haryana', 'Himachal Pradesh',
        'Tripura', 'Nagaland', 'Chhattisgarh', 'Uttarakhand', 'Jharkhand',
        'Delhi', 'Manipur', 'Jammu and Kashmir', 'Telangana',
        'Arunachal Pradesh', 'Sikkim'
        ]
    )

    crop = st.selectbox(
        label="Pick a crop", 
        options=[
        'Arecanut', 'Arhar/Tur', 'Castor seed', 'Coconut ', 'Cotton(lint)',
        'Dry chillies', 'Gram', 'Jute', 'Linseed', 'Maize', 'Mesta',
        'Niger seed', 'Onion', 'Osther  Rabi pulses', 'Potato',
        'Rapeseed &Mustard', 'Rice', 'Sesamum', 'Small millets',
        'Sugarcane', 'Sweet potato', 'Tapioca', 'Tobacco', 'Turmeric',
        'Wheat', 'Bajra', 'Black pepper', 'Cardamom', 'Coriander',
        'Garlic', 'Ginger', 'Groundnut', 'Horse-gram', 'Jowar', 'Ragi',
        'Cashewnut', 'Banana', 'Soyabean', 'Barley', 'Khesari', 'Masoor',
        'Moong(Green Gram)', 'Other Kharif pulses', 'Safflower',
        'Sannhamp', 'Sunflower', 'Urad', 'Peas & beans (Pulses)',
        'other oilseeds', 'Other Cereals', 'Cowpea(Lobia)',
        'Oilseeds total', 'Guar seed', 'Other Summer Pulses', 'Moth'
        ]
    )

    if st.button(label="Generate",key="market_price_button"):
        with st.spinner("Generating..."):
            response = requests.post(
                url="https://smart-agri-advisor.onrender.com/chat",
                json={
                    "user_input": f"The state is {state} and the crop is {crop}.",
                    "agent_name": "market_price_agent"
                }
            )

            if response.status_code == 200:
                data = response.json()
                agent_output = data["response"]
            else:
                agent_output = f"API error: {response.status_code}"            

            st.subheader("Market-based Suggestion:", divider=True)
            st.write(agent_output)
