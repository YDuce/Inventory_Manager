#!/usr/bin/env python3
"""Development server with auto-reload"""
import os
import subprocess
import sys


def main():
    os.environ["FLASK_ENV"] = "development"
    os.environ["FLASK_DEBUG"] = "1"

    try:
        subprocess.run([sys.executable, "run.py"], check=True)
    except KeyboardInterrupt:
        print("Development server stopped")


if __name__ == "__main__":
    main()
