import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

def google_search(params):
    url = "https://www.googleapis.com/customsearch/v1"
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raises an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None

def search_google(query, city, region):
    api_key = os.getenv('GOOGLE_API_KEY')
    cse_id = os.getenv('CUSTOM_SEARCH_ENGINE_ID')
    print(query, city, region, api_key, cse_id)

    if not api_key or not cse_id:
        print('Could not')
        return {'error': 'API key or Custom Search Engine ID not found.'}

    params = {
        'q': f"Onde comprar {query} em {city} {region}",
        'key': api_key,
        'cx': cse_id,
        'filter': '1',
        'gl': 'BR',
        'hl': 'pt',
        'lr': 'lang_pt',
        'googlehost': 'google.com.br'
    }

    results = google_search(params)
    if results:
        items = results.get('items', [])
        formatted_items = []
        for item in items:
            title = item.get('title', 'N/A')
            snippet = item.get('snippet', 'N/A')
            link = item.get('link', 'N/A')
            image = item['pagemap']['cse_image'][0]['src'] if 'cse_image' in item['pagemap'] else 'N/A'
            formatted_items.append({
                'title': title,
                'snippet': snippet,
                'link': link,
                'image': image
            })
        print('enviou')
        json_data = json.dumps(formatted_items, indent=4)
        return formatted_items
    else:
        return {'error': 'No results found.'}

