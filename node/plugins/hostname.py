#!/usr/bin/python
import json

class Plugin():
    @staticmethod
    def data():
        fs = file("/proc/sys/kernel/hostname")
        data = fs.readline().strip()
        fs.close()
        
        return data

def main():
    print json.dumps(Plugin.data())

if __name__ == '__main__':
    main()
