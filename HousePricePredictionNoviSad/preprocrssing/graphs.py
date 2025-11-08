import matplotlib.pyplot as plt
import pandas as pd


pd.pandas.set_option('display.max_rows', None)
pd.pandas.set_option('display.max_columns', None)
if __name__ == '__main__':
    data = pd.read_csv('../data/očišćenSet.csv')
    plt.scatter(y = data['cena'], x = data['površina'])
    plt.ylabel('Cena')
    plt.xlabel('Kvadratura')
    plt.show()

    print(data[data['površina']>300000])

