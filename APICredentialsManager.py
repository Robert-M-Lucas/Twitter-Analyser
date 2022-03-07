def get_credentials() -> tuple:
    try:
        with open("data/TOKEN.txt", "r") as f:
            return f.read().split("\n")
    except FileNotFoundError:
        return "", "", "", ""


def save_credentials(tokens: list):
    with open("data/TOKEN.txt", "w") as f:
        f.write("\n".join(tokens))
