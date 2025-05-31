import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
import numpy as np

st.title("Napoved povprečne bruto plače v Sloveniji (2023–2027)")

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

df_use = df[df["LETO"] >= 2015] if uporabi_recent else df

X = df_use["LETO"].values.reshape(-1, 1)
y = df_use["DATA"].values

if metoda == "Linearna regresija":
    model = LinearRegression()
elif metoda == "Polinomska regresija (stopnja 2)":
    model = make_pipeline(PolynomialFeatures(2), LinearRegression())

model.fit(X, y)

leta_napoved = np.arange(2023, 2028).reshape(-1, 1)
placa_napoved = model.predict(leta_napoved)

fig, ax = plt.subplots()
ax.plot(df["LETO"], df["DATA"], marker="o", label="Dejanske vrednosti")
ax.plot(leta_napoved.flatten(), placa_napoved, marker="o", linestyle="--", label="Napoved")
ax.set_title(f"Napoved povprečne bruto plače v Sloveniji (2023–2027)")
ax.set_xlabel("Leto")
ax.set_ylabel("Bruto plača (€)")
ax.legend()
ax.grid(True)
st.pyplot(fig)
