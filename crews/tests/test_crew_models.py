import pytest

from crews.models import Crew

@pytest.mark.django_db
def test_crew_str():
    crew = Crew(first_name="Albert", last_name="Krylov")
    assert str(crew) == "Albert Krylov"