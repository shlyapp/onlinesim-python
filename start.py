import subprocess
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

os.chdir(parent_dir)

scripts = [
    'onlinesim-python.src.example',
]

for script in scripts:
    subprocess.run(["python", "-m", script])
