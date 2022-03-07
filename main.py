from bs4 import BeautifulSoup
import requests

link = 'https://www.southwest.com/air/booking/select.html?adultPassengersCount=1&departureDate=2022-04-19&departureTimeOfDay=ALL_DAY&destinationAirportCode=ONT&fareType=USD&int=LFCBOOKAIR&originationAirportCode=DEN&passengerType=ADULT&promoCode=&returnAirportCode=&returnDate=2022-04-26&returnTimeOfDay=ALL_DAY&selectedFlight1=2022-04-20&selectedFlight2=2022-04-26&tripType=roundtrip'

source = requests.get(link).text

soup = BeautifulSoup(source, 'lxml')

print(soup)