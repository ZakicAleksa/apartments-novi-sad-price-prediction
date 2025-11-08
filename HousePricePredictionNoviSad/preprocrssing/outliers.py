import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

pd.pandas.set_option('display.max_rows', None)
pd.pandas.set_option('display.max_columns', None)
if __name__ == '__main__':
    data = pd.read_csv('../data/očišćenSet.csv')

    # Round the surface column to the nearest multiple of 5
    data['zaokružena_površina'] = np.round(data['površina'] / 10) * 10

    plt.figure(figsize=(15, 15))  # Adjusted figure size
    sns.boxplot(data=data, x="zaokružena_površina", y="cena")
    plt.xlabel("Квадратура")
    plt.ylabel("Цена")
    plt.title("Ванредне вредности на основу квадратуре и цене")
    plt.show()

    # Print outliers based on the rounded surface
    outliers = data[data["cena"] > data.groupby('zaokružena_površina')['cena'].transform(
        lambda x: x.quantile(0.75) + 3 * (x.quantile(0.75) - x.quantile(0.25)))]

    print(outliers)