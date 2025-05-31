import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Naloži podatke
csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../placa_utf8.csv"))
df = pd.read_csv(csv_path)
df["DATA"] = pd.to_numeric(df["DATA"], errors="coerce")

# Filtriraj osnovno
df = df[
    (df["PLAČA"] == "Bruto") &
    (df["MERITVE"] == "Povprečje") &
    (df["STATISTIČNA REGIJA"] != "SLOVENIJA")
].copy()

st.title("📍 Primerjava bruto plač med regijami skozi leta")

# Izberi spol in starost
spol = st.radio("Spol", ["Moški", "Ženske", "Spol - SKUPAJ"])
starost = st.selectbox("Starostna skupina", sorted(df["STAROST"].unique()))

# Filtriraj
filt = (df["SPOL"] == spol) & (df["STAROST"] == starost)
df_filtered = df[filt]

# Nariši graf
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(data=df_filtered, x="LETO", y="DATA", hue="STATISTIČNA REGIJA", marker="o", ax=ax)
ax.set_title(f"Bruto plače po regijah skozi čas ({spol}, {starost})")
ax.set_ylabel("Bruto plača (€)")
ax.set_xlabel("Leto")
ax.legend(title="Regija", bbox_to_anchor=(1.05, 1), loc='upper left')
st.pyplot(fig)
