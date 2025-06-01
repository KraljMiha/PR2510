# Napoved plač

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
import numpy as np

st.title("📈 Napoved povprečne bruto plače v Sloveniji (2023–2027)")

st.markdown("""
To orodje omogoča **napoved gibanja povprečne bruto plače** v Sloveniji za obdobje **2023–2027**.
Napoved temelji na zgodovinskih podatkih Statističnega urada RS in uporablja **linearne ali polinomske regresijske modele**.

🛠️ Uporabnik lahko izbere:
- **metodo napovedi** (linearna ali polinomska),
- ali se uporabi celoten zgodovinski nabor ali le zadnjih 7 let.

Rezultat je graf, ki prikazuje:
- dejanske zgodovinske podatke,
- izbrano napoved za prihodnja leta.
""")

df = pd.read_csv("placa_utf8.csv")
df = df[
    (df["STATISTIČNA REGIJA"] == "SLOVENIJA") &
    (df["PLAČA"] == "Bruto") &
    (df["MERITVE"] == "Povprečje") &
    (df["STAROST"] == "Starost - SKUPAJ") &
    (df["SPOL"] == "Spol - SKUPAJ")
].copy()

df["DATA"] = pd.to_numeric(df["DATA"], errors="coerce")
df = df.dropna(subset=["DATA"])
df = df.sort_values("LETO")

metoda = st.selectbox("Izberi metodo napovedi:", ["Linearna regresija", "Polinomska regresija (stopnja 2)"])
uporabi_recent = st.checkbox("Uporabi samo zadnjih 7 let (od 2015 dalje)", value=True)

if metoda == "Linearna regresija" and not uporabi_recent:
    st.warning("⚠️ Linearna regresija na vseh letih morda ni najbolj primerna, ker zgodnji podatki izkrivljajo zadnje trende. Bolj je uporabinh zadnjih 7 let ali polinomska metoda.")

df_use = df[df["LETO"] >= 2015] if uporabi_recent else df
X = df_use["LETO"].values.reshape(-1, 1)
y = df_use["DATA"].values

if metoda == "Linearna regresija":
    model = LinearRegression()
else:
    model = make_pipeline(PolynomialFeatures(2), LinearRegression())

model.fit(X, y)

leta_napoved = np.arange(2023, 2028).reshape(-1, 1)
placa_napoved = model.predict(leta_napoved)

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df["LETO"], df["DATA"], marker="o", color="blue", label="Dejanske vrednosti")
ax.plot(leta_napoved.flatten(), placa_napoved, marker="o", linestyle="--", color="red", label="Napoved")

for leto, vrednost in zip(leta_napoved.flatten(), placa_napoved):
    ax.text(leto, vrednost - 50, f"{vrednost:.0f}€", ha='center', va='top', fontsize=10, color='red')

ax.set_title("Napoved povprečne bruto plače v Sloveniji (2023–2027)", fontsize=14)
ax.set_xlabel("Leto", fontsize=12)
ax.set_ylabel("Bruto plača (€)", fontsize=12)
ax.legend(fontsize=11)
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_xticks(np.arange(min(df["LETO"]), 2028, 1))
plt.tight_layout()

st.pyplot(fig)
