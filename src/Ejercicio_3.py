from utils.DataFrameUtils import DataFrameUtils

import random
import math

def get_random_numbers():
    random.seed()
    w1 = random.randint(-5, 5)
    w2 = random.randint(-5, 5)
    t = random.randint(-5, 5) 
    return (w1, w2, t)

def verify_values(array1, array2):
    return (array1 == array2).all()

def sigmoidea(x1, x2, w1, w2, t):
    percept = 1 / (1 + math.exp(-1 * (x1*w1 + x2*w2 - t)))
    return 1 if percept >= 0.5 else 0

data = DataFrameUtils.create_dataframe_from_dict(
    {
        "x1": [0, 1, 0, 1],
        "x2": [0, 0, 1, 1],
        "y":  [1, 1, 1, 0]
    }
)
print(data)

while True:
    w1, w2, t = get_random_numbers()
    col = data.apply(lambda row: sigmoidea(row["x1"], row["x2"], w1, w2, t), axis=1)
    print(f"Testing: w1 = {w1}, w2 = {w2}, t = {t}")
    if verify_values(data["y"], col):
        print("Success...")
        break

print("\nRequired values: ")
print(f"\tw1 = {w1}\n\tw2 = {w2}\n\tt  = {t}")