import pandas as pd

def solve_task3(data: pd.DataFrame):
    print("3. Определить самую частую позицию (item) в заказе")
    print(data['item_name'].mode(), end="\n\n")