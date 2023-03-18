import csv
import time
from typing import List

import pyperclip
import streamlit as st

from models.model import Text
from utils.blank_line import blank_line
from utils.check_inputs import check_inputs
from utils.generate_text import generate_text

# Variables
success_message = None
if 'disable_submit' not in st.session_state:
    st.session_state.disable_submit = True
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

manual_tab, auto_tab = st.tabs(['自分で生成', 'ファイルから自動生成'])

with manual_tab:
    with st.form('input-text'):
        label_col, text_col, digits_col = st.columns([2, 3, 1], gap='medium')
        with label_col:
            input_label = st.text_input('ラベル', placeholder='半角英数字')
        with text_col:
            input_text = st.text_input('繰り返したい文字', value='', placeholder='埼玉県春日部市')
        with digits_col:
            input_digits = st.text_input('桁数', value='', placeholder='10')

        generate_button = st.form_submit_button('テキストを生成')

        if generate_button:
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
                    success_message = st.success('生成完了🎉')
                except ValueError:
                    st.error('桁数には数字を入力してください。')
                except Exception as e:
                    st.error(e)
with auto_tab:
    with st.form('upload-csv'):
        uploaded_file = st.file_uploader('CSVファイルをアップロード', type='csv')
        upload_button = st.form_submit_button("テキストを生成")
        if upload_button:
            try:
                with st.spinner('生成中...'):
                    file_contents = uploaded_file.getvalue().decode("utf-8").splitlines()
                    reader = csv.reader(file_contents)

                    for row in reader:
                        st.session_state.generated_texts.append(
                            Text(
                                label=row[0],
                                generated_text=row[1],
                            )
                        )
                    success_message = st.success('生成完了🎉')
            except AttributeError:
                st.error('CSVファイルをアップロードしてください🙇‍♂️')

# Margin
for _ in range(5):
    blank_line()

# Generated text section
st.subheader('生成済みテキスト')

if (list_length := len(st.session_state.generated_texts)) > 0:
    export_button = st.button('CSVファイルをエクスポート')

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
            copy_button, copy_index = st.button('コピー', key=f'copy-button-{i}'), i

            if copy_button:
                pyperclip.copy(st.session_state.generated_texts[copy_index].generated_text)
        with col2:
            delete_button, delete_index = st.button('削除', key=f'delete-button-{i}'), i

            if delete_button:
                del st.session_state.generated_texts[delete_index]
                st.experimental_rerun()
    if success_message:
        time.sleep(3)
        success_message.empty()
else:
    st.caption('生成済みのテキストはありません。')
