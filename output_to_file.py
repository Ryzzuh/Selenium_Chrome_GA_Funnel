#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

def main(filename="filename", data="data"):
  with open(f"./output/{filename}.txt", "w") as text_file:
    print(f"{data}", file=text_file)

if __name__ == "__main__":
  main()