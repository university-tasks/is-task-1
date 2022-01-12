import pandas as pd

def solve_task5(data: pd.DataFrame):
    print("5. Измените тип переменной item_price c помощью лямбда-функции")
    data["item_price"] = data["item_price"].apply(lambda x: float(x[1:])).astype("float64")
    print("", end="\n\n")   