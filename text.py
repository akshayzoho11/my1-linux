import subprocess
import sys
import time
import os

# --- 1. DEPENDENCY CHECK FIRST ---
# Removed pywinauto, pywin32, comtypes as they are Windows-only
packages = ['pyautogui', 'Pillow', 'Xlib'] 
print("Checking dependencies...")
try:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + packages)
    print("All dependencies installed.")
except subprocess.CalledProcessError as e:
    print(f"Error installing packages: {e}")
    sys.exit(1)

# --- 2. IMPORT AFTER INSTALLATION ---
import pyautogui

# --- CONFIG ---
# Ensure we are running on the virtual display provided by the YAML
if "DISPLAY" not in os.environ:
    print("Warning: DISPLAY environment variable not found. Automation might fail.")
    os.environ["DISPLAY"] = ":99"

CLICK_X, CLICK_Y = 1100, 725
WAIT_TIME = 30
SCREENSHOT_DIR = "screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

# Give Wine a moment to be ready if it's the first run
time.sleep(2)

def take_screenshot(name):
    path = os.path.join(SCREENSHOT_DIR, name)
    try:
        pyautogui.screenshot(path)
        print(f"Screenshot saved: {path}")
    except Exception as e:
        print(f"Error taking screenshot {name}: {e}")

# --- TEST SCREENSHOT ---
take_screenshot("01_after_install.png")

# --- LAUNCH INSTALLER ---
second_path = os.path.join(os.getcwd(), "install-3.exe")
print(f"Launching Second from: {second_path}")

if not os.path.exists(second_path):
    print(f"ERROR: {second_path} not found!")
    sys.exit(1)

# CHANGE: Use 'wine' to run the .exe on Linux
try:
    subprocess.Popen(['wine', second_path])
    print("Installer launched via Wine.")
except FileNotFoundError:
    print("ERROR: 'wine' command not found. Ensure it is installed in the YAML.")
    sys.exit(1)

time.sleep(30)
take_screenshot("10_after_launching_second.png")

# --- AUTOMATION SEQUENCE ---
# Note: Wine window management can be tricky. 
# You might need to adjust sleep times depending on how fast Wine loads the app.
pyautogui.press('tab')
time.sleep(10)
take_screenshot("first_tab.png")
pyautogui.press('up')
time.sleep(10)
take_screenshot("first_up.png")
pyautogui.press('space')
time.sleep(10)
take_screenshot("first_space.png")
pyautogui.press('enter')
time.sleep(10)
take_screenshot("first_enter.png")
pyautogui.press('enter')
time.sleep(10)
take_screenshot("11a_after_finishing_second.png")

pyautogui.press('tab')
time.sleep(10)
take_screenshot("second_tab.png")
pyautogui.press('space')
time.sleep(1)
take_screenshot("second_space.png")
# pyautogui.press('enter')
# time.sleep(10)

# pyautogui.press('right')
# take_screenshot("11b_after_finishing_second.png")
# time.sleep(1)

# pyautogui.press('right')
# time.sleep(1)
# take_screenshot("11c_after_finishing_second.png")

# pyautogui.press('tab')
# time.sleep(1)
# take_screenshot("11d_after_finishing_second.png")

# pyautogui.press('space')
# time.sleep(1)
# take_screenshot("11e_after_finishing_second.png")

# pyautogui.press('tab')
# time.sleep(1)
# take_screenshot("11f_after_finishing_second.png")

# pyautogui.write("AkshayKumarPandey")
# pyautogui.press('tab')
# take_screenshot("11_after_finishing_second.png")

# print("Automation completed successfully!")
