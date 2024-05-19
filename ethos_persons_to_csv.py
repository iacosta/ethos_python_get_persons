import requests
import csv
import json

API_KEY = 'XXXXXX-ZZZZZ-AAAA-BBBB-ABCDEFEHIJK'
AUTH_URL = 'https://integrate.elluciancloud.com/auth'
DATA_URL = 'https://integrate.elluciancloud.com/api/persons'
TOKEN_EXPIRATION_MINUTES = 30

def get_access_token():
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }
    payload = json.dumps({'expirationMinutes': TOKEN_EXPIRATION_MINUTES})
    print(f"Requesting access token with payload: {payload} and headers: {headers}")
    response = requests.post(AUTH_URL, headers=headers, data=payload)
    print(f"Response status code: {response.status_code}")
    print(f"Response text: {response.text}")
    if response.status_code != 200:
        print(f"Failed to get access token: {response.status_code}, {response.text}")
        response.raise_for_status()
    return response.text

def get_persons_data(token):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    persons_data = []
    page = 0
    page_size = 500  # Ajustar según la configuración de la API si es necesario
    while True:
        url = f"{DATA_URL}?page[size]={page_size}&page[number]={page}"
        print(f"Requesting persons data with token: {token} from URL: {url}")
        response = requests.get(url, headers=headers)
        print(f"Response status code: {response.status_code}")
        print(f"Response text: {response.text}")
        if response.status_code != 200:
            print(f"Failed to get persons data: {response.status_code}, {response.text}")
            response.raise_for_status()

        try:
            data = response.json()
            print("JSON data received:")
            print(json.dumps(data, indent=4))
            if not data:
                break
            persons_data.extend(data)
            page += 1
        except json.JSONDecodeError as json_err:
            print(f"JSON decode error: {json_err}")
            break
    return persons_data

def write_to_csv(data, filename='Persons.csv'):
    if not data:
        print("No data to write.")
        return

    # Collect all possible field names
    all_keys = set()
    for item in data:
        all_keys.update(item.keys())
    
    with open(filename, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=list(all_keys))
        dict_writer.writeheader()
        for item in data:
            # Fill missing fields with None
            row = {key: item.get(key, None) for key in all_keys}
            dict_writer.writerow(row)

def main():
    try:
        token = get_access_token()
        print(f"Access token received: {token}")
        persons_data = get_persons_data(token)
        write_to_csv(persons_data)
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except json.JSONDecodeError as json_err:
        print(f"JSON decode error: {json_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

if __name__ == "__main__":
    main()
