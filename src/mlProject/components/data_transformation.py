import pandas as pd
from src.mlProject.logger import logging


class DataTransformation:

    def initiate_data_transformation(self, train_path, test_path):

        train_df = pd.read_csv(train_path)
        test_df = pd.read_csv(test_path)

        # convert date
        train_df["Date"] = pd.to_datetime(train_df["Date"])
        test_df["Date"] = pd.to_datetime(test_df["Date"])

        # create time features
        for df in [train_df, test_df]:

            df["Year"] = df["Date"].dt.year
            df["Month"] = df["Date"].dt.month
            df["Day"] = df["Date"].dt.day
            df["WeekOfYear"] = df["Date"].dt.isocalendar().week.astype(int)

        # encode categorical
        train_df = pd.get_dummies(train_df, columns=["StateHoliday"], drop_first=True)
        test_df = pd.get_dummies(test_df, columns=["StateHoliday"], drop_first=True)

        # target
        y_train = train_df["Sales"]
        y_test = test_df["Sales"]

        # drop unused columns
        X_train = train_df.drop(["Sales", "Date"], axis=1)
        X_test = test_df.drop(["Sales", "Date"], axis=1)

        logging.info("Data Transformation Completed")

        return X_train, X_test, y_train, y_test