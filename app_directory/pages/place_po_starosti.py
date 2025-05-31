import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.title("👥 Plače po starostnih skupinah in regijah")

base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../placa_utf8.csv"))
df = pd.read_csv(base_path)

df["DATA"] = pd.to_numeric(df["DATA"], errors="coerce")

starostne_skupine = ["15-24 let", "25-34 let", "35-44 let", "45-54 let", "55-64 let", "65 let ali več"]

leto = st.slider("Izberi leto", 2015, 2022, 2022)

df_filtered = df[
    (df["LETO"] == leto) &
    (df["PLAČA"] == "Bruto") &
    (df["MERITVE"] == "Povprečje") &
    (df["SPOL"] == "Spol - SKUPAJ") &
    (df["STATISTIČNA REGIJA"] != "SLOVENIJA") &
    (df["STAROST"].isin(starostne_skupine))
]

regija_avg = df_filtered.groupby("STATISTIČNA REGIJA")["DATA"].mean().sort_values(ascending=False)
df_filtered["STATISTIČNA REGIJA"] = pd.Categorical(df_filtered["STATISTIČNA REGIJA"], categories=regija_avg.index, ordered=True)

fig, ax = plt.subplots(figsize=(14, 6))
sns.barplot(data=df_filtered, x="STATISTIČNA REGIJA", y="DATA", hue="STAROST", ax=ax)
plt.xticks(rotation=45)
plt.ylabel("Bruto plača (€)")
plt.title(f"Povprečne bruto plače po regijah ({leto})")
st.pyplot(fig)
