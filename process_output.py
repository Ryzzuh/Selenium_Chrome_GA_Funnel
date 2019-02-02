#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pandas import datetime
import os
print(os.getcwd())
import io
from csv import DictWriter
files = os.listdir('./output')
index = [x for x in range(len(files))]
print(index)
rows = []

def main():
  line_addition = 1
  for i, file in enumerate(files):
    f = io.open(f'./output/{file}', 'r' , encoding='windows-1252')
    try:
      lines = f.readlines()
      date = ([s for s, i in enumerate(lines) if "% of goal completions" in i])[0]
      view_cart = ([s for s, i in enumerate(lines) if "ViewCart" in i])[0]
      shipping_options = ([s for s, i in enumerate(lines) if "ShippingOptions" in i])[1]
      payment = ([s for s, i in enumerate(lines) if "Payment" in i])[1]
      order_confirmation = ([s for s, i in enumerate(lines) if "Order Confirmation" in i])[6]
      '''
      row = { 'Date' : datetime.strptime(lines[date+1].rstrip().split("-")[0], '%d %b %Y').strftime('%Y/%m/%d'),
              'ViewCart': lines[view_cart+2].rstrip("%)\n").split("(")[1],
              'ShippingOptions': lines[shipping_options+2].rstrip("%)\n").split("(")[1],
              'Payment': lines[payment+2].rstrip("%)\n").split("(")[1],
              'OrderConfirmation': lines[order_confirmation+2].rstrip("%)% funnel conversion rate\n")
             }
      '''
      row = { 'Date' : datetime.strptime(lines[date+1].rstrip().split("-")[0], '%d %b %Y').strftime('%Y/%m/%d'),
              'ViewCart': lines[view_cart+1].rstrip("%)\n"),
              'ShippingOptions': lines[shipping_options+1].rstrip("%)\n"),
              'Payment': lines[payment+1].rstrip("%)\n"),
              'OrderConfirmation': lines[order_confirmation+1].rstrip("%)\n")
             }

      rows.append(row)
      print(row)
    except Exception as e:
      print(e)
      pass

  with open('spreadsheet.csv', 'w') as outfile:
    writer = DictWriter(outfile, ('Date', 'ViewCart', 'ShippingOptions', 'Payment', 'OrderConfirmation'))
    writer.writeheader()
    writer.writerows(rows)

if __name__ == "__main__":
  main()