import streamlit as st
import pandas as pd
import requests

# --- CONFIG ---
API_KEY = ""
BASE_URL = ""

# --- FUNCTION TO FETCH WEATHER ---
def get_weather(city):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=8f5bf33f00eeb712ed2b6687ee18eee3&units=metric')
    return response.json()

# --- UI ---
st.set_page_config(page_title="Weather App", layout="centered")

st.title("🌤️ Weather App")

df = pd.read_csv("data/demographics.csv")
city = st.selectbox("Select an Indian City :", df['city'], placeholder='Cities', index=None)

if st.button("Get Weather"):
    if city:
        data = get_weather(city)

        if data.get("cod") != 200:
            st.error("City not found")
        else:
            # Extract data
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            weather_desc = data["weather"][0]["description"]
            wind_speed = data["wind"]["speed"]

            # Display
            st.subheader(f"Weather in {city}")
            st.write(f"🌡 Temperature: {temp} °C")
            st.write(f"💧 Humidity: {humidity}%")
            st.write(f"🌬 Wind Speed: {wind_speed} m/s")
            st.write(f"☁ Condition: {weather_desc}")

    else:
        st.warning("Please enter a city name")
