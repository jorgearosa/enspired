from pathlib import Path
from src.apartment_and_chair_ltd.helpers import read_in_file, get_project_root, write_out_file

class TestHelpers:

    INPUT_FILE='rooms.txt'
    OUTPUT_FILE='rooms_test_output.txt'
    
    def test_read_in_file(self):
        input = read_in_file(Path(get_project_root(), TestHelpers.INPUT_FILE))
        assert len(input.loc[input['+-----------+------------------------------------+'].str.contains("W", case=False)])==7

    def test_write_out_file(self):
        input = read_in_file(Path(get_project_root(), TestHelpers.INPUT_FILE))
        write_out_file(data=input, filename=Path(get_project_root(), TestHelpers.OUTPUT_FILE))
        df_check_output = read_in_file(Path(get_project_root(), TestHelpers.OUTPUT_FILE))
        assert len(df_check_output.loc[df_check_output['+-----------+------------------------------------+'].str.contains("W", case=False)])==7