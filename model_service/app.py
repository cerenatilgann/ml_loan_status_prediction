from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Load trained model
with open('model/model.pkl', 'rb') as model_file:
    model = joblib.load(model_file)

@app.route('/', methods=['POST'])
def predict():
    
    try:
        json = request.get_json()

        df = pd.DataFrame(json, index=[0])

        y_predict = model.predict(df)

        if y_predict[0] == 0  :
            pred = "Approved"
        else:
            pred = "Rejected"
            
        result = {"Predicted Loan Satus" : pred}

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True, port=8090)



