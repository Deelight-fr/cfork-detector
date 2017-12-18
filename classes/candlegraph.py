#!/usr/bin/python
#
# Copyright 2017 Deelight
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

import matplotlib.pyplot as plt
from matplotlib.finance import candlestick_ohlc

class CandleGraph:

    def load(self, data):

        ax1 = plt.subplot2grid((1, 1), (0, 0))
        ohlc = []
        for candle in data:
            append_me = candle[0], candle[1], candle[2], candle[3], candle[4], candle[5]
            ohlc.append(append_me)

        # TODO: adapt width
        candlestick_ohlc(ax1, ohlc, width=1, colorup='#77d879', colordown='#db3f3f')

    def drawFractals(self, fractals):
        for idx, value in enumerate(fractals):
            plt.plot([fractals[idx][0]], [fractals[idx][1]], 'g1')

    def drawCForks(self, cforks):

        cforksDrawn = 0
        cforkColors = ['red', 'orange']

        for cfork in cforks:

            # extend first line
            # TODO: find a better way (currently a fixed *2 expansion)
            firstLineSecondPointX = cfork.x1 + 2 * (cfork.x2 - cfork.x1)
            firstLineSecondPointY = cfork.y1 + 2 * (cfork.y2 - cfork.y1)

            plt.plot([cfork.x1, firstLineSecondPointX], [cfork.y1, firstLineSecondPointY], linewidth=1, color=cforkColors[cforksDrawn % 2])

            # extend second line
            # TODO: find a better way (currently a fixed *2 expansion)
            secondLineSecondPointX = cfork.x2 + 3 * (cfork.x3 - cfork.x2)
            secondeLineSecondPointY = cfork.y2 + 3 * (cfork.y3 - cfork.y2)

            # cforksDrawn used to alternate between two colors to avoid confusion
            plt.plot([cfork.x2, secondLineSecondPointX], [cfork.y2, secondeLineSecondPointY], linewidth=1, color=cforkColors[cforksDrawn % 2])

            cforksDrawn += 1

    def show(self):
        plt.show()