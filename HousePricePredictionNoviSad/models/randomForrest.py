import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error
import numpy as np
from sklearn.model_selection import GridSearchCV


    # rf_Grid = GridSearchCV(estimator=rf, param_grid=params, cv=3, verbose=2, n_jobs=8)
    # rf_Grid.fit(x_train, y_train)
    # print(rf_Grid.best_params_)


if __name__ == '__main__':
    import pandas as pd
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.metrics import r2_score, mean_absolute_error

    data = pd.read_csv('../data/enkodovanSet.csv')

    Z = data.drop('cena', axis=1)
    X = data.drop('cena', axis=1).values
    y = data['cena'].values

    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    n_estimators = [int(x) for x in np.linspace(start=100, stop=600, num=10)]
    max_depth = [2, 3, 4, 5, 6, None]
    min_samples_split = [2, 3, 4, 5]
    min_samples_leaf = [1, 2, 3, 4]
    max_features = ["sqrt", "log2", None, "auto"]

    params = {
        'bootstrap': True,
        'max_depth': None,
        'max_features': 'auto',
        'min_samples_leaf': 1,
        'min_samples_split': 2,
        'n_estimators': 155
    }

    rf = RandomForestRegressor(**params)
    rf.fit(x_train, y_train)
    y_pred = rf.predict(x_test)

    print("Random Forest regressor R2:", r2_score(y_test, y_pred))
    print('MAE:', mean_absolute_error(y_test, y_pred))

    feature_importances = rf.feature_importances_
    print("\nFeature importances:")
    for feature, importance in zip(Z.columns, feature_importances):
        print(f"{feature}: {importance:.4f}")