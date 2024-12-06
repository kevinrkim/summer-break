from flask import Flask, request, jsonify
import pandas as pd
import os

app = Flask(__name__)
transaction_data = None

# POST API process CSV into Python object transaction_data
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
    global transaction_data

    if transaction_data is None:
        return jsonify({'error': 'no valid data found'})
    gross_revenue = 0
    expenses = 0

    for index, row in transaction_data.iterrows():
        print(pd.notna(row['type']))
        if pd.notna(row['type']) and str(row['type']).strip() == 'Expense':
            print(row['amount'])
            expenses += float(row['amount'])
        elif pd.notna(row['type']) and str(row['type']).strip() == 'Income':
            print(row['amount'])
            gross_revenue += float(row['amount'])
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