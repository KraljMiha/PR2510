import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("placa_utf8.csv")

df["LETO"] = pd.to_numeric(df["LETO"], errors="coerce")
df["DATA"] = pd.to_numeric(df["DATA"], errors="coerce")
df = df.dropna(subset=["LETO", "DATA"])

meritve = ["10. percentil", "90. percentil", "99. percentil", "Mediana", "Povprečje"]
df = df[
    (df["PLAČA"] == "Neto") &
    (df["MERITVE"].isin(meritve))
]

st.title("📊 Analiza plačnih percentilov skozi čas")

regija = st.selectbox("Izberi regijo:", sorted(df["STATISTIČNA REGIJA"].unique()))
starost = st.selectbox("Izberi starostno skupino:", sorted(df["STAROST"].unique()))

filtered = df[
    (df["STATISTIČNA REGIJA"] == regija) &
    (df["STAROST"] == starost) &
    (df["SPOL"] == "Spol - SKUPAJ")
].copy()

pivot_df = filtered.pivot_table(index="LETO", columns="MERITVE", values="DATA").sort_index()

growth_df = pivot_df.pct_change() * 100
growth_df = growth_df.round(2)

st.subheader("📈 Vrednosti po letih")
fig, ax = plt.subplots(figsize=(10, 6))
for col in pivot_df.columns:
    ax.plot(pivot_df.index, pivot_df[col], marker="o", label=col)
ax.set_title(f"Neto plače po statističnih vrednostih ({regija}, {starost})")
ax.set_xlabel("Leto")
ax.set_ylabel("Znesek (€)")
ax.grid(True, linestyle="--", alpha=0.6)
ax.legend()
st.pyplot(fig)

st.subheader("📊 Letna sprememba (%)")
st.dataframe(growth_df.style.format("{:.2f} %").highlight_max(axis=0, color='lightgreen').highlight_min(axis=0, color='salmon'))
