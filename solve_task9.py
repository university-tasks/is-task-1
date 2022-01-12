from typing import Dict
import pandas as pd

from plot_histogram import plot_histogram

def get_roasting_data(data: list[str]) -> Dict:
    d = {"mild": 0, "medium": 0, "hot": 0 }

    for item in data:
        if "(Mild)" in item: d["mild"]+=1
        if "(Medium)" in item: d["medium"]+=1
        if "(Hot)" in item: d["hot"]+=1 

    return d

def solve_task9(data: pd.DataFrame):
    print("!!!9. Определить статистику заказов стейков, а также статистику заказов прожарки")

    def get_roasting_data(data: list[str]):
        d = {"mild": 0, "medium": 0, "hot": 0 }

        for item in data:
            if "(Mild)" in item: d["mild"]+=1
            if "(Medium)" in item: d["medium"]+=1
            if "(Hot)" in item: d["hot"]+=1 

        return d

    steak_data = data.loc[data["item_name"].str.contains("Steak", na=False)]

    steak_data_to_plot = dict(filter(lambda x: x[1] > 0, steak_data["item_name"].value_counts().to_dict().items()))
    plot_histogram(steak_data_to_plot, "Статистика заказов стейков")


    steak_roasting_data_to_plot = get_roasting_data(steak_data["choice_description"])
    plot_histogram(steak_roasting_data_to_plot, "Статистика прожарок для стейков")

    roasting_data_to_plot = get_roasting_data(data["choice_description"].tolist())
    plot_histogram(roasting_data_to_plot, "Общая статистика прожарок")