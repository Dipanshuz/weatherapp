
import streamlit as st
import requests

# --- CONFIG ---
API_KEY = "32882a8e5c93523066ececf9474b4be1"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# --- FUNCTION TO FETCH WEATHER ---
def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

# --- UI ---
st.set_page_config(page_title="Weather App", layout="centered")

st.title("🌤️ Weather App")

city = st.text_input("Enter city name")

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
