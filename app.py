import streamlit as st
from words import words

st.title("Kelime Öğrenme Modu")

# ----------------------------
# Başlangıç değerleri
# ----------------------------
if "current_index" not in st.session_state:
    st.session_state.current_index = 0

if "show_meaning" not in st.session_state:
    st.session_state.show_meaning = False

if "show_association" not in st.session_state:
    st.session_state.show_association = False

# ----------------------------
# Mevcut kelime
# ----------------------------
current_index = st.session_state.current_index
selected = words[current_index]

# ----------------------------
# İlerleme çubuğu
# ----------------------------
progress = (current_index + 1) / len(words)
st.progress(progress)

st.write(f"{current_index + 1} / {len(words)} kelime")

# ----------------------------
# Kelime göster
# ----------------------------
st.header(selected["word"])

# Anlam göster
if st.button("Anlamı Göster"):
    st.session_state.show_meaning = True

if st.session_state.show_meaning:
    st.write("Anlam:", selected["meaning"])

# Çağrışım göster
if st.button("Çağrışımı Göster"):
    st.session_state.show_association = True

if st.session_state.show_association:
    st.write("Çağrışım:", selected["association"])

# ----------------------------
# Sonraki kelime
# ----------------------------
if st.button("Sonraki Kelime"):
    st.session_state.current_index += 1

    # Liste bitince başa dön
    if st.session_state.current_index >= len(words):
        st.session_state.current_index = 0

    st.session_state.show_meaning = False
    st.session_state.show_association = False

    st.rerun()