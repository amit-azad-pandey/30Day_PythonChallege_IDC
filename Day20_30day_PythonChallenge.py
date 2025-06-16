import requests

def fetch_page(url):
    try:
        response = requests.get(url, timeout=5)      
        response.raise_for_status()                  
    except requests.exceptions.RequestException as e:
        print("Could not fetch page:", e)
        return


    print("\nPage preview:\n")
    print(response.text[:500])

url = input("Enter URL: ").strip()
fetch_page(url)