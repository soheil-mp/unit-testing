
import os
import sys
from pathlib import Path

# print("============>", os.getcwd())

# # This assumes that your working directory is the root of the project.
# # sys.path.append(str(Path(__file__).parents[3] / 'src'))

sys.path.append(os.getcwd())
# print("============>", os.getcwd())

from src.features.feature_extraction import *


def test_do_something():
    assert do_something(1, 1) == 2