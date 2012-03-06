#!/usr/bin/python
import json

class Plugin():
    @staticmethod
    def data():
        fs = file("/proc/loadavg")
        data = fs.readline().strip()
        load_1, load_5, load_15, a, b = data.split()
        fs.close()

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
