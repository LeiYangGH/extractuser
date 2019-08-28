import unittest
from tidy_user_loc import keep_first_section,keep_key_jpa,tidy_locnums_comma2tab

class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, False)
    # def test_keep_first_section(self):
    #     line = r'1916Linux	Co. Aontroim/Antrim 脡ire/Ireland 馃嚠馃嚜'
    #     line = keep_first_section(line)
    #     print(line)
    #     self.assertEqual(False, 'Antrim' in line)
    #     self.assertEqual(False, '/' in line)
    # def test_keep_key_jpa(self):
    #     line = r'BUTANiTRO	東京ピッグランド(仮設中)'
    #     line = keep_key_jpa(line)
    #     print(line)
    #     self.assertEqual(False, '仮設中' in line)
    #     self.assertEqual(False, 'ピッグランド' in line)
    #     self.assertEqual(True, '東京' in line)
    #
    # def test_keep_key_jpa_nums(self):
    #     line = r'tenmei0	東京都2.1次元'
    #     line = keep_key_jpa(line)
    #     print(line)
    #     self.assertEqual(False, '次元' in line)
    #     self.assertEqual(False, '2.1' in line)
    #     self.assertEqual(True, '東京' in line)

    def test_tidy_locnums_comma2tab(self):
        line = r'43army	49.225402,-122.916518'
        line = tidy_locnums_comma2tab(line)
        print(line)
        self.assertEqual(False, ',' in line)
        self.assertEqual(True, '\t' in line)
if __name__ == '__main__':
    unittest.main()
