import shutil
import os

screenshot_dir = path
desktop_dir = path
if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)

desktop_files = os.listdir(desktop_dir)
for file in desktop_files:
    if file.startswith('Screenshot') and file.endswith('.png'):
        file_dir = desktop_dir + '/' + file
        shutil.move(file_dir, screenshot_dir)
