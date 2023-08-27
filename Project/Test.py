from unittest import TestCase, main
from ClearMessage import clearBanWord

class TestClearMessage(TestCase):

    def test_clearBanWord(self):
        self.assertEqual(clearBanWord("лист"), "****")


if __name__ == "__main__":
    main()
    