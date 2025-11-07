import pandas as pd
import pickle
from flask import Flask, request, jsonify
from flasgger import Swagger, swag_from

app = Flask(__name__)
Swagger(app)

model = pickle.load(open(r"C:\Users\aleksa\Desktop\fax\ORI\OriProject\HousePricePredictionNoviSad\diplomski\models\model.pkl", "rb"))

# Define all possible features here based on your table columns
all_features = [
    'surface', 'rooms', 'furniture', 'garage', 'floor', 'yearOfBuild',
    'alarm, terasa', 'dvorište, terasa', 'lođa', 'podrum', 'podrum, terasa',
    'prilaz za invalide, dvorište, terasa', 'prilaz za invalide, terasa', 'terasa',
    'terasa, lođa', 'terase (2)', 'Adamovićevo Naselje', 'Adice', 'Avijatičarsko Naselje',
    'Bulevar Evrope', 'Bulevar Oslobođenja', 'Bulevar Patrijarha Pavla', 'Cara Dušana',
    'Detelinara', 'Futoški put', 'Grbavica', 'Kej', 'Klisa', 'Liman', 'Liman 2', 'Liman 3',
    'Liman 4', 'Lipov Gaj', 'Nova Detelinara', 'Novo Naselje', 'Petrovaradin', 'Podbara',
    'Rotkvarija', 'Sajmište', 'Salajka', 'Socijalno', 'Spens', 'Sremska Kamenica',
    'Stara Detelinara', 'Stari Grad', 'Tatarsko Brdo', 'Telep', 'Veternik', 'rare_location',
    'Železnička stanica', 'Rare_var_heating', 'centralno grejanje', 'etažno grejanje',
    'grejanje na gas', 'grejanje na struju', 'podno grejanje', 'Dupleks', 'Dvorišni stan',
    'Penthaus', 'Rare_var_type', 'Salonac', 'Stan u kući', 'Stan u zgradi', 'Rare_var_elevator',
    'ima lift (1)', 'ima lift (2)', 'luksuzno', 'novo', 'održavano', 'potrebno renoviranje',
    'renovirano', 'u izgradnji', 'uobičajeno stanje'
]

@app.route("/predict", methods=["POST"])
@swag_from({
    'responses': {
        200: {
            'description': 'A list of predictions',
            'examples': {
                'application/json': {"Прогноза цене некретнине": ["0 EUR", "1 EUR"]}
            }
        }
    },
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {feature: {'type': 'number'} for feature in all_features}
                }
            }
        }
    ],
    'tags': ['Prediction']
})
def predict():
    request_json_ = request.json
    request_df = pd.DataFrame(request_json_)

    # Load the columns used during training
    data = pd.read_csv('../data/numeric_data_with_state.csv')
    X_columns = data.drop('price', axis=1).columns

    # Ensure request_df has the same columns as X_columns
    request_df = request_df[X_columns]

    # Predict using the loaded model
    prediction = model.predict(request_df)

    # Format predictions with EUR suffix
    prediction_with_eur = [f"{pred} EUR" for pred in prediction]

    return jsonify({"Прогноза цене некретнине": prediction_with_eur})


if __name__ == "__main__":
    app.run(debug=True)
