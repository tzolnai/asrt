# !/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright (C) <2019>  <Tamás Zolnai>    <zolnaitamas2000@gmail.com>

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import os
# Add the local path to the main script and external scripts so we can import them.
sys.path = [".."] + \
    [os.path.join("..", "externals", "psychopy_mock")] + sys.path

import unittest
import asrt
import psychopy_gui_mock as pgm


class showGroupSettingsDialogTest(unittest.TestCase):

    def testDefault(self):
        gui_mock = pgm.PsychoPyGuiMock()

        exp_settings = asrt.ExperimentSettings("", "")
        exp_settings.show_group_settings_dialog(2)

        self.assertEqual(len(exp_settings.groups), 2)

        list_of_texts = gui_mock.getListOfTexts()
        self.assertEqual(len(list_of_texts), 1)
        self.assertEqual(
            list_of_texts[0], "A csoportok megnevezése a következő (pl. kísérleti, kontroll, ....) ")

        list_of_fields = gui_mock.getListOfFields()
        self.assertEqual(len(list_of_fields), 2)
        self.assertEqual(list_of_fields[0].label, "Csoport 1")
        self.assertEqual(list_of_fields[1].label, "Csoport 2")

    def testMoreGropus(self):
        gui_mock = pgm.PsychoPyGuiMock()
        numgroups = 3
        exp_settings = asrt.ExperimentSettings("", "")
        exp_settings.show_group_settings_dialog(numgroups)

        self.assertEqual(len(exp_settings.groups), numgroups)

        list_of_texts = gui_mock.getListOfTexts()
        self.assertEqual(len(list_of_texts), 1)
        self.assertEqual(
            list_of_texts[0], "A csoportok megnevezése a következő (pl. kísérleti, kontroll, ....) ")

        list_of_fields = gui_mock.getListOfFields()
        self.assertEqual(len(list_of_fields), numgroups)
        self.assertEqual(list_of_fields[0].label, "Csoport 1")
        self.assertEqual(list_of_fields[1].label, "Csoport 2")
        self.assertEqual(list_of_fields[2].label, "Csoport 3")

    def testNoGroup(self):
        gui_mock = pgm.PsychoPyGuiMock()
        numgroups = 0
        exp_settings = asrt.ExperimentSettings("", "")
        exp_settings.show_group_settings_dialog(numgroups)

        self.assertEqual(len(exp_settings.groups), 1)
        self.assertEqual(exp_settings.groups[0], "nincsenek csoportok")

        list_of_texts = gui_mock.getListOfTexts()
        self.assertEqual(len(list_of_texts), 0)

        list_of_fields = gui_mock.getListOfFields()
        self.assertEqual(len(list_of_fields), numgroups)

    def testCancel(self):
        gui_mock = pgm.PsychoPyGuiMock()
        gui_mock.setReturnValue(False)
        numgroups = 2
        exp_settings = asrt.ExperimentSettings("", "")

        with self.assertRaises(SystemExit):
            exp_settings.show_group_settings_dialog(numgroups)

    def testAccentCharacters(self):
        gui_mock = pgm.PsychoPyGuiMock()
        gui_mock.addFieldValues(["áaéeíióoőöúuűüÁAÉEÍIÓOŐÖÚUŰÜ", "kontrol"])
        numgroups = 2
        exp_settings = asrt.ExperimentSettings("", "")
        exp_settings.show_group_settings_dialog(numgroups)

        self.assertEqual(len(exp_settings.groups), numgroups)
        self.assertEqual(
            exp_settings.groups[0], "aaeeiioooouuuuaaeeiioooouuuu")
        self.assertEqual(exp_settings.groups[1], "kontrol")

    def testSpecialCharacters(self):
        gui_mock = pgm.PsychoPyGuiMock()
        gui_mock.addFieldValues(
            ["áaéeíió-oőö-úuű-üÁ AÉEÍ IÓOŐ ÖÚUŰÜ", "kontrol"])
        numgroups = 2
        exp_settings = asrt.ExperimentSettings("", "")
        exp_settings.show_group_settings_dialog(numgroups)

        self.assertEqual(len(exp_settings.groups), numgroups)
        self.assertEqual(
            exp_settings.groups[0], "aaeeiio_ooo_uuu_ua_aeei_iooo_ouuuu")
        self.assertEqual(exp_settings.groups[1], "kontrol")


if __name__ == "__main__":
    unittest.main()  # run all tests
