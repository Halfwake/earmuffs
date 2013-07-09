#Copyright 2013 Andrew Dudash
# 
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.

import unittest

import earmuffs

class TestEarmuffs(unittest.TestCase):
    def setUp(self):
        earmuffs._environment = {}
    def test_defparameter(self):
        self.assertEqual(earmuffs.defparameter(a = 3, b = 4), {'a' : 3, 'b' : 4})
    def test_earmuffs(self):
        earmuffs.defparameter(a = 3, b = 4), {'a' : 3, 'b' : 4}
        self.assertEqual(earmuffs.earmuffs('a'), 3)
        self.assertEqual(earmuffs.earmuffs('b'), 4)
    def test_defvar(self):
        earmuffs.defparameter(a = 3)
        earmuffs.defvar(a = 4)
        self.assertEqual(earmuffs.earmuffs('a'), 3)
        self.assertEqual(earmuffs.defvar(b = 0), {'b' : 0})
        self.assertEqual(earmuffs.earmuffs('b'), 0)
    def test_let(self):
        earmuffs.defparameter(name = 'zack')
        def show_name():
            return earmuffs.earmuffs('name')
        with earmuffs.let(name = 'kelly'):
            self.assertEqual(show_name(), 'kelly')
        with earmuffs.let(name = 'kelly'):
            with earmuffs.let(name = 'johnson'):
                self.assertEqual(show_name(), 'johnson')
        def change_name_and_call(new_name, func):
            with earmuffs.let(name = new_name):
                return func()
        self.assertEqual(change_name_and_call('kelly', show_name), 'kelly')
        with earmuffs.let(name = 'kelly'):
            self.assertEqual(change_name_and_call('johnson', show_name), 'johnson')
            
if __name__ == '__main__':
    unittest.main()
