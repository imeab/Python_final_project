def get_string(prompt_msg):
    while True:
        value = input(prompt_msg).strip()
        if value:
            return value

        print("입력값은 공백일 수 없습니다. 다시 입력해주세요.")

def get_valid_integer(prompt_msg, error_msg = "숫자만 입력해주세요."):
    while True:
        try:
            return int(input(prompt_msg))
        except ValueError:
            print(error_msg)

def get_valid_float(prompt_msg, error_msg = "숫자(실수)만 입력해주세요."):
    while True:
        try:
            return float(input(prompt_msg))
        except ValueError:
            print(error_msg)