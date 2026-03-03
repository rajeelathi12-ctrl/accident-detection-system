import streamlit as st
import pandas as pd
from datetime import datetime
import math
import random

st.title("🚨 AI-Based Accident Detection & Ambulance System")

# -----------------------------
# Function: Detect Accident
# -----------------------------
def detect_accident(speed, impact):
    if speed > 60 and impact:
        return True
    return False

# -----------------------------
# Function: Get Location (Salem Random)
# -----------------------------
def get_location():
    lat = random.uniform(11.60, 11.70)
    lon = random.uniform(78.10, 78.20)
    return lat, lon

# -----------------------------
# Function: Calculate Distance
# -----------------------------
def calculate_distance(lat1, lon1, lat2, lon2):
    return math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)

# -----------------------------
# Ambulance & Hospital Data
# -----------------------------
ambulances = [
    ("Ambulance 1", 11.6643, 78.1460),
    ("Ambulance 2", 11.6700, 78.1500),
    ("Ambulance 3", 11.6550, 78.1350),
]

hospitals = [
    ("Hospital A", 11.6680, 78.1470),
    ("Hospital B", 11.6600, 78.1400),
]

# -----------------------------
# Button Click
# -----------------------------
if st.button("Simulate Accident"):

    speed = 80
    impact = True

    if detect_accident(speed, impact):

        st.success("🚨 Accident Detected")

        # Severity Level
        if speed > 100:
            st.error("🔴 Severe Accident")
        elif speed > 60:
            st.warning("🟠 Moderate Accident")
        else:
            st.info("🟢 Minor Accident")

        # Time
        current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        st.info(f"⏰ Accident Time: {current_time}")

        # Location
        lat, lon = get_location()
        st.subheader("📍 Accident Location (Salem)")
        st.map(pd.DataFrame({"lat":[lat], "lon":[lon]}))

        # Find Nearest Ambulance
        nearest_amb = min(
            ambulances,
            key=lambda amb: calculate_distance(lat, lon, amb[1], amb[2])
        )

        # Find Nearest Hospital
        nearest_hosp = min(
            hospitals,
            key=lambda hosp: calculate_distance(lat, lon, hosp[1], hosp[2])
        )

        st.success(f"🚑 Assigned Ambulance: {nearest_amb[0]}")
        st.success(f"🏥 Nearest Hospital: {nearest_hosp[0]}")
        st.info("📢 Alert sent successfully!")

    else:
        st.info("No accident detected")