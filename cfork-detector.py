#!/usr/bin/python
#
# Copyright 2017 Deelight
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from classes.exchangedata import ExchangeData
from classes.candleanalyzer import CandleAnalyzer
from classes.candlegraph import CandleGraph

data = ExchangeData.getJson()

timeframe = None
topFractals = None
bullishCFforks = None

analyzedTimeframes = ['3600', str(3600*4), str(3600*24)]

for timeframe in analyzedTimeframes:

    print("### Timeframe:", timeframe, "seconds")

    candleAnalyzerInstance = CandleAnalyzer()

    # Keeping last 200 candles
    candleAnalyzerInstance.loadData(data[timeframe][-200:])

    topFractals = candleAnalyzerInstance.getTopFractals()

    print('Fractals #:', len(topFractals))

    bullishCFforks = candleAnalyzerInstance.getBullishCForks(topFractals)

    print('Cforks #:', len(bullishCFforks))

    # Print status of last CFork
    if len(bullishCFforks) > 0:
        candleAnalyzerInstance.printCForkStatus(bullishCFforks[-1])

    print()

# Draw last graph

graph = CandleGraph()
# Keeping last 200 candles
graph.load(data[timeframe][-200:])
graph.drawTopFractals(topFractals)
graph.drawBullishCForks(bullishCFforks)
graph.show()
