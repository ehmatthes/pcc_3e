from city_functions_pop_optional import city_country

def test_city_country():
    """Does a simple city and country pair work?"""
    santiago_chile = city_country('santiago', 'chile')
    assert santiago_chile == 'Santiago, Chile'

def test_city_country_population():
    """Can I include a population argument?"""
    santiago_chile = city_country('santiago', 'chile', population=5_000_000)
    assert santiago_chile == 'Santiago, Chile - population 5000000'