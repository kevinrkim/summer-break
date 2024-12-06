# About the project
This is a simple project that allows the user to take a CSV file containing transaction data (of both expenses and income) and output a simple JSON containing the calculations on total gross revenues, expenses, and net revenues.

# Table of Contents
- Requirements
- Setting up a Python environment
- Running the Python application
- API endpoints
- Using the test file
- Additional context
- Solution shortcomings
- Future refinements

# Requirements
- Python3
- Flask
- Pandas

# Setting up a Python environment
1. Ensure that all of the contents of this folder (summer-break) is saved locally onto your computer.
2. Create and activate a virtual Python environment to more easily manage the project dependencies.
    ```
    python3 -m venv myenv
    source myenv/bin/activate # for MacOS or Linux
    myenv\Scripts\activate # for Windows
    ```
3. Install the project dependencies
    ```
    pip install Flask pandas
    ```

# Running the Python application
1. Start the Flask application with the following command:
    ```
    python app.py
    ```
2. Ensure that there is a data.csv input file in the same directory (summer-break). The dataset should have no headers, but contain the following columns:
    - Date (in yyyy-mm-dd format)
    - Type (string value either 'Expense' or 'Income')
    - Amount (in format ##.##)
    - Memo (string containing any important references, will not be used as data input for calculations)
3. The two APIs (/report and /transactions) can be accessed using curl.

# API Endpoints
- POST /transactions
    - Description: Accepts a CSV file containing transaction information, parses, and stores the data as a Python object
    - Request: Form-data with a key titled file that contains the CSV file
    Response: 200 OK if the file is successfully uploaded, or 400 Bad Request if a file is not found or is invalid
- GET /report
    - Description: Performs calculations on the input data and returns output as JSON
    - Response: 200 OK with a JSON object containing the total gross revenue, expenses, and net revenue, or 400 Bad Request if no data is found

# Using the test file
This directory already contains a test file and a sample input dataset to perform the test on. In order to utilize the test, simply execute the test file:
```
./test.sh
```

# Additional context
The solution is relatively simple given some assumptions I made around the quality of the data. In looking at the sample data, the values appeared to be consistent and well-organized. The values in each column were formatted correctly (with the exception of a line item that contained a comment on spark plugs, which should likely have been a memo in one of the other rows). Therefore, for the sake of simplicity, I coded the calculations to accept the inputs mostly as they are with minimal checks and adjustments. The only adjustments I made were to eliminate the leading white spaces before the 'type' values, ensuring that the amounts were properly represented as floats rather than strings, and ensuring that NaN values were not included in the calculations.

# Solution shortcomings
My solution was built around the sample dataset, meaning that I created checks and validations only for the specific examples of unclean data that I saw. In the current state, my solution would not succeed if there are other types of noise in the data (e.g., white space in any of the other columns besides 'type', lowercase/uppercase variations in the 'type', etc.)

# Future refinements
If I had more time to work on this project, I would certainly address the shortcomings listed above. While my solution works just fine as an MVP, I would definitely want to ensure that all potential variations and noise in the input data are accounted for. I would make sure to clean up all white noise, accept any variations in the capitalization of any of the string fields, and perhaps even implement a fuzzy matching algorithm to be even more forgiving in case of any fat finger mistakes in the input data.