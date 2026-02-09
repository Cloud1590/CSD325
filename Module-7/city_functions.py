def city_country(city, country, population=None, language=None):
    """Return formatted city information."""
    result = f"{city.title()}, {country.title()}"

    if population:
        result += f" - population {population}"

    if language:
        result += f", {language.title()}"

    return result


# Required function calls
print(city_country("santiago", "chile"))
print(city_country("santiago", "chile", 5000000))
print(city_country("santiago", "chile", 5000000, "spanish"))
