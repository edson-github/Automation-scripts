import requests

url = input("Enter domain or IP with / at end:")
path = input("Enter Wordlist path :")
with open(path, "r") as file:
    for _ in range(len(file)):
        wls = file.readline()
        r = requests.get(url + wls)
        stats = r.status_code

    print("_" * 50)
    print(f"Path :{url}{wls}", stats)
    print("_" * 50)
