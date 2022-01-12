import pandas as pd
from plot_histogram import plot_histogram

def solve_task6(data: pd.DataFrame):
    print("6. Построить гистограмму кол-во денег заработанных по каждой позиции (item)")
    data_to_display = data.groupby(by=["item_name"])["item_price"].sum().to_dict()
    plot_histogram(data_to_display, "Гистограмма кол-ва денег, заработанных с каждой позиции")