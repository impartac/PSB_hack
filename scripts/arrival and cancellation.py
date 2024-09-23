import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Read Excel file
df = pd.read_excel('train.xlsx')

# Explore the data
print(df.head())
print(df.info())

df['Дата отмены'] = df['Дата отмены'].notna().astype(int)

df['Месяц'] = df['Заезд'].dt.month

# Группируем DataFrame по месяцу и считаем количество отмен
grouped = df.groupby('Месяц')['Дата отмены'].sum()

# Строим гистограмму
plt.figure(figsize=(10, 6))
plt.bar(grouped.index, grouped.values)
plt.xlabel('Месяц')
plt.ylabel('Количество отмен')
plt.title('Количество отмен бронирований по месяцам')
plt.xticks(rotation=45) 
plt.xticks(range(1, 13))
plt.show()