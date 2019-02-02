#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from datetime import date, timedelta

def main():
  """ Main program """
  # Code goes over here.

  url_tokens = {
    1: 'https://analytics.google.com/analytics/web/#report/conversions-goal-funnel/a89859w27785432p26521297/%3F_u.date00%3D',
    2: '%26_u.date01%3D',
    3: '%26funnel_goaloption_1-graphOptions.primaryConcept%3Danalytics.goalConversionRate1/'
  }
  # create date range
  d1 = datetime.date(2017, 5, 25)  # start date
  d2 = datetime.date(2018, 5, 25)  # end date
  delta = d2 - d1  # timedelta
  dates= [(d1+timedelta(x)).strftime('%Y%m%d') for x in range(delta.days)]
  print(delta)
  print(dates)



if __name__ == "__main__":
  main()