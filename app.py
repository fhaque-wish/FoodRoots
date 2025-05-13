import streamlit as st
import openai
import os

# Title and Description
st.title("🍜 Food Lineage Explorer")
st.write("Discover the ancestry and evolution of your favorite foods. Enter a modern food name, and our AI will trace its historical and cultural journey.")

# Input food name
food_name = st.text_input("Enter a modern food name (e.g., 'Ramen', 'Pizza')")

# OpenAI API Key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Function to call GPT-4o
@st.cache_data(show_spinner=False)
def get_food_lineage(food):
    prompt = f"""
    Trace the historical evolution and cultural lineage of the dish \"{food}\".
    Include its ancient origins, key transformation points, regional variants, and how it became today's version.
    Present the output in a chronological format, optionally suggesting a lineage diagram in text.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=1000
    )
    return response['choices'][0]['message']['content']

# Trigger API call
if st.button("Trace Lineage") and food_name:
    with st.spinner("Consulting culinary history archives..."):
        try:
            lineage = get_food_lineage(food_name)
            st.markdown("### 🍽️ Food Lineage Result")
            st.markdown(lineage)
        except Exception as e:
            st.error(f"Error: {e}")

# Optional: Image upload section for future enhancement
st.markdown("---")
st.markdown("### 📷 Coming Soon: Image-based Food Recognition")
uploaded_file = st.file_uploader("Upload a food image to auto-detect its lineage (not yet implemented)", type=["jpg", "jpeg", "png"])
if uploaded_file:
    st.info("Image uploaded. Stay tuned for image recognition in the next update!")

