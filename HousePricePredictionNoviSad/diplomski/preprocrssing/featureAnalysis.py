import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
import matplotlib as mpl

pd.pandas.set_option('display.max_rows', None)
pd.pandas.set_option('display.max_columns', None)
if __name__ == '__main__':
    data = pd.read_csv("../data/numeric_data_with_state.csv")

    print(data.isnull().sum())

    x = data.drop(["price"], axis=1)
    y = data['price']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

    heatmap_data = data[["price",
                         "surface",
                         "rooms",
                         "furniture",
                         "garage",
                         "floor",
                         "yearOfBuild",
                         "ima lift (1)",
                         "ima lift (2)",
                         'luksuzno',
                         'renovirano',
                         'novo',
                         'u izgradnji']]
    data_no_rooms = data.drop(["rooms"], axis=1)
    plt.figure(figsize=(10, 10))
    cor = heatmap_data.corr()
    sns.heatmap(cor, annot=True, cmap=plt.cm.CMRmap_r)
    plt.show()
