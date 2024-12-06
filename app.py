from flask import Flask, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

# process CSV into Python object transaction_data
def process_data(file):
    headers = ['date', 'type', 'amount', 'memo']
    df = pd.read_csv(file, header=None, names=headers)
    transaction_data = []
    for index, row in df.iterrows():
        record = {headers[i]: row.iloc[i] for i in range(len(headers))}
        transaction_data.append(record)
    return transaction_data

# GET API for CSV input data
@app.route('/report', methods=['GET'])
def upload_data():
    if 'file' not in request.args:
        return jsonify({'error': 'No file part'}), 400
    file = request.args['file']
    if file.endswith('.csv'):
        # call process_data API
        transaction_data = process_data(file)
        return jsonify(transaction_data), 200
    else:
        return jsonify({'error': 'Input is not CSV file type'}), 400

# POST API for JSON output of processed data
@app.route('/transactions', methods=['POST'])
def return_json():
    # retrieve input data
    if 'file' not in request.args:
        return jsonify({'error': 'No file part'}), 400
    file = request.args['file']
    if file.endswith('.csv'):
        transaction_data = process_data(file)
    if not transaction_data:
        return jsonify({'error': 'No input data'}), 400
    
    # return gross revenue, expenses, and net revenue
    gross_revenue = 0
    expenses = 0
    for transaction in transaction_data:
        if transaction['type'] == 'Expense':
            expenses += transaction['amount']
        elif transaction['type'] == 'Income':
            gross_revenue += transaction['amount']
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