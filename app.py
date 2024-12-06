from flask import Flask, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

# process CSV into Python object transaction_data

# POST API
@app.route('/transactions', methods=['POST'])
def store_data():
    global transaction_data
    if 'file' not in request.files:
        return jsonify({'error': 'file not found'}), 400
    file = request.files['file']

    if file and file.filename.endswith('.csv'):
        headers = ['date', 'type', 'amount', 'memo']
        transaction_data = pd.read_csv(file, header=None, names=headers)
        return jsonify({'message': 'file successfully uploaded'}), 200
    else:
        return jsonify({'message': 'valid CSV not found'})

# GET API 
@app.route('/report', methods=['GET'])
def return_json():
    if transaction_data is None:
        return jsonify({'error': 'no valid data found'})
    gross_revenue = 0
    expenses = 0

    for index, row in transaction_data.iterrows():
        if row['type'] == 'Expense':
            expenses += row['amount']
        elif row['type'] == 'Income':
            gross_revenue += row['amount']
    net_revenue = gross_revenue - expenses
    output = [
        {
            "gross-revenue": gross_revenue,
            "expenses": expenses,
            "net-revenue": net_revenue       
        }
    ]
    return jsonify(output), 200

if __name__ == '__main__':
    app.run(debug=True)