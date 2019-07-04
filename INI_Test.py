from INI import INI
import unittest

class INI_Test(unittest.TestCase):
    def setUp(self) :
        sample1 = """
       [general]
       appname = configparser
       version=0.1
       [author]
       name =xmonader
       email =notxmonader@gmail.com
       """
        sample1.strip()
        self.ini=INI(sample1)

    def testIsKeyVal(self):
        self.assertEqual(self.ini.is_keyval("omar = ok"),True)
        self.assertEqual(self.ini.is_keyval("hhhhhhh"),False)
        self.assertEqual(self.ini.is_keyval("[profile]"),False)
        self.assertEqual(self.ini.is_keyval("#codescalers"), False)
        self.assertEqual(self.ini.is_keyval(""), False)
    def testIsSection(self):
        self.assertEqual(self.ini.is_section("omar = ok"), False)
        self.assertEqual(self.ini.is_section("hhhhhhh"), False)
        self.assertEqual(self.ini.is_section("[profile]"), True)
        self.assertEqual(self.ini.is_section("#codescalers"), False)
        self.assertEqual(self.ini.is_section(""), False)
    def testIsEmpty(self):
        self.assertEqual(self.ini.is_empty("omar = ok"), False)
        self.assertEqual(self.ini.is_empty("hhhhhhh"), False)
        self.assertEqual(self.ini.is_empty("[profile]"), False)
        self.assertEqual(self.ini.is_empty("#codescalers"), False)
        self.assertEqual(self.ini.is_empty(""), True)
    def testGetInformation(self):
        self.assertEqual(self.ini.get_properity("general","version"),"0.1")
        self.assertEqual(self.ini.get_properity("author","email"),"notxmonader@gmail.com")
        self.assertEqual(self.ini.has_properity("author","email"),True)
        self.assertEqual(self.ini.has_properity("author","hhhhhh"),False)
        self.assertEqual(self.ini.has_properity("ggggg","hhhhh"),False)
        self.assertEqual(self.ini.has_section("author"),True)
        self.assertEqual(self.ini.has_section("hhhhhh"),False)


if __name__ == '__main__':
    unittest.main()
