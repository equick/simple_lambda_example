from __future__ import print_function

from datetime import datetime
from urllib2 import urlopen
from re import findall

SITE = 'https://www.national-lottery.co.uk/results/lotto/draw-history/csv'
EXPECTED = 'LIME16286451,NAVY48187931'  # String expected to be on the page


def validate(res):
    matches = findall(EXPECTED, res);

    if len(matches) == 0:
      return False
    else:
      return True


def lambda_handler(event, context):
    print('Checking {} at {}...'.format(SITE, event['time']))
    try:
        if not validate(urlopen(SITE).read()):
            raise Exception('Validation failed')
    except:
        print('Check failed!')
        raise
    else:
        print('Check passed!')
        return event['time']
    finally:
        print('Check complete at {}'.format(str(datetime.now())))
