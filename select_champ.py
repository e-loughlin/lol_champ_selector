from helpers import *
import random
import pyautogui as gui
import time
import argparse
import math

def rt():
    return random.uniform(0,1)

if __name__ == "__main__":

    CLI=argparse.ArgumentParser()
    CLI.add_argument(
    "--champs",  # name on the CLI - drop the `--` for positional/required parameters
    nargs="*",  # 0 or more values expected => creates a list
    type=str,
    default=[],  # default if nothing is provided
    )
    CLI.add_argument(
    "--bans",
    nargs="*",
    type=str,  # any type/callable can be used here
    default=[],
    )
    args = CLI.parse_args()
    # access CLI options

    if len(args.champs) == 0:
        exit("You must select at least 1 champ to select.")
    if len(args.bans) == 0:
        exit("You must select at least 1 champ to ban.")

    print("Champs (Order of Priority): %r" % args.champs)
    print("Bans (Order of Priority): %r" % args.bans)

    print("LoL Auto Game Starter: Ensure you have clicked \"Start Match\"...")
    time.sleep(3)

    while(True):
        print("Waiting for queue pop...")
        x, dodged = wait_until_img_appears_or_dodge_occurs(["accept.png"], math.inf)
        if x:
            print("Game accepted!")
            gui.click(x, interval=rt())
        if dodged:
            continue

        print("Waiting for champ pre-select...")
        # Pre-Select your Champ
        #TODO: Iterate through multiple possible champs to select
        x, dodged = wait_until_img_appears_or_dodge_occurs(["search.png"], math.inf)
        if dodged: 
            continue
        gui.click(x, interval=rt())
        gui.write(args.champs[0], interval=random.uniform(0.1, 0.25))
        x, dodged = wait_until_img_appears_or_dodge_occurs(["champ_box.png"], math.inf)
        gui.click(x, interval=rt())
        print("Champ Selected...")
        if dodged: 
            continue

        # Ban A Champ
        print("Waiting for Bans...")
        # TODO: Iterate over list of bans
        x, dodged = wait_until_img_appears_or_dodge_occurs(["ban_a_champ.png"], math.inf)
        if dodged: 
            continue
        x, dodged = wait_until_img_appears_or_dodge_occurs(["search.png"], math.inf)
        if dodged: 
            continue
        gui.click(x, interval=rt())
        gui.write(args.bans[0], interval=random.uniform(0.1, 0.25))
        x, dodged = wait_until_img_appears_or_dodge_occurs(["ban_border.png"], math.inf)
        if dodged: 
            continue
        gui.click(x, interval=rt())
        x, dodged = wait_until_img_appears_or_dodge_occurs(["ban_button.png"], math.inf)
        if dodged: 
            continue
        gui.click(x, interval=rt())
        print("Champ Banned...")

        # Lock In Your Champ
        x, dodged = wait_until_img_appears_or_dodge_occurs(["pick_your_champion.png", "pick_your_champion_2.png"], math.inf)
        if dodged: 
            continue
        x, dodged = wait_until_img_appears_or_dodge_occurs(["search.png"], math.inf)
        if dodged: 
            continue
        gui.click(x, interval=rt())

        x, dodged = wait_until_img_appears_or_dodge_occurs(["lock_in.png"], math.inf)
        if dodged: 
            continue
        print("Locked In!")
        gui.click(x, interval=rt())