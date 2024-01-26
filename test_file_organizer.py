import shutil
from os import sep
from pathlib import Path
from file_organizer import FileOrganizer, Controller

test_dir = Path('sandbox') / 'test_dir'
if test_dir.exists():
    shutil.rmtree(test_dir)
shutil.copytree(Path('sandbox') / 'test_dir_example', test_dir)

print(f'Running test on {test_dir}')
organizer = FileOrganizer('sandbox' + sep + 'test_dir')
controller = Controller(organizer)
controller.run()
