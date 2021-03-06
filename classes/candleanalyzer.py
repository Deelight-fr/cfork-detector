#!/usr/bin/python
#
# Copyright 2017 Deelight
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from classes.cfork import CFork

class CandleAnalyzer:

    data = None

    def loadData(self, data):
        self.data = data

    def getTopFractals(self):
        # Custom method 1 (check N candles before, N after)
        # N = scanPeriod

        scanPeriod = 2

        fractals = []

        for idx, candle in enumerate(self.data):
            # data elements : ts, open, high, low, close, ...

            # previous N
            if idx > scanPeriod - 1:
                previous = self.data[idx - scanPeriod:idx]
                highs = [x[2] for x in previous]
                previousPeriodHigh = max(highs)

            # next N
            if idx < len(self.data) - (scanPeriod - 1):
                following = self.data[idx + 1:idx + scanPeriod]
                highs = [x[2] for x in following]
                followingPeriodHigh = max(highs)

            if (scanPeriod - 1 < idx < len(self.data) - (scanPeriod - 1) and
                    candle[2] > previousPeriodHigh and
                    candle[2] > followingPeriodHigh):
                fractals.append([candle[0], candle[2]])

        return fractals

    def getBottomFractals(self):
        # Custom method 1 (check N candles before, N after)
        # N = scanPeriod

        scanPeriod = 2

        fractals = []

        for idx, candle in enumerate(self.data):
            # data elements : ts, open, high, low, close, ...

            # previous N
            if idx > scanPeriod - 1:
                previous = self.data[idx - scanPeriod:idx]
                lows = [x[3] for x in previous]
                previousPeriodLow = min(lows)

            # next N
            if idx < len(self.data) - (scanPeriod - 1):
                following = self.data[idx + 1:idx + scanPeriod]
                lows = [x[3] for x in following]
                followingPeriodLow = min(lows)

            if (scanPeriod - 1 < idx < len(self.data) - (scanPeriod - 1) and
                    candle[3] < previousPeriodLow and
                    candle[3] < followingPeriodLow):
                fractals.append([candle[0], candle[3]])

        return fractals

    def getBullishCForks(self, topFractals):
        computedCForks = []

        for idx, value in enumerate(topFractals):

            if idx < len(topFractals) - 2:
                # The two last fractals can't build a full cfork (3 needed)

                # First fractal
                x1 = topFractals[idx][0]
                y1 = topFractals[idx][1]

                # Second fractal
                x2 = topFractals[idx + 1][0]
                y2 = topFractals[idx + 1][1]

                # Slope
                slope1to2 = (y2 - y1) / (x2 - x1)

                if slope1to2 < 0:

                    # Now can we find the next line with a smaller slope?
                    idxOffset = 2
                    forkLineFound = False
                    failedFork = False
                    while idx + idxOffset < len(topFractals) and not forkLineFound and not failedFork:

                        x3 = topFractals[idx + idxOffset][0]
                        y3 = topFractals[idx + idxOffset][1]

                        # Compute second slope
                        slope2to3 = (y3 - y2) / (x3 - x2)

                        # Second slope has to be negative but greater than first slope
                        # Here we use a 1.5 factor to ignore almost flat forks
                        # TODO : adapt this factor
                        if slope2to3 < 0:
                            if abs(slope2to3) * 1.5 < abs(slope1to2):

                                newCfork = CFork([x1, y1], [x2, y2], [x3, y3])
                                computedCForks.append(newCfork)

                                forkLineFound = True
                        else:
                            # Failed fork - no solution
                            failedFork = True

                        idxOffset += 1

        return computedCForks

    def getBearishCForks(self, bottomFractals):
        computedCForks = []

        for idx, value in enumerate(bottomFractals):

            if idx < len(bottomFractals) - 2:
                # The two last fractals can't build a full cfork (3 needed)

                # First fractal
                x1 = bottomFractals[idx][0]
                y1 = bottomFractals[idx][1]

                # Second fractal
                x2 = bottomFractals[idx + 1][0]
                y2 = bottomFractals[idx + 1][1]

                # Slope
                slope1to2 = (y2 - y1) / (x2 - x1)

                if slope1to2 > 0:

                    # Now can we find the next line with a smaller slope?
                    idxOffset = 2
                    forkLineFound = False
                    failedFork = False
                    while idx + idxOffset < len(bottomFractals) and not forkLineFound and not failedFork:

                        x3 = bottomFractals[idx + idxOffset][0]
                        y3 = bottomFractals[idx + idxOffset][1]

                        # Compute second slope
                        slope2to3 = (y3 - y2) / (x3 - x2)

                        # Second slope has to be positive but greater than first slope
                        # Here we use a 1.5 factor to ignore almost flat forks
                        # TODO : adapt this factor
                        if slope2to3 > 0:
                            if abs(slope2to3) * 1.5 < abs(slope1to2):

                                newCfork = CFork([x1, y1], [x2, y2], [x3, y3])
                                computedCForks.append(newCfork)

                                forkLineFound = True
                        else:
                            # Failed fork - no solution
                            failedFork = True

                        idxOffset += 1

        return computedCForks


    def printBullishCForkStatus(self, cfork):

        slope = (cfork.y3 - cfork.y2) / (cfork.x3 - cfork.x2)
        print('CFork slope:', slope)

        cforkTargetY = slope * (self.data[-1][0] - cfork.x2) + cfork.y2
        print('CFork target:', cforkTargetY)
        print('Current price:', self.data[-1][2])

        if self.data[-1][2] > cforkTargetY:
            print('Last candle high over last bullish fork')
        else:
            print('Last candle high under last bullish fork')
        if self.data[-1][2] > cforkTargetY > self.data[-1][3]:
            print('Last candle crossed last bullish fork')

    def printBearishCForkStatus(self, cfork):

        slope = (cfork.y3 - cfork.y2) / (cfork.x3 - cfork.x2)
        print('CFork slope:', slope)

        cforkTargetY = slope * (self.data[-1][0] - cfork.x2) + cfork.y2
        print('CFork target:', cforkTargetY)
        print('Current price:', self.data[-1][2])

        if self.data[-1][2] > cforkTargetY:
            print('Last candle high over last bearish fork')
        else:
            print('Last candle high under last bearish fork')
        if self.data[-1][2] > cforkTargetY > self.data[-1][3]:
            print('Last candle crossed last bearish fork')