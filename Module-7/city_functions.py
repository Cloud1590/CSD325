# city_functions.py

def city_country(city, country, population=None, language=None):
    """Return a formatted string like 'City, Country' with optional population and language."""
    result = f"{city.title()}, {country.title()}"
    
    if population is not None:
        result += f" - population {population}"
    
    if language is not None:
        result += f", {language.title()}"
    
    return result

# Call the function at least three times with different argument combinations
if __name__ == "__main__":
    # 1. Just city and country
    print(city_country("santiago", "chile"))
    
    # 2. City, country, and population
    print(city_country("tokyo", "japan", population=37400068))
    
    # 3. City, country, population, and language
    print(city_country("paris", "france", population=2140526, language="french"))