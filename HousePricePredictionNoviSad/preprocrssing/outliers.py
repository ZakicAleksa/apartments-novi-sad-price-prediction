import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

pd.pandas.set_option('display.max_rows', None)
pd.pandas.set_option('display.max_columns', None)
if __name__ == '__main__':
    data = pd.read_csv('../data/numeric_data.csv')

    # Round the surface column to the nearest multiple of 5
    data['rounded_surface'] = np.round(data['surface'] / 10) * 10

    plt.figure(figsize=(15, 15))  # Adjusted figure size
    sns.boxplot(data=data, x="rounded_surface", y="price")
    plt.xlabel("Квадратура")
    plt.ylabel("Цена")
    plt.title("Ванредне вредности на основу квадратуре и цене")
    plt.show()

    # Print outliers based on the rounded surface
    outliers = data[data["price"] > data.groupby('rounded_surface')['price'].transform(
        lambda x: x.quantile(0.75) + 3 * (x.quantile(0.75) - x.quantile(0.25)))]

    print(outliers)