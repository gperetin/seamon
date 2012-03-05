#!/usr/bin/python
import re

class Plugin():
    @staticmethod
    def data():
        fs = file("/proc/sys/kernel/hostname")
        data = fs.readline().strip()
	data = data.replace('\n', ' ')
        
	return data

def main():
    print Plugin.data()

if __name__ == '__main__':
    main()
