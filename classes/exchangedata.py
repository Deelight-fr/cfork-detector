#!/usr/bin/python
#
# Copyright 2017 Deelight
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

import json

class ExchangeData:

    @staticmethod
    def getJson():

        # dataFile = 'gdax-btcusd.json'
        dataFile = 'data-samples/kraken-etceur.json'
        data = json.load(open(dataFile))
        print("Request cost :", data['allowance']['cost'], "- Remaining:", data['allowance']['remaining'])

        return data['result']