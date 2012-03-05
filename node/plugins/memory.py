#!/usr/bin/python
import re
import json

class Plugin():
    @staticmethod
    def data():
        fs = file("/proc/meminfo")
        data = fs.read().strip()
        data = data.replace('\n', ' ')

        reg_data = re.match(r"(.*)MemTotal:\s+(?P<memory_total>\d+)\s+kB", data)
        dict_data = reg_data.groupdict()
        reg_data = re.match(r"(.*)MemFree:\s+(?P<memory_free>\d+)\s+kB", data)
        dict_data.update(reg_data.groupdict())

        for key in dict_data:
            dict_data[key] = int(dict_data[key])

        dict_data.update({'memory_used': (dict_data['memory_total'] - dict_data['memory_free'])})

        return dict_data

def main():
    print json.dumps(Plugin.data())

if __name__ == '__main__':
    main()
