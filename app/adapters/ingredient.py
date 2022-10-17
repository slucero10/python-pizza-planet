from typing import List

from ..repositories.models import Ingredient

class IngredientAdapter:
    def get_ingredients_from_txt(file_path: str) -> List[Ingredient]:
        try:
            with open(file_path, 'r') as file:
                ingredients = []
                while (line := file.readline().rstrip()):
                    line_arr = line.split(';')
                    ingredients.append(Ingredient(name=line_arr[0], price=float(line_arr[1])))
                return ingredients
        except Exception as e:
            raise Exception(str(e))