import unittest
from helpers import *

class TestImageDetection(unittest.TestCase):
    # def test_cannot_see_image_and_will_return_none(self):
    #     x, dodged = wait_until_img_appears_or_dodge_occurs(["find_match.png"], max_tries=1, confidence=0.99)
    #     # self.assertIsNone(x)
    #     gui.moveTo(x[0]-50, x[1])
    #     print(x)
    #     self.assertFalse(dodged)

    def test_insult_ryan(self):
            x = wait_until_img_appears(["chat.png"], math.inf)
            gui.click(x)
            gui.write(generate_random_insult("Ryan"), random.uniform(0.05, 0.15))
            gui.press("enter")

if __name__ == '__main__':
    unittest.main()
