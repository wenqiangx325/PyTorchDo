import requests
import torch

def download_data():
    url = "https://s3.amazonaws.com/capitalbikeshare-data/2017-capitalbikeshare-tripdata.zip"
    requests.get(url)

if __name__ == "__main__":
    pass
