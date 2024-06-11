import streamlit as st
from streamlit_extras.stateful_button import button
from utils import st_def, t_dsa

st.set_page_config(page_title='👋 AI',  page_icon="🚀",)
st.title('🔍 AI')
st_def.st_logo()
#------------------------------------------------------------------------------------------------
t1, t2 = st.tabs(["General", "AI DSA"])

with t1: t_dsa._general()
with t2: t_dsa._ai()

if button("Button 1", key="button1"):
    st.markdown("🚀) 🍨📄Rule Extraction📚: Python Libraries  Approaches📰🍨 ")

    if button("Button 2", key="button2"):
        st.image("./images/zhang.gif")

        if button("Button 3", key="button3"):
            st.write("All 3 buttons are pressed")


