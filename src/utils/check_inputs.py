def check_inputs(text: str, digits: str) -> None:
    if not text and not digits:
        raise Exception('繰り返したい文字 と 桁数 を入力してください🙇‍♂️')
    elif not text:
        raise Exception('繰り返したい文字 を入力してください🙇‍♂️')
    elif not digits:
        raise Exception('桁数 を入力してください🙇‍♂️')
    elif int(digits) > 10000:
        raise Exception('桁数 には10000以下の数字を入力してください🙇‍♂️')
