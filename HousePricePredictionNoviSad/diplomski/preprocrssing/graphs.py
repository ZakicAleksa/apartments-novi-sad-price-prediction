import matplotlib.pyplot as plt
import pandas as pd


pd.pandas.set_option('display.max_rows', None)
pd.pandas.set_option('display.max_columns', None)
if __name__ == '__main__':
    data = pd.read_csv('../data/numeric_data.csv')
    plt.scatter(y = data['price'], x = data['surface'])
    plt.ylabel('Цена')
    plt.xlabel('Квадратура')
    plt.show()

    print(data[data['surface']>300000])

