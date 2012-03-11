#!/usr/bin/python
import json
import os

class Plugin():
    @staticmethod
    def data():
        load_1, load_5, load_15 = os.getloadavg()

        dict_data = {
            'load_1': float(load_1),
            'load_5': float(load_5),
            'load_15': float(load_15)
        }

        return dict_data

def main():
    print json.dumps(Plugin.data())

if __name__ == '__main__':
    main()
