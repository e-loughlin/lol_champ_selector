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
    "--champs", 
    nargs="*",
    type=str,
    default=[],  
    )
    CLI.add_argument(
    "--bans",
    nargs="*",
    type=str, 
    default=[],
    )
    CLI.add_argument(
    "--insult",
    type=str,  
    default=None,
    )
    CLI.add_argument(
    "--fact",
    type=bool,  
    default=False,
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

    while(True):
        preselect_champ = args.champs[0]
        print("Waiting for queue pop...")
        x = wait_until_img_appears(["accept.png"], math.inf)
        if x:
            print("Game accepted!")
            gui.click(x, interval=rt())
        else:
            continue

        print("Regaining focus on League Screen...")
        print("Make sure no other windows are in front of the champ select window, or this will fail...")
        
        time.sleep(4)

        print("Waiting for champ pre-select...")
        # Pre-Select your Champ
        x, dodged = wait_until_img_appears_or_dodge_occurs(["search.png"], math.inf)
        if dodged: 
            continue
        gui.click(x, clicks=2)
        gui.press('backspace')
        gui.write(preselect_champ, interval=random.uniform(0.1, 0.25))
        x, dodged = wait_until_img_appears_or_dodge_occurs(["champ_box.png"], max_tries=1)
        if dodged: 
            continue
        if x:
            gui.click(x, interval=rt())
            print("Champ {} Pre-Selected...".format(args.champs[0]))
        else:
            print("Champ {} not found...".format(args.champs[0]))

        # Ban A Champ
        print("Waiting for Bans...")
        for ban in args.bans:
            print("Attempting to ban {}".format(ban))
            x, dodged = wait_until_img_appears_or_dodge_occurs(["ban_a_champ.png"], math.inf)
            if dodged: 
                break
            x, dodged = wait_until_img_appears_or_dodge_occurs(["search.png"], math.inf)
            if dodged: 
                break
            gui.click(x, clicks=2)
            gui.press('backspace')
            gui.write(ban, interval=random.uniform(0.05, 0.1))
            x, dodged = wait_until_img_appears_or_dodge_occurs(["ban_border.png"], 2)
            if dodged: 
                break
            if not x:
                print("Could not ban {}".format(ban))
                continue
            gui.click(x[0]-25, x[1], interval=rt(), clicks=2)
            x, dodged = wait_until_img_appears_or_dodge_occurs(["ban_button.png"], 2)
            if dodged: 
                break
            if not x:
                print("Could not ban {}".format(ban))
                continue
            gui.click(x, interval=rt())
            print("Champ {} Banned...".format(ban))
            break

        if dodged:
            continue

        # Lock In Your Champ
        for champ in args.champs:
            print("Attempting to select {}".format(champ))
            x, dodged = wait_until_img_appears_or_dodge_occurs(["pick_your_champion.png", "pick_your_champion_2.png"], math.inf)
            if dodged: 
                break
            
            if champ != preselect_champ:
                x, dodged = wait_until_img_appears_or_dodge_occurs(["search.png"], math.inf)
                if dodged: 
                    break
                gui.click(x, clicks=2)
                gui.press('backspace')
                gui.write(champ, interval=random.uniform(0.05,0.13))

                x, dodged = wait_until_img_appears_or_dodge_occurs(["champ_box.png"], max_tries=2, confidence=0.95)
                gui.click(x, interval=rt())
                if dodged:
                    break
                if not x:
                    print("Could not select {}".format(champ))
                    continue

            x, dodged = wait_until_img_appears_or_dodge_occurs(["lock_in.png"], confidence=0.9, max_tries=2)
            if dodged: 
                break
            if not x:
                print("Could not select {}".format(champ))
                continue

            print("Locked In!")
            gui.click(x, interval=rt())
            break

        if dodged:
            continue

        if args.insult:
            x, dodged = wait_until_img_appears_or_dodge_occurs(["chat.png"], math.inf)
            if dodged:
                continue
            gui.click(x)
            gui.write(generate_random_insult(args.insult), random.uniform(0.05, 0.06))
            gui.press("enter")

        x, dodged = wait_until_img_appears_or_dodge_occurs(["top_bar.png"], math.inf)
        gui.click(x)

        if args.fact:
            x, dodged = wait_until_img_appears_or_dodge_occurs(["chat.png"], math.inf)
            if dodged:
                continue
            gui.click(x)
            gui.write(generate_random_fact(), random.uniform(0.05, 0.07))
            gui.press("enter")

        # End script if game starts
        x, dodged = wait_until_img_appears_or_dodge_occurs(["game_started.png"], math.inf)
        if dodged:
            continue
        if x:
            exit("Game started! Have fun!")
