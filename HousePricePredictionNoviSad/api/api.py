import pandas as pd
import pickle
from flask import Flask, request, jsonify
from flasgger import Swagger, swag_from

app = Flask(__name__)
Swagger(app)

model = pickle.load(open("..\models\model.pkl", "rb"))

# Define all possible features here based on your table columns
all_features = [
    'površina', 'broj soba', 'nameštenost', 'garaža', 'sprat', 'godina izgradnje',
    'alarm, terasa', 'dvorište, terasa', 'lođa', 'podrum', 'podrum, terasa',
    'prilaz za invalide, dvorište, terasa', 'prilaz za invalide, terasa', 'terasa',
    'terasa, lođa', 'terase (2)', 'Adamovićevo Naselje', 'Adice', 'Avijatičarsko Naselje',
    'Bulevar Evrope', 'Bulevar Oslobođenja', 'Bulevar Patrijarha Pavla', 'Cara Dušana',
    'Detelinara', 'Futoški put', 'Grbavica', 'Kej', 'Klisa', 'Liman', 'Liman 2', 'Liman 3',
    'Liman 4', 'Lipov Gaj', 'Nova Detelinara', 'Novo Naselje', 'Petrovaradin', 'Podbara',
    'Rotkvarija', 'Sajmište', 'Salajka', 'Socijalno', 'Spens', 'Sremska Kamenica',
    'Stara Detelinara', 'Stari Grad', 'Tatarsko Brdo', 'Telep', 'Veternik', 'retka_lokacija',
    'Železnička stanica', 'retka_vrednost_grejanje', 'centralno grejanje', 'etažno grejanje',
    'grejanje na gas', 'grejanje na struju', 'podno grejanje', 'Dupleks', 'Dvorišni stan',
    'Penthaus', 'retka_vrednost_tip', 'Salonac', 'Stan u kući', 'Stan u zgradi', 'retka_vrednost_lift',
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
    data = pd.read_csv('../data/enkodovanSet.csv')
    X_columns = data.drop('cena', axis=1).columns

    # Ensure request_df has the same columns as X_columns
    request_df = request_df[X_columns]

    # Predict using the loaded model
    prediction = model.predict(request_df)

    # Format predictions with EUR suffix
    prediction_with_eur = [f"{pred} EUR" for pred in prediction]

    return jsonify({"Прогноза цене некретнине": prediction_with_eur})


if __name__ == "__main__":
    app.run(debug=True)
