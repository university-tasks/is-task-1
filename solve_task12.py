import pandas as pd
from pandas.core.indexes import multi

def solve_task12(data: pd.DataFrame):
    print("12. Определить цену по каждой позиции в отдельности")

    # unique_items = set(data["item_name"].to_list())
    # for item in unique_items:
    #     splitted = item.split(" and ")
    #     if len(splitted) > 0:
    #         unique_items.remove(item)
    #         for splitted_item in splitted:
    #             unique_items.add(splitted_item)

    # print(unique_items)

    prices = data[data["quantity"] == 1]
    multi_order = data[data["item_name"].isin(prices["item_name"].to_list())]