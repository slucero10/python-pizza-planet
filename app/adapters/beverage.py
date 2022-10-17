from typing import List

from ..repositories.models import Beverage

class BeverageAdapter:
    def get_beverages_from_txt(file_path: str) -> List[Beverage]:
        try:
            with open(file_path, 'r') as file:
                beverages = []
                while (line := file.readline().rstrip()):
                    line_arr = line.split(';')
                    beverages.append(Beverage(name=line_arr[0], size=float(line_arr[1]), price=float(line_arr[2])))
                return beverages
        except Exception as e:
            raise Exception(str(e))
