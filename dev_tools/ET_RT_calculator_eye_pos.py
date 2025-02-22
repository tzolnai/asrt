# !/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright (C) <2019>  <Tamás Zolnai>  <zolnaitamas2000@gmail.com>

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
import shelve
import codecs
from io import StringIO


def convert(raw_file_name, new_file_name):

    with codecs.open(raw_file_name, 'r', encoding='utf-8') as raw_output_file:
        raw_lines = raw_output_file.readlines()
    new_file_data = StringIO()
    new_file_data.write(raw_lines[0][:len(raw_lines[0]) - 1])
    new_file_data.write('RT (samples)')
    new_file_data.write('\n')

    last_trial = "1"
    counter = 0
    current_line = 0
    eye_in_AOI = False

    for line in raw_lines[1:]:
        current_line += 1
        if last_trial != line.split('\t')[13]:
            eye_in_AOI = False
            last_trial = line.split('\t')[13]
            continue
        if eye_in_AOI:
            last_trial = line.split('\t')[13]
            continue

        # stimulus
        current_stimulus = int(line.split('\t')[21])
        stimulus_on_screen = line.split('\t')[22]

        # calculate eye_pos
        left_gaze_XY = (float(line.split('\t')[27].replace(',', '.')), float(line.split('\t')[28].replace(',', '.')))
        left_gaze_valid = int(line.split('\t')[31])
        right_gaze_XY = (float(line.split('\t')[29].replace(',', '.')), float(line.split('\t')[30].replace(',', '.')))
        right_gaze_valid = int(line.split('\t')[32])
        x_coord = 0.0
        y_coord = 0.0
        if left_gaze_valid == 1 and right_gaze_valid == 1:
            x_coord = (left_gaze_XY[0] + right_gaze_XY[0]) / 2
            y_coord = (left_gaze_XY[1] + right_gaze_XY[1]) / 2
        elif left_gaze_valid:
            x_coord = left_gaze_XY[0]
            y_coord = left_gaze_XY[1]
        elif right_gaze_valid:
            x_coord = right_gaze_XY[0]
            y_coord = right_gaze_XY[1]

        # eye inside AOI
        dict_pos = {1: (float(-7.5), float(-7.5)),
                    2: (float(7.5), float(-7.5)),
                    3: (float(-7.5), float(7.5)),
                    4: (float(7.5), float(7.5))}

        if stimulus_on_screen == 'True' and abs(x_coord - dict_pos[current_stimulus][0]) <= 2.0 and abs(y_coord - dict_pos[current_stimulus][1]) <= 2.0:
            eye_in_AOI = True

        if last_trial != line.split('\t')[13] or line == raw_lines[len(raw_lines) - 1] or eye_in_AOI:
            new_file_data.write((raw_lines[current_line - 1])[:len(raw_lines[current_line - 1]) - 1])
            new_file_data.write('\t')
            if line == raw_lines[len(raw_lines) - 1]:
                new_file_data.write(str(counter + 1))
            else:
                new_file_data.write(str(counter))
            new_file_data.write('\n')
            last_trial = line.split('\t')[13]
            counter = 0
        if line.split('\t')[14] != "-1":
            counter += 1

    with codecs.open(new_file_name, 'w', encoding='utf-8') as new_output_file:
        new_output_file.write(new_file_data.getvalue())
    new_file_data.close()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("You need to specify the path of an output txt file.")

    if not os.path.isfile(sys.argv[1]):
        print("The passed parameter should be a valid file's path: " + sys.argv[1])

    convert(sys.argv[1], sys.argv[2])
