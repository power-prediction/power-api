from sklearn.ensemble import RandomForestRegressor
from fastapi import FastAPI
from pydantic import BaseModel

from datetime import datetime
import pickle
import pandas as pd

class Condition(BaseModel):
    temperature : float
    rain_sum : float
    humidity: float
    date: str
    hour : int
    surface_sum: float
    building_type : str


api = FastAPI()

@api.post("/get_power_use/")
def get_electricity_pricing(data: Condition):
    date = datetime.strptime(data.date,"%Y-%m-%d")
    humidity = data.humidity
    year = int(date.year)
    month = int(date.month)
    day = int(date.day)
    hour = data.hour

    건물유형_건물기타 = 0 
    건물유형_공공 = 0 
    건물유형_대학교 = 0 
    건물유형_데이터센터 = 0 
    건물유형_백화점및아울렛 = 0
    건물유형_병원 = 0 
    건물유형_상용 = 0
    건물유형_아파트 = 0
    건물유형_연구소 = 0
    건물유형_지식산업센터 = 0
    건물유형_할인마트 = 0 
    건물유형_호텔및리조트 = 0

    if data.building_type == '건물유형_건물기타':
        건물유형_건물기타 = 1
    if data.building_type == '건물유형_공공':
        건물유형_공공 = 1
    if data.building_type == '건물유형_대학교':
        건물유형_대학교 = 1
    if data.building_type == '건물유형_데이터센터':
        건물유형_데이터센터 = 1
    if data.building_type == '건물유형_백화점및아울렛':
        건물유형_백화점및아울렛 = 1
    if data.building_type == '건물유형_병원':
        건물유형_병원 = 1
    if data.building_type == '건물유형_상용':
        건물유형_상용 = 1
    if data.building_type == '건물유형_아파트':
        건물유형_아파트 = 1
    if data.building_type == '건물유형_연구소':
        건물유형_연구소 = 1
    if data.building_type == '건물유형_지식산업센터':
        건물유형_지식산업센터 = 1
    if data.building_type == '건물유형_할인마트':
        건물유형_할인마트 = 1
    if data.building_type == '건물유형_호텔및리조트':
        건물유형_호텔및리조트 = 1

    dict = {"기온(C)":data.temperature,
            "강수량(mm)":data.rain_sum,
            "습도(%)":humidity,
            "연도":year,
            "월":month,
            "일":day,
            "시":hour,
            "연면적(m2)":data.surface_sum,
            "건물유형_건물기타":건물유형_건물기타,
            "건물유형_공공":건물유형_공공,
            "건물유형_대학교":건물유형_대학교,
            "건물유형_데이터센터":건물유형_데이터센터,
            "건물유형_백화점및아울렛":건물유형_백화점및아울렛,
            "건물유형_병원":건물유형_병원,
            "건물유형_상용":건물유형_상용,
            "건물유형_아파트":건물유형_아파트,
            "건물유형_연구소":건물유형_연구소,
            "건물유형_지식산업센터":건물유형_지식산업센터,
            "건물유형_할인마트":건물유형_할인마트,
            "건물유형_호텔및리조트":건물유형_호텔및리조트}
    
    model_input = pd.DataFrame(dict,index=[0])

    with open("./rf_pred.pkl","rb") as f:
        rf_model = pickle.load(f)
    
    pred = rf_model.predict(model_input)
    return round(pred[0],2)


    








    


