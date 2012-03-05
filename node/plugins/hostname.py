#!/usr/bin/python
import json

class Plugin():
    @staticmethod
    def data():
        fs = file("/proc/sys/kernel/hostname")
        data = fs.readline().strip()
	data = data.replace('\n', ' ')
        
	return data

def main():
    print json.dumps(Plugin.data())

if __name__ == '__main__':
    main()
