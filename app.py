import streamlit as st
import json
import os

# Load data from JSON
with open("results.json", "r") as f:
    data = json.load(f)

st.set_page_config(page_title="ShoeVision", layout="wide")

# --- UI HEADER ---
st.markdown("<h1 style='text-align: center; color: #E3EEB2;'>👟 ShoeVision</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px; color:gray;'>Your AI-powered footwear classifier with color detection</p>", unsafe_allow_html=True)
st.markdown("---")

# --- COLOR FILTER ---
st.subheader("🎨 What would be your color?")
color_input = st.color_picker("Pick a color", "#ffffff")
st.markdown("###")

# --- SHOE TYPE FILTER ---
st.subheader("👞 Will it be boots, sandals, or shoes?")
shoe_types = ["All", "Boot", "Sandal", "Shoe"]
selected_type = st.radio("Select shoe type:", shoe_types, horizontal=True)

# --- FILTER & DISPLAY IMAGES ---
def color_distance(c1, c2):
    return sum((a - b) ** 2 for a, b in zip(c1, c2)) ** 0.5

# Convert picked HEX color to RGB tuple
picked_rgb = tuple(int(color_input.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))

filtered_data = []

for item in data:
    # Calculate Euclidean distance between dominant color and picked color
    dist = color_distance(item["dominant_color"], picked_rgb)
    
    # Filter by shoe type and color distance threshold (tighter threshold)
    if (selected_type == "All" or item["predicted_class"].lower() == selected_type.lower()) and dist < 50:
        item["distance"] = dist  # Save distance for sorting
        filtered_data.append(item)

# Sort results by closest color match (lowest distance first)
filtered_data.sort(key=lambda x: x["distance"])

# Display filtered shoes in 3 columns
if filtered_data:
    cols = st.columns(3)
    for idx, item in enumerate(filtered_data):
        with cols[idx % 3]:
            st.image(
                item["image"],
                width=220,
                caption=f"{item['predicted_class']} | Color: {item['dominant_color']} | Match: {round(item['distance'], 1)}"
            )
else:
    st.info("No shoes match the selected filters. Try another color or type.")

