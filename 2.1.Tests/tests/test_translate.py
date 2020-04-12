import unittest

import translate_ya


class Translate(unittest.TestCase):

    def test_translate_it(self):
        self.assertEqual(translate_ya.translate('hi', 'ru')['text'][0], 'привет')

    def test_code(self):
        self.assertEqual(translate_ya.translate('hi', 'ru')['code'], 200)

    def test_wrong_to_lang(self):
        self.assertEqual(translate_ya.translate('en', 'dfgbgf')['code'], 501)


if __name__ == '__main__':
    unittest.main()
