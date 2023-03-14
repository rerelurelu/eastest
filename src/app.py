import streamlit as st

from utils.blank_line import blank_line

# Header
st.title('Eastest')
st.caption('指定された文字または文字列を使用して任意の桁数の文字列を生成できます。')

# Margin
for _ in range(5):
    blank_line()

# Generator section
st.subheader('テキスト生成')

col1, col2 = st.columns([3, 1], gap='medium')

with col1:
    st.text_input('original-text', placeholder='繰り返したい文字', label_visibility='hidden')

with col2:
    st.text_input('digits', placeholder='桁数', label_visibility='hidden')

_, col2 = st.columns([6, 0])

with col2:
    st.button('生成')
