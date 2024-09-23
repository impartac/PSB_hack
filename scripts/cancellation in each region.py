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

grouped = df.groupby('Гостиница')['Дата отмены'].agg(['sum', 'count'])

# Рассчитываем процент отмен для каждого региона
grouped['Процент отмен'] = (grouped['sum'] / grouped['count']) * 100

# Определяем регионы
regions = ['Регион 1', 'Регион 2']

# Строим гистограмму
plt.figure(figsize=(10, 6))
plt.bar(regions, [grouped['Процент отмен'][1:2].sum(), grouped['Процент отмен'][3:5].sum()])
plt.xlabel('Регион')
plt.ylabel('Процент отмен')
plt.title('Процент отмен бронирований по регионам гостиниц')
plt.show()