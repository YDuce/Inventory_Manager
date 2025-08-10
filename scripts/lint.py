#!/usr/bin/env python3
"""Format and lint code"""
import subprocess


def main():
    print("Formatting code...")
    subprocess.run(["black", "inventory_manager_app/", "scripts/"])

    print("Linting...")
    subprocess.run(["flake8", "inventory_manager_app/"])

    print("Complete")


if __name__ == "__main__":
    main()
