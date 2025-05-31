import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.title("♀️♂️ Spolne razlike po regijah")
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../placa_utf8.csv"))
df = pd.read_csv(base_path)
df["DATA"] = pd.to_numeric(df["DATA"], errors="coerce")

leto = st.selectbox("Izberi leto", sorted(df["LETO"].unique(), reverse=True))

df_spol = df[
    (df["LETO"] == leto) &
    (df["PLAČA"] == "Bruto") &
    (df["MERITVE"] == "Povprečje") &
    (df["STAROST"] == "Starost - SKUPAJ") &
    (df["STATISTIČNA REGIJA"] != "SLOVENIJA") &
    (df["SPOL"].isin(["Moški", "Ženske"]))
]

pivot = df_spol.pivot_table(index="STATISTIČNA REGIJA", columns="SPOL", values="DATA").dropna()
pivot["RAZLIKA (%)"] = ((pivot["Moški"] - pivot["Ženske"]) / pivot["Ženske"]) * 100

fig, ax = plt.subplots(figsize=(10, 5))
pivot = pivot.sort_values("RAZLIKA (%)", ascending=False)
sns.barplot(x=pivot.index, y=pivot["RAZLIKA (%)"], color="salmon", ax=ax)
plt.xticks(rotation=45)
plt.title(f"Spolna razlika v bruto plačah po regijah ({leto})")
plt.ylabel("Razlika (%)")
st.pyplot(fig)
