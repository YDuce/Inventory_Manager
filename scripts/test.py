#!/usr/bin/env python3
"""Run full test suite with coverage"""
import subprocess
import sys


def main():
    commands = [["pytest", "-v"], ["flake8", "inventory_manager_app/"]]

    for cmd in commands:
        print(f"Running: {' '.join(cmd)}")
        result = subprocess.run(cmd)
        if result.returncode != 0:
            print(f"{cmd[0]} failed")
            sys.exit(1)

    print("All checks passed")


if __name__ == "__main__":
    main()
