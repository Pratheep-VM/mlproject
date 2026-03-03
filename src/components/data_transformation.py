import sys
import os
from dataclasses import dataclass
from src.logger import logging
import pandas as pd
import numpy as np
from src.exception import CustomException
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join("artifacts","preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()
    
    def get_data_transformer_object(self):

        '''
        This function is responsible for data transformation
    
        '''
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]

            num_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median")),
                    ("scaler",StandardScaler())
                ]
            )

            cat_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder",OneHotEncoder()),
                    ("scaler",StandardScaler(with_mean=False))

                ])
            logging.info(f"Categorical Columns: {categorical_columns}")
            logging.info(f"Numerical Columns: {numerical_columns}")

            preprocessor=ColumnTransformer([
                ("num_pipeline",num_pipeline,numerical_columns),
                ("cat pipeline",cat_pipeline,categorical_columns)])
            
            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path) 
            test_df=pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")

            preprocessing_obj=self.get_data_transformer_object()

            target_column="math_score"
            numerical_columns=["writing_score","reading_score"]  

            train_input_df=train_df.drop(columns=[target_column],axis=1)
            test_input_df=test_df.drop(columns=[target_column],axis=1)

            train_output_df=train_df[target_column]
            test_output_df=test_df[target_column]

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

            preprocessed_train_arr=preprocessing_obj.fit_transform(train_input_df)
            preprocessed_test_arr=preprocessing_obj.transform(test_input_df)

            train_arr=np.c_[preprocessed_train_arr,np.array(train_output_df)]
            test_arr=np.c_[preprocessed_test_arr,np.array(test_output_df)]

            logging.info("Saved preprocessing object.")

            save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj

            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        except Exception as e:
            raise CustomException(e,sys)




        



     
