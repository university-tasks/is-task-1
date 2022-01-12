import pandas as pd

def solve_task2(data: pd.DataFrame):
    print("2. Вывести названия столбцов")
    for name in data.columns: print(name, end=" ")
    print("", end="\n\n")