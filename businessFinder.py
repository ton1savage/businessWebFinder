import requests

def area_code_to_coordinates(area_code):
    # Your API key for Google Geocoding API
    api_key = 'AIzaSyBIJG0MXNpRmUK0_yGd9qQDNpE7D83rYp4'

    # API endpoint for Geocoding API
    url = 'https://maps.googleapis.com/maps/api/geocode/json'

    # Parameters for the request
    params = {
        'address': area_code,
        'key': api_key
    }

    # Sending HTTP GET request to the API
    response = requests.get(url, params=params)


    # Checking if the request was successful
    if response.status_code == 200:
        # Parsing JSON response
        data = response.json()

        # Extracting latitude and longitude from the response
        if data['status'] == 'OK' and len(data['results']) > 0:
            location = data['results'][0]['geometry']['location']
            latitude = location['lat']
            longitude = location['lng']
            return latitude, longitude
        else:
            print("Geocoding API returned no results for the area code:", area_code)
            return None
    else:
        print('Error:', response.status_code)
        return None

def find_small_businesses_by_coordinates(latitude, longitude, keyword):
    # Your API key for Google Places API
    api_key = 'AIzaSyDTJtZ2N1iLs4ARYgd7ZrBjzlG6C2c_Dsc'

    # API endpoint
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'

    # Parameters for the request
    params = {
        'keyword': keyword,
        'location': f"{latitude},{longitude}",  # Use latitude and longitude coordinates
        'radius': 10000,  # Search within 10km radius
        'type': 'point_of_interest',  # Limit search to points of interest
        'rankby': 'prominence',  # Order results by prominence
        'key': api_key
    }

    # Sending HTTP GET request to the API
    response = requests.get(url, params=params)

    # Checking if the request was successful
    if response.status_code == 200:
        # Parsing JSON response
        data = response.json()

        # Extracting relevant information from the response
        businesses = []
        for result in data['results']:
            business_name = result['name']
            business_address = result.get('vicinity', 'Address not available')
            rating = result.get('rating', 'Rating not available')
            website = get_business_website(result['place_id'])
            businesses.append({'name': business_name, 'address': business_address, 'rating': rating, 'website': website})

        # Sort businesses by rating (lowest first)
        businesses.sort(key=lambda x: x['rating'] or float('inf'))

        return businesses
    else:
        print('Error:', response.status_code)
        return None

def get_business_website(place_id):
    # Your API key for Google Places API
    api_key = 'AIzaSyDTJtZ2N1iLs4ARYgd7ZrBjzlG6C2c_Dsc'

    # API endpoint for Place Details
    url = 'https://maps.googleapis.com/maps/api/place/details/json'

    # Parameters for the request
    params = {
        'place_id': place_id,
        'fields': 'website',
        'key': api_key
    }

    # Sending HTTP GET request to the API
    response = requests.get(url, params=params)

    # Checking if the request was successful
    if response.status_code == 200:
        # Parsing JSON response
        data = response.json()

        # Extracting website from the response
        result = data.get('result', {})
        website = result.get('website', 'Website not available')
        return website
    else:
        print('Error:', response.status_code)
        return 'Website not available'
    
def find_small_businesses_by_area_code(area_code, keyword):
    # Convert area code to coordinates
    coordinates = area_code_to_coordinates(area_code)
    if coordinates is None:
        return None

    # Call the function to find businesses by coordinates
    return find_small_businesses_by_coordinates(coordinates[0], coordinates[1], keyword)

# Prompt the user to enter an area code and a keyword
area_code = input("Enter an area code: ")
keyword = input("Enter a keyword for the type of small businesses you're interested in: ")

# Example usage
small_businesses = find_small_businesses_by_area_code(area_code, keyword)

if small_businesses:
    print("Small Businesses in the area with area code", area_code, "that might need a new website:")
    for business in small_businesses:
        print("Name:", business['name'])
        print("Address:", business['address'])
        print("Rating:", business['rating'])
        print("Website:", business['website'])
        print()
else:
    print("No small businesses found in the area with area code", area_code)