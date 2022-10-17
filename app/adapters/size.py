from typing import List

from ..repositories.models import Size

class SizeAdapter:
    def get_sizes_from_txt(file_path: str) -> List[Size]:
        try:
            with open(file_path, 'r') as file:
                sizes = []
                while (line := file.readline().rstrip()):
                    line_arr = line.split(';')
                    sizes.append(Size(name=line_arr[0], price=float(line_arr[1])))
                return sizes
        except Exception as e:
            raise Exception(str(e))