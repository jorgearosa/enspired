from pathlib import Path
import pytest
from src.apartment_and_chair_ltd.helpers import read_in_file, get_project_root
from src.apartment_and_chair_ltd.chair_type import ChairType

class TestChairType:

    INPUT_FILE='rooms.txt'

    def test_floor_plan_none(self):
        with pytest.raises(Exception) as excinfo:
            ChairType(floor_plan=None)
        assert str(excinfo.value) == "Floor plan has to be provided"

    def test_floor_plan_per_apartment(self):
        input = read_in_file(Path(get_project_root(), TestChairType.INPUT_FILE))
        chair_type = ChairType(input)._get_chair_types_per_apartment()
        assert chair_type == 'total:\n W: 14, P: 7, S: 3, C: 1'

    def test_floor_plan_per_room(self):
        input = read_in_file(Path(get_project_root(), TestChairType.INPUT_FILE))
        chair_type = ChairType(input)._get_chair_types_per_room()
        assert chair_type == 'total:\n W: 14, P: 7, S: 3, C: 1'