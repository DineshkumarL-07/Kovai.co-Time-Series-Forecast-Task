import pandas as pd

data = pd.read_csv(r"C:\Users\rgowt\Downloads\Time Series forecast.csv")  

service_columns = ['Local Route', 'Light Rail', 'Peak Service', 'Rapid Route', 'School', 'Other']
descriptive_stats = data[service_columns].agg(['mean', 'median', 'min', 'max', 'std'])

print("Descriptive Statistics for each service type:")
print(descriptive_stats)

data = pd.read_csv(r"C:\Users\rgowt\Downloads\Time Series forecast.csv", parse_dates=['Date'], dayfirst=True)  

service_columns = ['Local Route', 'Light Rail', 'Peak Service', 'Rapid Route', 'School', 'Other']
yearly_stats = data.groupby('Year')[service_columns].agg(['mean', 'median', 'min', 'max', 'std'])

print("Yearly Descriptive Statistics for each service type:")
print(yearly_stats)
