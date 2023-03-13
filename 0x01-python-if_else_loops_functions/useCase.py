#!/usr/bin/python3
import sys

for name in sys.builtin_module_names:
    print(f"{name}")

print("###############################")

for path in sys.path:
    print(f"{path}")