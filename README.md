Small Business Finder

Overview

This script helps find small businesses in a given area code that might need a new website. It uses the Google Geocoding API to convert area codes to latitude and longitude coordinates and the Google Places API to search for businesses based on a given keyword.

Features

Converts an area code into geographical coordinates.

Searches for small businesses using the Google Places API.

Retrieves business names, addresses, ratings, and website URLs.

Sorts businesses by rating, listing those with the lowest ratings first.

Prerequisites

Before using this script, ensure you have the following:

Python installed on your machine.

An API key for the Google Geocoding API.

An API key for the Google Places API.

The requests library installed (install using pip install requests).

Installation

Clone the Repository

git clone https://github.com/yourusername/small-business-finder.git
cd small-business-finder

Install Dependencies

pip install -r requirements.txt

Set Up API Keys

Open script.py in a text editor.

Replace 'Enter API key here' with your actual Google API keys.

Usage

Run the Script

python script.py

Provide Inputs

Enter an area code when prompted.

Enter a keyword for the type of business you are searching for (e.g., "restaurant", "plumber", "salon").

The script will return a list of small businesses in that area, including:

Business name

Address

Rating

Website (if available)

Example Output

Enter an area code: 94102
Enter a keyword for the type of small businesses you're interested in: bakery
Small Businesses in the area with area code 94102 that might need a new website:

Name: Joe's Bakery
Address: 123 Main St, San Francisco, CA
Rating: 3.5
Website: Website not available

Name: Sweet Delights
Address: 456 Market St, San Francisco, CA
Rating: 4.2
Website: http://sweetdelights.com

Notes

The script sorts businesses by rating in ascending order, helping to identify businesses that may need improvement.

If no businesses are found, the script will notify the user.

License

This project is licensed under the MIT License.

Author

Ethan Robinson
