# 🌾 Smart Agri Advisor

**Smart Agri Advisor** is a modular, AI-powered multi-agent system designed to assist small-scale farmers in India. It provides personalized recommendations and real-time data to help with crucial farming decisions such as crop selection, fertilizer planning, market price analysis, and weather risk assessment.

Hosted API: [https://smart-agri-advisor.onrender.com/chat](https://smart-agri-advisor.onrender.com)

---

## 🧠 Project Goals

- ✅ Empower small farmers with real-time, intelligent farming advice.
- ✅ Reduce risk and improve yield through data-driven decisions.
- ✅ Modular and scalable system powered by AI agents.
- ✅ Easy integration via RESTful API.

---

## 🧩 Agents Implemented

### 1. 🌱 `crop_selector_agent`
- Recommends suitable crops based on location and season.

### 2. 🌾 `fertilizer_plan_agent`
- Suggests appropriate fertilizers based on crop and season.

### 3. 📈 `market_price_agent`
- Fetches **real-time market prices** through google-search for crops based on state and gives tips on when to sell, store, or wait.

### 4. ☁️ `weather_risk_agent`
- Provides weather forecasts and alerts farmers about risks like drought, rainfall, or storms.

---

## ⚙️ Technology Stack

- **Google Agent Development Kit (ADK)**
- **FastAPI** – for API development
- **Render.com** – for hosting backend APIs
- **LLM Models** – Gemini 2.0 Flash 
- **Streamlit** - for UI frontend 

---