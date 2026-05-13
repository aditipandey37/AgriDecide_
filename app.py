#---------- PAGE CONFIG ----------

import streamlit as st
import time
import random
import pandas as pd

#---------- PAGE CONFIG ----------

st.set_page_config(
page_title="AgriDecide AI",
page_icon="🌾",
layout="centered"
)

#---------- SESSION ----------

if "page" not in st.session_state:
   st.session_state.page = 1

#---------- CUSTOM CSS ----------

st.markdown("""

""", unsafe_allow_html=True)

#---------- MAIN CONTAINER ----------

st.markdown('', unsafe_allow_html=True)

#---------- HEADER ----------

st.markdown('🌾 AgriDecide AI', unsafe_allow_html=True)

st.markdown(
'Smart AI Decision Support for Farmers',
unsafe_allow_html=True
)

#---------- PAGE 1 ----------

if st.session_state.page == 1:

   st.subheader("📥 Crop Input")

crop = st.text_input("Crop Name", "Wheat")

quantity = st.number_input(
    "Quantity (Quintals)",
    min_value=1,
    max_value=1000,
    value=50
)

mandi_price = random.randint(2000, 2400)

st.info(f"📡 Live Mandi Price: ₹{mandi_price}/quintal")

st.session_state.crop = crop
st.session_state.quantity = quantity
st.session_state.price = mandi_price

if st.button("🤖 Get AI Recommendation", use_container_width=True):

    with st.spinner("Analyzing market trends using AI..."):
        time.sleep(2)

    st.session_state.page = 2
    st.rerun()
#---------- PAGE 2 ----------

elif st.session_state.page == 2:

   st.subheader("🤖 AI Recommendation")

q = st.session_state.quantity
p = st.session_state.price

sell = q * p
process = q * (p + random.randint(450, 650))

st.markdown('<div class="card highlight">', unsafe_allow_html=True)

st.success("✅ Best Option: PROCESS")

st.write("### 📈 AI Confidence: 92%")

st.metric(
    label="Expected Extra Profit",
    value=f"₹{process - sell}"
)

st.write("### 📌 Reason")

st.write(
    "Processed products are currently in high demand "
    "with better market margins."
)

st.markdown('</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("⬅ Back", use_container_width=True):
        st.session_state.page = 1
        st.rerun()

with col2:
    if st.button("Next ➡", use_container_width=True):
        st.session_state.page = 3
        st.rerun()
---------- PAGE 3 ----------

elif st.session_state.page == 3:

st.subheader("📊 Profit Comparison")

q = st.session_state.quantity
p = st.session_state.price

sell = q * p
store = q * (p + 200)
process = q * (p + 500)

st.markdown('<div class="card">', unsafe_allow_html=True)

st.write(f"### 💰 Sell Directly: ₹{sell}")
st.write(f"### 🏬 Store & Sell Later: ₹{store}")
st.write(f"### 🏭 Process Crop: ₹{process}")

st.markdown('</div>', unsafe_allow_html=True)

chart_data = pd.DataFrame({
    "Strategy": ["Sell", "Store", "Process"],
    "Profit": [sell, store, process]
})

st.bar_chart(chart_data.set_index("Strategy"))

st.success(f"🚀 Additional Profit from Processing: ₹{process - sell}")

col1, col2 = st.columns(2)

with col1:
    if st.button("⬅ Back", use_container_width=True):
        st.session_state.page = 2
        st.rerun()

with col2:
    if st.button("Next ➡", use_container_width=True):
        st.session_state.page = 4
        st.rerun()
---------- PAGE 4 ----------

elif st.session_state.page == 4:

st.subheader("🏭 Nearby Processing Unit")

st.markdown('<div class="card">', unsafe_allow_html=True)

st.write("### 📍 Sharma Agro Processing Unit")
st.write("📏 Distance: 2 km")
st.write("🟢 Availability: Slots available")

st.markdown('</div>', unsafe_allow_html=True)

if st.button("✅ Confirm Booking", use_container_width=True):
    st.success("Booking Confirmed Successfully!")

if st.button("⬅ Back", use_container_width=True):
    st.session_state.page = 3
    st.rerun()
#---------- FOOTER ----------

st.markdown(
'Smart Farming Choose AgriDecide',
unsafe_allow_html=True
)

st.markdown('', unsafe_allow_html=True)
