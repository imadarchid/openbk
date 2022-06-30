from utils.extractors import attijari, cih
from typing import List

def extract(file) -> List:
    result = cih(file)
    return result
