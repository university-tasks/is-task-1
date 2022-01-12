import pandas as pd
import numpy as np

from solve_task1 import solve_task1
from solve_task2 import solve_task2
from solve_task3 import solve_task3
from solve_task4 import solve_task4
from solve_task5 import solve_task5
from solve_task6 import solve_task6
from solve_task7 import solve_task7
from solve_task8 import solve_task8
from solve_task9 import solve_task9
from solve_task10 import solve_task10
from solve_task11 import solve_task11
from solve_task12 import solve_task12
 
data = pd.read_csv("./dataset.tsv", sep="\t", header=0)
data = data.replace(np.nan, '', regex=True)
data = data.astype({
    "order_id" : "int64", 
    "quantity": "int64", 
    "item_name": "category",
    })

solve_task1(data)
solve_task2(data)
solve_task3(data)
solve_task4(data)
solve_task5(data)
solve_task6(data)
solve_task7(data)
solve_task8(data)
solve_task9(data)
solve_task10(data)
solve_task11(data)
solve_task12(data)