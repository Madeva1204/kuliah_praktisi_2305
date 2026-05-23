import streamlit as st

st.set_page_config(
  page_title="kuliah praktisi",
  layout="wide"
)

# Hirarki teks
st.title("📊 Dashboard")
st.header("Laporan Bulanan")
st.subheader("📈 Monthly Expenses")
st.caption("Made with ❤️ using Streamlit")

title = st.text_input("Movie title", "Life of Brian")
st.write("The current movie title is", title)

if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")
