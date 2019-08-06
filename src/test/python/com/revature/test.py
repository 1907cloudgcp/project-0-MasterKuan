#!/usr/bin/env python3
import os


def main():
	os.system("python server/server.py &")
	os.system("python server/client.py")


if __name__ == '__main__':
	main()
