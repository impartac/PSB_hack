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

restrictioned_data = df[df['Внесена предоплата']<100000]['Внесена предоплата']
prepayment_values = sorted(restrictioned_data.unique())

# Создаем список для хранения процентных значений отмен
cancellation_rates = []

# Цикл по значениям предоплаты
for value in prepayment_values:
    # Фильтруем DataFrame по предоплате не более чем value
    filtered_df = df[df['Внесена предоплата'] <= value]
    
    # Вычисляем процент отмен
    cancellation_rate = filtered_df['Дата отмены'].mean() * 100
    cancellation_rates.append(cancellation_rate)

# Строим график
plt.figure(figsize=(10, 6))
plt.plot(prepayment_values, cancellation_rates)

# Настройка осей и заголовка
plt.xlabel('Предоплата')
plt.ylabel('Процент отмен брони')
plt.ylim(0,100)
plt.title('Зависимость процента отмен брони от предоплаты')

# Отображаем график
plt.show()





'''
plt.figure(figsize=(12, 8))
sns.scatterplot(x=pre_pay, y=cancellation, data=combined_columns, alpha=0.7)
sns.regplot(x=pre_pay, y=cancellation, data=combined_columns, color='red', ci=None)

plt.title('Cancellation vs PrePayment Amount')
plt.xlabel('Prepayment Amount')
plt.ylabel('Cancellation Status (0 = Not Cancelled, 1 = Cancelled)')
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()
# Rename the original 'Cancellation' column to preserve the original data'''
'''df = df.rename(columns={cancellation: 'Cancellation_Original'})

# Drop the original 'Cancellation' column
df = df.drop(cancellation, axis=1)

# Reorder columns to keep the original order
columns_order = ['Cancellation_Original', 'Cancellation_Binary'] + [col for col in df.columns if col not in ['Cancellation_Original', 'Cancellation_Binary']]
df = df[columns_order]

print("Updated DataFrame:")
print(df)'''
#print(f"The correlation between {сolumn1} and {column2} is: {correlation:.2f}")

