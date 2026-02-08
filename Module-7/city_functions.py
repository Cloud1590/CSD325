def city_country(city, country, population=None, language=None):
    """Return formatted city information."""
    if population and language:
        return f"{city.title()}, {country.title()} - population {population}, {language.title()}"
    return f"{city.title()}, {country.title()}"
# Function calls (required for screenshots)
print(city_country("santiago", "chile"))
print(city_country("paris", "france"))
print(city_country("tokyo", "japan"))
