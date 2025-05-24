import pandas as pd
import streamlit as st

df = pd.read_csv("data/muscle_fiber_data.csv")

st.title("MyoMap: Mouse Muscle Fiber Atlas")
st.write("Explore slow and fast-twitch fiber types in mouse muscles")

selected_muscle = st.selectbox("Select a muscle", df["Muscle"].unique())
filtered = df[df["Muscle"] == selected_muscle]

st.bar_chart(data=filtered, x="FiberType", y="Percentage")
