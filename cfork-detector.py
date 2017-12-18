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
fractals = None
cforks = None

analyzedTimeframes = ['3600', str(3600*4), str(3600*24)]

for timeframe in analyzedTimeframes:

    print("### Timeframe:", timeframe, "seconds")

    candleAnalyzerInstance = CandleAnalyzer()

    # Keeping last 200 candles
    candleAnalyzerInstance.loadData(data[timeframe][-200:])

    fractals = candleAnalyzerInstance.getFractals()

    print('Fractals #:', len(fractals))

    cforks = candleAnalyzerInstance.getBullishCForks(fractals)

    print('Cforks #:', len(cforks))

    # Print status of last CFork
    if len(cforks) > 0:
        candleAnalyzerInstance.printCForkStatus(cforks[-1])

    print()

# Draw last graph

graph = CandleGraph()
# Keeping last 200 candles
graph.load(data[timeframe][-200:])
graph.drawFractals(fractals)
graph.drawCForks(cforks)
graph.show()
