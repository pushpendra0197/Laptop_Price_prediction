import numpy as np
import pandas as pd
import streamlit as st
import joblib
import sklearn
model=joblib.load("laptop_price_prediction.pkl")

st.title("Welcome to Laptop Price Prediction")
st.sidebar.text("Acer,Apple,Asus,Chuwi,Dell,Fujitsu,Google,Huawei,LG,Lenovo,MSI,Mediacom,Microsoft,Razer,Samsung,Toshiba,Vero,Xiaomi")
Company=st.sidebar.select_slider("Company",[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
st.sidebar.text("2 in 1 Convertible,Gaming,Netbook,Notebook,Ultrabook,Workstation")
TypeName=st.sidebar.select_slider("TypeName",[0,1,2,3,4,5])
st.sidebar.text("Android,Chrome OS,Linux,Mac OS X,No OS,Windows 10,Windows 10 S,Windows,macOS")
OS=st.sidebar.select_slider("OS",[0,1,2,3,4,5,6,7,8])
st.sidebar.text("Full HD,Quad HD+,Standard,4K Ultra HD")
Screen=st.sidebar.select_slider("screen",[0,1,2,3])
st.sidebar.text("No,Yes")
TouchScreen=st.sidebar.selectbox("Touchscreen",[0,1])
st.sidebar.text("No,Yes")
IpsPanel=st.sidebar.selectbox("IpsPanel",[0,1])
st.sidebar.text("No,Yes")
RetineDisplay=st.sidebar.selectbox("RetinaDisplay",[0,1])
st.sidebar.text("AMD,Intel,Samsung")
CPU_company=st.sidebar.selectbox("CPU_company ",[0,1,2])
st.sidebar.text("SSD,Flash Storage,HDD,Hybrid SSD")
PrimaryStorageType=st.sidebar.select_slider("PrimaryStorageType",[0,1,2,3])
st.sidebar.text("AMD,ARM,Intel,Nvidia")
GPU_company=st.sidebar.select_slider("GPU_company",[0,1,2,3])
Ram=st.sidebar.text_input("Ram")
CPU_freq=st.sidebar.text_input("CPU_freq")
PrimaryStorage=st.sidebar.text_input("PrimaryStorage")
SecondaryStorage=st.sidebar.text_input("SecondaryStorage")
Inches=st.sidebar.text_input("Inches")
button=st.sidebar.button("Predict")
###################################################################
if button:
    Company=int(Company)
    TypeName=int(TypeName)
    OS=int(OS)
    Screen=int(Screen)
    TouchScreen=int(TouchScreen)
    IPSpanel=int(IpsPanel)
    RetinaDisplay=int(RetineDisplay)
    CPU_company=int(CPU_company)
    PrimaryStorageType=int(PrimaryStorageType)
    GPU_company=int(GPU_company)
    Ram=int(Ram)
    CPU_freq=float(CPU_freq)
    PrimaryStorage=int(PrimaryStorage)
    SecondaryStorage=int(SecondaryStorage)
    Inches=float(Inches)
    Data=pd.DataFrame({"Company":Company,
                        "TypeName":TypeName,
                        "OS":OS,
                        "Screen": Screen,
                        "Touchscreen":TouchScreen,
                        "IPSpanel":IpsPanel,
                        "RetinaDisplay":RetineDisplay,
                        "CPU_company":CPU_company,
                        "PrimaryStorageType":PrimaryStorageType,
                        "GPU_company":GPU_company,
                        "Ram":Ram,
                        "CPU_freq":CPU_freq,
                        "PrimaryStorage":PrimaryStorage,
                        "SecondaryStorage":SecondaryStorage,
                        "Inches":Inches},index=[0])
    pred=model.predict(Data)
    pred=int(pred)
    pr=(f"{pred} RS")
    st.subheader(pr,divider='red')
    st.balloons()






