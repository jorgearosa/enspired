import click
from chair_type import ChairType
from helpers import read_in_file, write_out_file, get_project_root

@click.command()
@click.option('-f', '--floor-plan-file', required=True, type=click.Path(), help='File path to floor plan file')
@click.option('--per-apartment', default=False, type=bool, help='A boolean, true if one wants to get number of chairs per aparment')
@click.option('--per-room', default=False, type=bool, help='A boolean, true if one wants to get number of chairs per room')
def get_chair_plan(floor_plan_file, per_apartment, per_room):
    """Simple program that reads in a floor plan file and outputs the following information:
    1. Number of different chair types for the apartment
    2. Number of different chair types per room."""

    floor_plan=read_in_file(floor_plan_file)
    if per_apartment:
        chairs=ChairType()._get_chair_types_per_apartment(floor_plan)
        print(chairs)
    if per_room:
        chairs=ChairType()._get_chair_types_per_room(floor_plan)
        print(chairs)

if __name__ == '__main__':
    get_chair_plan()