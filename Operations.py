def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def divide(a: float, b: float) -> float:
    if b == 0:
        return 0
    else:
        return a / b


def multiply(a: float, b: float) -> float:
    return a * b


def power(a: float, b: float) -> float:
    return a ** b


Values = {
            "Likes": ["likes", True],
            "Retweets": ["retweets", True],
            "Length": ["len", True],
            "Date": ["date", False]
        }

Operations = {
    "Add": [add, "+"],
    "Subtract": [subtract, "-"],
    "Divide": [divide, "/"],
    "Multiply": [multiply, "x"],
    "Power": [power, "^"]
}
