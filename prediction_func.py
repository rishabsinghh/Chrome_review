from transformers import pipeline
import pandas as pd
import numpy as np

class PredictionFunc:
    def __init__(self,file_object,log_writer ):
        self.log_writer = log_writer
        self.file_object = file_object
        self.pipeline =pipeline("sentiment-analysis")
    def predict(self,df):
        try:
            self.log_writer.log(self.file_object,"Entered into predict function")
            self.data=df
            review=[]
            for x in self.data['Text']:
                try:
                    review_dict=self.pipeline(str(x))[0]
                    review.append(review_dict['label'])
                except Exception as e:
                    review.append('neutral')
                    self.log_writer.log(self.file_object,"Error in Loop: "+str(e))
                    pass
            self.data['review']=review
            final_out=self.data.loc[(self.data['Star']<2) & (self.data['review']=='POSITIVE')]
            self.log_writer.log(self.file_object,"Exited from predict function")
            final_out=final_out.drop(['review'],axis=1)
            return final_out
        except Exception as e:
            self.log_writer.log(self.file_object,"Error in predict function: "+str(e))
            return None
        

