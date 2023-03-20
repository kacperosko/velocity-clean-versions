import os
from pathlib import Path
from bin.printcolors import PrintColors


# Create an instance of PrintColors to call print methods inside
clr = PrintColors()

# Define directory to root of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Path to directory where temporary CSV files are saving
TEMP_CSV_DIR = os.path.join(BASE_DIR, "bin", "temp")
