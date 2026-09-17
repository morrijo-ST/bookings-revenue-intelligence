import pandas as pd
from synthetic import generate_bookings_data

def load_data(path=None):
    df=generate_bookings_data() if path is None else pd.read_csv(path,parse_dates=["week"])
    df["weighted_pipeline"]=df["booking_value"]*df["probability"]
    return df

def summary(df):
    won=df.loc[df.stage=="Closed Won","booking_value"].sum()
    weighted=df["weighted_pipeline"].sum()
    rev=df["recognized_revenue"].sum()
    renew=df["renewal_value"].sum()
    return {"closed_won":won,"weighted_pipeline":weighted,"revenue":rev,"renewals":renew}
