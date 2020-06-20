from svm.CustomSVM import CustomSVM
import ipyvolume as ipv
import numpy as np
import pandas as pd

plots = pd.DataFrame.from_dict({
    "x": [1.0,1.0,1.0,3.0,1.0,3.0,1.0,3.0,1.0],
    "y": [0.0,0.0,1.0,1.0,1.0,2.0,2.0,2.0,1.0],
    "z": [1.0,2.0,2.0,4.0,3.0,3.0,1.0,1.0,0.0],
    "color": ["red","red","red","red","red","blue","blue","blue","blue"]
})

customModel = CustomSVM(plots)
customModel.build_model()
customModel.draw_plots()
customModel.draw_hyperplane()