from city_functions import city_country

def test_city_country():
    """Does a simple city and country pair work?"""
    santiago_chile = city_country('santiago', 'chile')
    assert santiago_chile == 'Santiago, Chile'