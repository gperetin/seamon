#!/usr/bin/python
import re
import json

class Plugin():
    @staticmethod
    def data():
        fs = file("/proc/loadavg")
        data = fs.read()
        data = data.replace('\n', ' ')

        reg_data = re.match(r"(?P<load_1>[\d.]*)\s(?P<load_5>[\d.]*)\s(?P<load_15>[\d.]*)\s+(.*)", data)
        dict_data = reg_data.groupdict()

        for key in dict_data:
            dict_data[key] = float(dict_data[key])

        return dict_data

def main():
    print json.dumps(Plugin.data())

if __name__ == '__main__':
    main()
