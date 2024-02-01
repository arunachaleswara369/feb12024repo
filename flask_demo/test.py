import requests
import json

def test_predict(url):
    data = {
        "Id": 1,
        "OverallQual": 7,
        "TotalBsmtSF": 856,
        "GrLivArea": 1710
    }
    response = requests.post(url + "/predict", params=data)
    
    if response.status_code == 200:
        result = response.text
        print("Single Row Prediction Result:", result)
    else:
        print("Error in predicting single row:", response.text)

def test_predict_file(url, file_path):
    files = {'input_file': open(file_path, 'rb')}
    response = requests.post(url + "/predict_file", files=files)
    
    if response.status_code == 200:
        result = response.text
        print("File Prediction Result:", result)
    else:
        print("Error in predicting from file:", response.text)

if __name__ == "__main__":
    # Update with the actual URL where your Flask app is running
    app_url = "http://127.0.0.1:3000"
    
    # Test single row prediction
    test_predict(app_url)

    # Test file prediction
    file_path = "../input_file.csv"  # Update with the path to your test file
    test_predict_file(app_url, file_path)