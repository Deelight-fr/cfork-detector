#!/usr/bin/python
#
# Copyright 2017 Deelight
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

import matplotlib.pyplot as plt
from matplotlib.finance import candlestick_ohlc

# <TEST>
# import json
# import pandas as pd
# from bokeh.plotting import figure, show, output_file
# from math import piimport pandas as pd
# from bokeh.plotting import figure, show, output_file
# from math import pi
# </TEST>

class CandleGraph:

    p = None

    def load(self, data):

        ax1 = plt.subplot2grid((1, 1), (0, 0))
        ohlc = []
        for candle in data:
            append_me = candle[0], candle[1], candle[2], candle[3], candle[4], candle[5]
            ohlc.append(append_me)

        # TODO: adapt width
        candlestick_ohlc(ax1, ohlc, width=1, colorup='#77d879', colordown='#db3f3f')

        # <TEST>
        # df = pd.read_json(json.dumps(data))
        # df.rename(columns={0: 'date', 1: 'open', 2: 'high', 3: 'low', 4: 'close', 5: 'volume', 6: 'unknown'}, inplace=True)
        # df["date"] = pd.to_datetime(df["date"], unit='s')
        # # print(df.to_csv())
        #
        # inc = df.close > df.open
        # dec = df.open > df.close
        # w = 12 * 60 * 60 * 1000 # half day in ms
        #
        # TOOLS = "pan,wheel_zoom,box_zoom,reset,save"
        #
        # self.p = figure(x_axis_type="datetime", tools=TOOLS, plot_width=1000, title="Candlestick Chart")
        # self.p.xaxis.major_label_orientation = pi / 4
        # self.p.grid.grid_line_alpha = 0.3
        #
        # self.p.segment(df.date, df.high, df.date, df.low, color="black")
        # self.p.vbar(df.date[inc], w, df.open[inc], df.close[inc], fill_color="#D5E1DD", line_color="black")
        # self.p.vbar(df.date[dec], w, df.open[dec], df.close[dec], fill_color="#F2583E", line_color="black")
        # </TEST>

    def drawTopFractals(self, fractals):
        for idx, value in enumerate(fractals):
            plt.plot([fractals[idx][0]], [fractals[idx][1]], 'g1')

    def drawBottomFractals(self, fractals):
        for idx, value in enumerate(fractals):
            plt.plot([fractals[idx][0]], [fractals[idx][1]], 'r1')

    def drawBullishCForks(self, cforks):

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

    def drawBearishCForks(self, cforks):

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

        # <TEST>
        # output_file("output/candlestick.html", title="candlestick chart")
        # show(self.p)
        # </TEST>