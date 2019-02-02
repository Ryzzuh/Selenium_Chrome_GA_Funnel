#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup


def main():
  """ Main program """
  # Code goes over here.
  with open('/html_data', 'r') as my_html_file:
    html_doc = my_html_file.read().replace('\n', '')
  soup = BeautifulSoup(html_doc, 'html.parser')
  print(soup.prettify())




if __name__ == "__main__":
  main()