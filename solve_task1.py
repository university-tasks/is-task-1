import pandas as pd

def solve_task1(data: pd.DataFrame):
    print("1. Вывести: кол-во наблюдений в датасете")
    print(len(data.index), end="\n\n")