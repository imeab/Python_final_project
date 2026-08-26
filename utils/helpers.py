def get_text_input(message):
    while True:
        text = input(message).strip()
        if text != "":
            return text
        print("공백은 입력할 수 없어요. 다시 입력해주세요.")


def get_number_input(message, error_message="숫자만 입력해주세요."):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print(error_message)


def get_decimal_input(message, error_message="숫자(소수 포함)만 입력해주세요."):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print(error_message)