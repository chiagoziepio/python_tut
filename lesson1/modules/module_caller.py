

# Allow importing from project root when running this file directly
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))


import nigeria
from lesson1.rps import rock_paper_scissors

print(nigeria.enugu)

nigeria.tryit()

rock_paper_scissors()