from prediction_func import PredictionFunc
from application_logger.logger import app_logger
import streamlit as st
import pandas as pd
import numpy as np
import streamlit_authenticator as stauth

file_object = open("training_logs/logs.txt",'a+')
log_writer=app_logger()
def main():
    log_writer.log(file_object,"Entered into main function")
    try:
        log_writer.log(file_object,"Application Started")
        predictor=PredictionFunc(file_object,log_writer)
        st.title("Chrome Reviews Problem")#Defining the Header for the page
        uploaded_file = st.file_uploader("Upload your data here", type=["csv"])
        if uploaded_file is not None:
                data = pd.read_csv(uploaded_file)#Reading the uploaded file
                st.subheader("Input Data")
                st.write(data)
                if st.button("Predict"):
                    result = predictor.predict(data)#Calling the predict function
                    st.success("Predictions done, Output:")
                    st.write(result)#Writing the output
                    st.download_button("Download",result.to_csv(index=False))#Downloading the output
                    log_writer.log(file_object,"Predictions done, output file generated")

        else:
            st.subheader("Please upload a CSV file")
    except Exception as e:
        log_writer.log(file_object,"Error in main function: "+str(e))
        raise e 
    log_writer.log(file_object,"Exited from main function")
    file_object.close()
if __name__=="__main__":
    #Authentication
    names = ['VIP']
    usernames = ['evaluator']
    passwords = ['please pass me to the next round']
    hashed_passwords = stauth.Hasher(passwords).generate()
    authenticate=stauth.Authenticate(names, usernames, hashed_passwords,'bread','1234',cookie_expiry_days=30)
    name, authentication_status, username = authenticate.login('Login','main')
    if authentication_status:
        authenticate.logout('Logout','main')
        main()
    elif authentication_status == False:
        st.error('Username/password is incorrect')
    elif authentication_status == None:
        st.warning('Please enter your username and password')