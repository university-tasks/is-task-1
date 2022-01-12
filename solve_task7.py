import pandas as pd

def solve_task7(data: pd.DataFrame):
    print("7. Средняя сумма заказа? (минимум 2 способа)")
    mean1 = data["item_price"].mean()
    mean2 = data["item_price"].sum()/len(data["item_price"])
    print(f"Среднее значение 1: ${mean1}")
    print(f"Среднее значение 2: ${mean2}")
    print("\n\n")