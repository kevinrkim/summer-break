# simple curl test of 2 endpoints assuming default port for Flask, adjust as needed
curl -X POST -F "file=@data.csv" http://127.0.0.1:5000/transactions
echo
curl http://127.0.0.1:5000/report
