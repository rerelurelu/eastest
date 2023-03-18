TEST_DATA = [
    # 入力文字数より桁数が少ない場合
    {
        'input_digits': 3,
        'input_text': 'name',
        'generated_text': 'nam',
    },
    # 入力文字数より桁数が多い場合
    {
        'input_digits': 10,
        'input_text': 'name',
        'generated_text': 'namenamena',
    },
    # 入力文字数と桁数が等しい場合
    {
        'input_digits': 7,
        'input_text': 'address',
        'generated_text': 'address',
    },
    # 入力文字が全角文字の場合
    {
        'input_digits': 10,
        'input_text': 'Ａ１％',
        'generated_text': 'Ａ１％Ａ１％Ａ１％Ａ',
    },
    # 入力文字が半角文字の場合
    {
        'input_digits': 10,
        'input_text': 'Aa1%',
        'generated_text': 'Aa1%Aa1%Aa',
    },
    # 入力文字に全角文字と半角文字が混ざっている場合
    {
        'input_digits': 10,
        'input_text': 'ＡB１2％%',
        'generated_text': 'ＡB１2％%ＡB１2',
    },
    # 入力文字に漢字が含まれる場合
    {
        'input_digits': 10,
        'input_text': '東京都港区',
        'generated_text': '東京都港区東京都港区',
    },
    # 入力文字にスペースが含まれる場合
    {
        'input_digits': 20,
        'input_text': '東京都港区赤坂 赤坂マンション　101',
        'generated_text': '東京都港区赤坂 赤坂マンション　101東',
    },
]
