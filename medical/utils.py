import pandas as pd
import numpy as np
import pickle
import json
import config
from sklearn import *
import os

class Medical():

    def __init__(self,age,sex,bmi,children,smoker,region):
        self.age=age
        self.sex=sex
        self.bmi=bmi
        self.children=children
        self.smoker=smoker
        self.region="region_"+region

    def load_model(self):
        with open(config.model_path,"rb")as file:
            self.model=pickle.load(file)
        with open(config.json_path,"r")as file:
            self.json=json.load(file)
    def get_predicted_charges(self):
        self.load_model()
        array=np.zeros(len(self.json["columns"]))
        array[0]=self.age
        array[1]=self.json["sex"][self.sex]
        array[2]=self.bmi
        array[3]=self.children
        array[4]=self.json["smoker"][self.smoker]
        region_index=self.json["columns"].index(self.region)
        array[region_index]=1

        charges=self.model.predict([array])[0]
        return charges