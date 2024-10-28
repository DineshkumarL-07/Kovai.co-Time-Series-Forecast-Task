import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\rgowt\Downloads\Time Series forecast.csv", parse_dates=['Date'], dayfirst=True)  

data['Year'] = data['Date'].dt.year

service_columns = ['Local Route', 'Light Rail', 'Peak Service', 'Rapid Route', 'School', 'Other']

for year in data['Year'].unique():
    yearly_data = data[data['Year'] == year]

    plt.figure(figsize=(14, 8))
    for column in service_columns:
        plt.plot(yearly_data['Date'], yearly_data[column], label=column)

    plt.title(f'Trends in Transport Service Patronage for the Year {year}')
    plt.xlabel('Date')
    plt.ylabel('Patronage Numbers')
    plt.legend()
    plt.show()

# Correlation code

import seaborn as sns
correlation_matrix = data[service_columns].corr()

plt.figure(figsize=(10, 8))

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)

plt.title('Correlation between Transport Services')
plt.show()