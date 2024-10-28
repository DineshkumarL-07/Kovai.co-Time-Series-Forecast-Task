import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt


data = pd.read_csv(r"C:\Users\rgowt\Downloads\Time Series forecast.csv", parse_dates=['Date'], dayfirst=True)  
service_columns = ['Local Route', 'Light Rail', 'Peak Service', 'Rapid Route', 'School', 'Other']
forecasts = {}

for column in service_columns:
    df_train = data[['Date', column]].rename(columns={'Date': 'ds', column: 'y'})
    model = Prophet(daily_seasonality=True)
    model.fit(df_train)

    future = model.make_future_dataframe(periods=7)
    forecast = model.predict(future)
    forecasts[column] = forecast[['ds', 'yhat']].tail(7)
    
for service, forecast_data in forecasts.items():
    print(f"Forecast for {service} for the next 7 days:")
    print(forecast_data)
    print("\n")


# next 7 days forecast visualization

data = pd.read_csv(r"C:\Users\rgowt\Downloads\Time Series forecast.csv", parse_dates=['Date'], dayfirst=True) 
service_columns = ['Local Route', 'Light Rail', 'Peak Service', 'Rapid Route', 'School', 'Other']
train_data = data.iloc[:-7]  
test_data = data.iloc[-7:] 
forecasts = {}

for column in service_columns:
    df_train = train_data[['Date', column]].rename(columns={'Date': 'ds', column: 'y'})

    model = Prophet(daily_seasonality=True)
    model.fit(df_train)

    future = model.make_future_dataframe(periods=7)
    forecast = model.predict(future)

    forecasts[column] = forecast[['ds', 'yhat']].tail(7)
    model.plot(forecast)
    plt.title(f'{column} - 7-Day Forecast')
    plt.xlabel('Date')
    plt.ylabel('Patronage')
    plt.show()
