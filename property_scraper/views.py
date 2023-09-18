
from django.shortcuts import render
from .models import Property
from bs4 import BeautifulSoup
import requests

def scrape_and_save_property_data(request):
    
    url = "https://www.99acres.com/3-bhk-bedroom-independent-house-villa-for-sale-in-muthangi-hyderabad-2070-sq-ft-r1-spid-E69531748"
  
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        property_name = soup.find('h2', class_='srpTuple__tupleTitleOverflow').text
        property_cost = soup.find('td', id='srp_tuple_price').text.strip()
        property_area = soup.find('td', id='srp_tuple_primary_area').text.strip()
        property_bedroom = soup.find('td', id='srp_tuple_bedroom').text.strip()
        property_description = soup.find('div', class_='ellipsis srpTuple__smallDescriptionStyle').text.strip()

        property_instance = Property(
            name=property_name,
            cost=property_cost,
            property_type=property_bedroom,  
            area=property_area,
            locality="Muthangi",  
            city="Hyderabad",  
            link=url,
            description=property_description,
        )

        property_instance.save()

        return render(request, 'scrape_complete.html')
    
def show_property_data(request):
    properties = Property.objects.all()
    return render(request, 'property_list.html', {'properties': properties})