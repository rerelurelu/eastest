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

st.button('生成')

# Margin
for _ in range(5):
    blank_line()

# Generated text section
st.subheader('生成済みテキスト')

st.text_area('', disabled=True, label_visibility='hidden')

col1, col2, _ = st.columns([1, 1, 5])

with col1:
    st.button('コピー')
with col2:
    st.button('削除')
