import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error

if __name__ == '__main__':
    data = pd.read_csv('../data/numeric_data_corrupted.csv')

    Z = data.drop('price', axis=1)
    X = data.drop('price', axis=1).values
    y = data['price'].values

    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=42)

    lr = LinearRegression()
    lr.fit(x_train, y_train)

    y_pred = lr.predict(x_test)

    print("Linear regression R2: ", r2_score(y_test, y_pred))
    print('MAE:', mean_absolute_error(y_test, y_pred))

