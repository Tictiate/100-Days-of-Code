from bs4 import BeautifulSoup
import requests

class souping_data:
    def __init__(self):
        response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
        site = response.text

        self.soup = BeautifulSoup(site, "html.parser")

    def collect_data(self):
        properties = self.soup.find_all(name="a", class_="property-card-link")
        property_links = [link['href'] for link in properties]

        property_addresses_cards = self.soup.find_all(name="address")
        property_addresses = [address.getText() for address in property_addresses_cards]

        property_price_cards = self.soup.find_all(name="div", class_="PropertyCardWrapper")
        property_prices = [price.getText() for price in property_price_cards]

        for i in range(len(property_prices)):
            s = property_prices[i][1:-1]  # remove first & last char
            s = s.replace("+", "")
            property_prices[i] = s

        for i in range(len(property_addresses)):
            s = property_addresses[i][1:-1]
            s = s.replace("|", "")
            property_addresses[i] = s.strip()

        return property_links, property_prices, property_addresses