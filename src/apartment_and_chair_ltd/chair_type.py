from collections import Counter
from helpers import get_project_root

class ChairType:
    def __init__(self, floor_plan):

        if floor_plan is None:
            raise Exception("Floor plan has to be provided")
    
        self.floor_plan = floor_plan

    def _get_chair_types_per_apartment(self):

        floor_plan_counter = dict(Counter(self.floor_plan))
        floor_plan_counter = {r: floor_plan_counter[r] for r in sorted(floor_plan_counter, key=floor_plan_counter.get, reverse=True)}

        chair_types = ['W', 'P', 'S', 'C']
        chair_types_per_apartment = [f"{key}: {value}" for key, value in floor_plan_counter.items() if key in chair_types]
        chair_types_per_apartment =", ".join(chair_types_per_apartment)
        
        new_line = '\n'
        return f"total:{new_line} {chair_types_per_apartment}"

    def _get_chair_types_per_room(self):
        pass