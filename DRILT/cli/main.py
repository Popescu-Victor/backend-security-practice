import requests
import pandas


domain = input("Enter the domain: ")
path_endpoint = input("Enter the path endpoint: ")
query_params = input("Enter the query parameters (comma-separated): ").split(",")

def fetch_data(domain, path_endpoint, query_params):
    url = f"https://{domain}/{path_endpoint}"
    params = {param: "" for param in query_params}
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")
        return None

data = fetch_data(domain, path_endpoint, query_params)