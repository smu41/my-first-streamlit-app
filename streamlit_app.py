import streamlit as st

st.header('st.button')

if st.button('Say Hello'):
  st.write('Why hello here!!')
else:
  st.write('Goodbye!')
