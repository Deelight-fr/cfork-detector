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
bottomFractals = None
bullishCFforks = None

analyzedTimeframes = ['3600', str(3600*4), str(3600*24)]

for timeframe in analyzedTimeframes:

    print("### Timeframe:", timeframe, "seconds")

    candleAnalyzerInstance = CandleAnalyzer()

    # Keeping last 200 candles
    candleAnalyzerInstance.loadData(data[timeframe][-200:])

    topFractals = candleAnalyzerInstance.getTopFractals()

    print('Top Fractals #:', len(topFractals))

    bottomFractals = candleAnalyzerInstance.getBottomFractals()

    print('Bottom Fractals #:', len(bottomFractals))

    bullishCFforks = candleAnalyzerInstance.getBullishCForks(topFractals)

    print('Cforks #:', len(bullishCFforks))

    # Print status of last bullish CFork
    if len(bullishCFforks) > 0:
        candleAnalyzerInstance.printBullishCForkStatus(bullishCFforks[-1])

    bearishCFforks = candleAnalyzerInstance.getBearishCForks(bottomFractals)

    print('Cforks #:', len(bearishCFforks))

    # Print status of last bearish CFork
    if len(bearishCFforks) > 0:
        candleAnalyzerInstance.printBearishCForkStatus(bearishCFforks[-1])

    print()

# Draw last graph

graph = CandleGraph()
# Keeping last 200 candles
graph.load(data[timeframe][-200:])
graph.drawTopFractals(topFractals)
graph.drawBottomFractals(bottomFractals)
graph.drawBullishCForks(bullishCFforks)
graph.drawBearishCForks(bearishCFforks)
graph.show()
