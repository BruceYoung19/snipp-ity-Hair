import pytest

def test_haircut_creation():
    # GIVEN valid haircut details
    haircut_id = 1
    description = "Buzz Cut"
    cost = 25.0

    # WHEN a Haircut object is created
    haircut = Haircut(haircut_id, description, cost)

    # THEN the Haircut should have the correct attributes
    assert haircut.haircut_id == haircut_id
    assert haircut.description == description
    assert haircut.cost == cost


def test_haircut_invalid_cost_type():
    # GIVEN an invalid cost type (string instead of float)
    # WHEN creating a Haircut with invalid cost
    # THEN it should raise a ValueError (if validation is added)
    with pytest.raises(ValueError):
        Haircut(1, "Buzz Cut", "twenty-five")

