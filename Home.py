import streamlit as st

st.set_page_config(
    page_title="Road Damage Detections Apps",
    page_icon="🛣️",
)


st.divider()
st.title("antiBAD - road damage detector")

st.markdown(
    """
    There is four types of damage that this model can detects such as:
    - Longitudinal Crack
    - Transverse Crack
    - Alligator Crack
    - Potholes


    You can select the apps from the sidebar to try and experiment with any kind of input **(realtime-webcam, video and images)** depends on your use case.

    
"""
)

st.divider()



