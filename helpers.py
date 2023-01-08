
import pyautogui as gui
import math
import time
import os

def wait_until_img_appears_or_dodge_occurs(image_paths, max_tries=3, confidence=0.9, exit_on_fail=False, sleep_time_sec=1):
    try_count = 0
    location = None
    game_dodged = None

    while not location and try_count < max_tries:
        for img_path in image_paths:
            location = gui.locateCenterOnScreen(os.path.join("./img", img_path), confidence=confidence)
            if location:
                break

            game_dodged = gui.locateCenterOnScreen(os.path.join("./img", "home.png"), confidence=confidence)
            if game_dodged:
                break

            time.sleep(sleep_time_sec)
            try_count += 1

    if game_dodged:
        return None, True

    if exit_on_fail and not location:
        exit("Failed to find any of the following images: {}".format(image_paths))

    return location, False

