import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Roshan Demo", page_icon="🌟", layout="centered")

st.title("ROSHAN I AM LIVE")
st.markdown("""
<div style="background-color:#222;color:#fff;padding:30px 15px;border-radius:16px;text-align:center;font-size:2rem;margin-bottom:32px;">
    🚀 <b>ROSHAN I AM LIVE</b> 🚀
</div>
""", unsafe_allow_html=True)

st.subheader("Here's a random sine curve for demo purposes:")

# Data for the graph
x = np.linspace(0, 20, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y, color='crimson', lw=3)
ax.set_title("Sine Wave", fontsize=18)
ax.set_xlabel("x")
ax.set_ylabel("sin(x)")
ax.grid(True, linestyle="dotted", color="gray", alpha=0.5)
st.pyplot(fig)

st.success("✅ Streamlit demo deployed successfully!")
st.info("Edit `app.py` to get started with your own app.")

if st.button("Show Data Table"):
    df = pd.DataFrame({'x': x, 'sin(x)': y})
    st.dataframe(df.head(10), use_container_width=True)
