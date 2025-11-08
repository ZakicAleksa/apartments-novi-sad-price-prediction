import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
import matplotlib as mpl

pd.pandas.set_option('display.max_rows', None)
pd.pandas.set_option('display.max_columns', None)
if __name__ == '__main__':
    data = pd.read_csv("../data/enkodovanSet.csv")

    print(data.isnull().sum())

    x = data.drop(["cena"], axis=1)
    y = data['cena']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

    heatmap_data = data[["cena",
                         "površina",
                         "broj soba",
                         "nameštenost",
                         "garaža",
                         "sprat",
                         "godina izgradnje",
                         "ima lift (1)",
                         "ima lift (2)",
                         'luksuzno',
                         'renovirano',
                         'novo',
                         'u izgradnji']]
    plt.figure(figsize=(10, 10))
    cor = heatmap_data.corr()
    sns.heatmap(cor, annot=True, cmap=plt.cm.CMRmap_r)
    plt.show()
