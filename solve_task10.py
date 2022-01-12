from numpy import number
import pandas as pd
from forex_python.converter import CurrencyRates

from plot_histogram import plot_histogram

def solve_task10(data: pd.DataFrame):
    print("10. Добавить новый столбец цен на каждую позицию в заказе в рублях.")
    rate = CurrencyRates().get_rate("USD", "RUB")
    data["item_price_ru"] = data["item_price"].apply(lambda x: x * rate)
    print("\n\n")