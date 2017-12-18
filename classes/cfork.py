#!/usr/bin/python
#
# Copyright 2017 Deelight
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

class CFork:
    x1 = None
    y1 = None
    x2 = None
    y2 = None
    x3 = None
    y3 = None

    def __init__(self, p1, p2, p3):
        self.x1 = p1[0]
        self.y1 = p1[1]
        self.x2 = p2[0]
        self.y2 = p2[1]
        self.x3 = p3[0]
        self.y3 = p3[1]