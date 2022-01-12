import pandas as pd
from plot_histogram import plot_histogram


def solve_task4(data: pd.DataFrame):
    print("4. Построить гистрограмму частоты заказов по позициям (item)")
    data_to_display = data["item_name"].value_counts().to_dict()
    plot_histogram(data_to_display, "Гистограмма частоты заказов")