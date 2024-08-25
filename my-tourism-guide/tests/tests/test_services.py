from app.services import get_destinations, get_destination_by_id, search_destinations

def test_get_destinations():
    destinations = get_destinations()
    assert len(destinations) > 0

def test_get_destination_by_id():
    destination = get_destination_by_id(1)
    assert destination['id'] == 1

def test_search_destinations():
    results = search_destinations('Beach')
    assert len(results) > 0
