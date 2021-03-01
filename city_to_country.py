from allcities import cities
import pycountry


def city_to_country(city):
    filtered_city_set = cities.filter(name=city, population='>500000')
    largest_city = next(iter(filtered_city_set))
    if largest_city.dict['country_code'] in [country.alpha_2 for country in list(pycountry.countries)]:
        country_code = largest_city.dict['country_code']
        return country_code
