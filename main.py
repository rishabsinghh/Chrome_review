from prediction_func import PredictionFunc
from application_logger.logger import app_logger
import streamlit as st
import pandas as pd
import numpy as np
import os
file_object = open("training_logs/logs.txt",'a+')
log_writer=app_logger()
def main():
    log_writer.log(file_object,"Entered into main function")
    try:
        log_writer.log(file_object,"Application Started")
        predictor=PredictionFunc(file_object,log_writer)
        st.title("Chrome Reviews Problem")
        uploaded_file = st.file_uploader("Upload your data here", type=["csv"])
        path_to_store=st.text_input("Enter the path to store the output file")
        if uploaded_file is not None:
                data = pd.read_csv(uploaded_file)
                st.subheader("Input Data")
                st.write(data)
                if st.button("Predict"):
                    result = predictor.predict(data)
                    result.to_csv(str(path_to_store)+"//"+"predicted_data.csv")
                    st.subheader("Predictions")
                    st.write("File created at: "+ str(path_to_store)+"\predicted_data.csv")
                    st.success("Predictions done")
                    log_writer.log(file_object,"Predictions done")

        else:
            st.subheader("Please upload a CSV file")
    except Exception as e:
        log_writer.log(file_object,"Error in main function: "+str(e))
        raise e 
    log_writer.log(file_object,"Exited from main function")
    file_object.close()
if __name__=="__main__":
    main()