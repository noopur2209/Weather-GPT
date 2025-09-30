# 🌦️ Weather-GPT

A conversational **AI-powered weather assistant** built with **Streamlit**, **OpenAI’s Chat Completions API (with tool calling)**, and the **OpenWeatherMap API**.  
The app lets you chat naturally and get real-time weather updates for any city, state, or country.  

---

## ✨ Features
- 💬 Chat with an AI assistant in a simple Streamlit UI  
- 🔗 Uses **OpenAI tool calling** to fetch real-time weather data  
- 🌍 Powered by the **OpenWeatherMap API**  
- 📝 Maintains conversation history using `st.session_state`  
- ⚡ Lightweight and easy to run locally  

---

## 🛠️ Tech Stack
- [Python](https://www.python.org/)  
- [Streamlit](https://streamlit.io/) – for the web UI  
- [OpenAI](https://platform.openai.com/) – for natural language and tool calling  
- [OpenWeatherMap](https://openweathermap.org/api) – for weather data  

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/weather-assistant.git
cd weather-assistant
```
### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Add Environment Variables
```bash
OPENAI_API_KEY=your_openai_api_key_here
WEATHER_API_KEY=your_openweathermap_api_key_here
WEATHER_BASE_URL=https://api.openweathermap.org/data/2.5/weather
```
### 5. Run the App
```bash
streamlit run app.py
```
## 🖼️ Demo

When you run the app, you’ll see a chat interface.
Examples of queries:

- “What’s the weather in Mumbai?”

- “Is it raining in New York?”

- “Give me the forecast for London.”

## 📂 Project Structure
```bash
.
├── app.py              # Main Streamlit app
├── requirements.txt    # Python dependencies
├── .env                # API keys (not committed to GitHub)
└── README.md           # Project documentation
```
## 🚀 Future Enhancements

 - Add support for 5-day forecast

 - Detect user’s location automatically via IP/geo

 - Add temperature unit selection (Celsius/Fahrenheit)

 - Deploy on Streamlit Cloud or Docker
