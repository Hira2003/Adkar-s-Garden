import streamlit as st
import json
from datetime import datetime
import time

dikr = "  ربي إني لما انزلت إلي من خير فقير "
emo = ":butterfly:"
def load_adkar():
  """Loads adkar from adkar.json file."""
  with open("adkar.json", "r", encoding="utf-8") as f:
    adkar_data = json.load(f)
  return adkar_data["adkar"]

def display_adkar(adkar_list):
  """Displays each adkar as a label with button-like appearance, centered and with a custom font."""
  for adkar in adkar_list:
    st.markdown(f'<div style="color: black; background-color: #e3dbe5; padding: 10px; border-radius: 5px; cursor: pointer; margin-bottom: 10px; text-align: center; font-family: \'Arial\', sans-serif;">{adkar}</div>', unsafe_allow_html=True)

st.title("Adkar Garden :hibiscus: | :leaves: حديقة الذكر")
# Get the current date and time

# Format the date and time
#current_time = 

# Print the current date and time
c1,c2,c3 = st.columns(3)

with c2:
    st.image("icn.png")
    st.text("دعاء مميز لليوم")
    time_holder = st.empty()
    st.markdown(f'<div style="color: black; background-color: #d5b6dc; padding: 10px; border-radius: 5px; cursor: pointer; margin-bottom: 10px; text-align: center; font-family: \'Arial\', sans-serif;">{dikr}</div>', unsafe_allow_html=True)
adkar_list = load_adkar()
display_adkar(adkar_list)

while True:
    now = datetime.now()
    time_holder.text(now.strftime("%Y-%m-%d %H:%M:%S"))
    time.sleep(1)
    
    

