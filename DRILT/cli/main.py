import requests


def main():
    url_check = input("Enter a URL to check: ")

    response = requests.get(url_check)

    print(response.status_code)   # e.g. 200
    print(response.headers)       # dict of response headers
    print(response.text)          # response body as a string


if __name__ == "__main__":
    main()  