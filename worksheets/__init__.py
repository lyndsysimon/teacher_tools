from random import SystemRandom
from datetime import datetime as dt

# English language letter frequence taken from Wikipedia
# http://en.wikipedia.org/wiki/Letter_frequency
#
# Values provided are multiplied by 10k, then provided as a cumulative total.

letter_frequency={
    817: 'a',
    966: 'b',
    1244: 'c',
    1669: 'd',
    2940: 'e',
    3162: 'f',
    3364: 'g',
    3973: 'h',
    4670: 'i',
    4685: 'j',
    4762: 'k',
    5165: 'l',
    5406: 'm',
    6080: 'n',
    6831: 'o',
    7024: 'p',
    7034: 'q',
    7632: 'r',
    8265: 's',
    9170: 't',
    9446: 'u',
    9544: 'v',
    9780: 'w',
    9795: 'x',
    9992: 'y',
    10000: 'z',
}

rng = SystemRandom(dt.now())

def natural_random_letter():
    '''
    Returns a pseudo-random letter, with a frequency that mimics that of the
    English language.
    '''
    return letter_frequency[
        sorted(
            [k for k in letter_frequency.keys() if k >= rng.randint(1,10000)]
        )[0]
    ]