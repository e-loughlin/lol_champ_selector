
import pyautogui as gui
import math
import time
import os
import random

def wait_until_img_appears(image_paths, max_tries=3, confidence=0.94, exit_on_fail=False, sleep_time_sec=1):
    try_count = 0
    location = None

    while not location and try_count < max_tries:
        for img_path in image_paths:
            location = gui.locateCenterOnScreen(os.path.join("./img", img_path), confidence=confidence)
            if location:
                break

            time.sleep(sleep_time_sec)
            try_count += 1

    if exit_on_fail and not location:
        exit("Failed to find any of the following images: {}".format(image_paths))

    return location

def wait_until_img_appears_or_dodge_occurs(image_paths, max_tries=3, confidence=0.94, exit_on_fail=False, sleep_time_sec=1):
    try_count = 0
    location = None
    game_dodged = None

    while not location and try_count < max_tries:
        for img_path in image_paths:
            location = gui.locateCenterOnScreen(os.path.join("./img", img_path), confidence=confidence)
            if location:
                break

            can_see_home_screen = gui.locateCenterOnScreen(os.path.join("./img", "in_queue.png"), confidence=0.98)
            if can_see_home_screen:
                # TODO: Add another screenshot for after you've accepted
                can_accept_queue = gui.locateCenterOnScreen(os.path.join("./img", "accept.png"), confidence=0.98)
                have_accepted_queue = gui.locateCenterOnScreen(os.path.join("./img", "have_accepted.png"), confidence=0.98)
                game_dodged = not (can_accept_queue or have_accepted_queue)
                if game_dodged:
                    return None, True

            time.sleep(sleep_time_sec)
            try_count += 1

    if exit_on_fail and not location:
        exit("Failed to find any of the following images: {}".format(image_paths))

    return location, False

def generate_random_insult(name):
    with open('./other/insults.txt') as f:
        lines = f.read().splitlines()
    return "Hey {}: {}".format(name, random.choice(lines))

def generate_random_fact():
    with open('./other/facts.txt') as f:
        lines = f.read().splitlines()
    return "Random Fact: {}".format(random.choice(lines))