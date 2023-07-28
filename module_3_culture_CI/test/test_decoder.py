from module_3_culture_CI.decoder import decrypt, code_list, for_test_dict
import unittest


class TestDecoder(unittest.TestCase):


    def test_get_schifr(self):
        for i, k in for_test_dict.items():
            self.assertEqual(decrypt(i), k)
        # self.assertEquals(decrypt(i), 'абра-кадабра')
        # self.assertEquals(decrypt('абраа..-кадабра'), 'абра-кадабра')
        # self.assertEquals(decrypt('абраа..-.кадабра'), 'абра-кадабра')
        # self.assertEquals(decrypt('абрау...-кадабра'), 'абра-кадабра')
        # self.assertEquals(decrypt('абра........'), '')
        # self.assertEquals(decrypt('абр......a.'), 'a')
        # self.assertEquals(decrypt('1..2.3'), '23')
        # self.assertEquals(decrypt('.'), '')

