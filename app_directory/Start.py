import streamlit as st

st.title("Interaktivna analiza plač v Sloveniji")
st.markdown("""
Dobrodošli v aplikaciji, kjer si lahko interaktivno ogledate:
- bruto plače po regijah in starostnih skupinah
- razliko med spoloma
- trende skozi čas

Uporabite meni na levi za izbiro posamezne analize.
""")
name = st.text_input("Vnesi svoje ime:")
if name:
    st.write(f"Pozdravljen, {name}! 👋 Dobrodošel v analizi slovenskih plač.")

