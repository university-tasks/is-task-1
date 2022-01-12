import pandas as pd

def solve_task8(data: pd.DataFrame):
    print("8. Выведите среднее, минимальное и максимальное, медианное значения позиций в заказе")
    mean = data["item_price"].mean()
    min = data["item_price"].min()
    max = data["item_price"].max()
    median = data["item_price"].median()
    print(f"Среднее значение: ${mean}")
    print(f"Минимальное значение: ${min}")
    print(f"Максимальное значение: ${max}")
    print(f"Медиана: ${median}")
    print("\n\n")
