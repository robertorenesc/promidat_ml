import math
import numpy as np
from utils.DataFrameUtils import DataFrameUtils

data = DataFrameUtils.create_dataframe_from_dict(
    {
        "x1": [1, 1, 1, 1],
        "x2": [0, 0, 1, 1],
        "x3": [0, 1, 0, 1],
        "z":  [1, 1, 1, 0]
    }
)

def verify_values(array1, array2):
    return (array1 == array2).all()

def perceptron(x1, x2, x3, w1, w2, w3, t):
    return (x1 * w1 + x2 * w2 + x3 * w3 - t)

def tangente_hiperbolica(x1, x2, x3, w1, w2, w3, t):
    val = (2 / (1 + math.exp(-2 * perceptron(x1, x2, x3, w1, w2, w3, t)))) - 1
    return 1 if val >= 0 else 0

weights = [x * 0.1 for x in range(-10, 11)]
thetas = [x * 0.1 for x in range(0, 11)]

success_values = list()

for t in thetas:
    for w3 in weights:
        for w2 in weights:
            for w1 in weights:
                tangente = data.apply(lambda row: tangente_hiperbolica(row["x1"], row["x2"], row["x3"], w1, w2, w3, t), axis=1)
                if verify_values(tangente, data["z"]):
                    success_values.append([w1, w2, w3, t])

print(DataFrameUtils.create_dataframe(success_values, columns=["w1", "w2", "w3", "T"]))