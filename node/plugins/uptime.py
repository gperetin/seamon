#!/usr/bin/python
import json

class Plugin():
    @staticmethod
    def data():
        fs = file("/proc/uptime")
        data = fs.readline().strip()
        data = float(min(data.split(' ')))
        fs.close()
        
        return data

def main():
    print json.dumps(Plugin.data())

if __name__ == '__main__':
    main()
