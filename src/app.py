from typing import List

import streamlit as st

from functions.generate_text import generate_text
from models.model import Text
from utils.blank_line import blank_line
from utils.check_inputs import check_inputs

# Variables
if 'generated_texts' not in st.session_state:
    st.session_state.generated_texts: List[Text] = []

# Header
st.title('Eastest')
st.caption('指定された文字または文字列を使用して任意の桁数の文字列を生成できます。')

# Margin
for _ in range(5):
    blank_line()

# Generator section
st.subheader('テキスト生成')

col1, col2, col3 = st.columns([2, 3, 1], gap='medium')

with col1:
    input_label = st.text_input('ラベル', placeholder='半角英数字')
with col2:
    input_text = st.text_input('繰り返したい文字', value='埼玉県春日部市', placeholder='埼玉県春日部市')
with col3:
    input_digits = st.text_input('桁数', value=100, placeholder='10')


if st.button('生成'):
    with st.spinner('生成中...'):
        try:
            check_inputs(input_text, input_digits)
            digits = int(input_digits)

            if input_label:
                label = input_label + ': ' + input_digits
            else:
                label = input_digits
            label += '桁'

            st.session_state.generated_texts.append(
                Text(
                    label=label,
                    generated_text=generate_text(input_text, digits),
                )
            )
        except ValueError:
            st.error('桁数には数字を入力してください。')
        except Exception as e:
            st.error(e)


# Margin
for _ in range(5):
    blank_line()

# Generated text section
st.subheader('生成済みテキスト')

if (list_length := len(st.session_state.generated_texts)) > 0:
    for i in range(list_length):
        blank_line()
        st.text_area(
            label=st.session_state.generated_texts[i].label,
            value=st.session_state.generated_texts[i].generated_text,
            disabled=True,
            height=160,
            key=f'textarea-{i}',
        )

        col1, col2, _ = st.columns([1, 1, 5])

        with col1:
            st.button('コピー', key=f'copy-button-{i}')
        with col2:
            st.button('削除', key=f'delete-button-{i}')
else:
    st.caption('生成済みのテキストはありません。')
