#!/user/bin/env python3

"""wcount.py:count words from an Internet file.

__author__ = "Weixin"
__pkuid__  = "1800011764"
__email__  = "1800011764@pku.edu.cn"
"""

import sys
from urllib.request import urlopen


def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    lines = lines.lower()
    import re
    wordlist = re.findall(r'[a-z]+', lines)
    import collections
    wordct = collections.Counter(wordlist)
    mostwords = wordct.most_common(topn)
    for i in mostwords:
        print('{0}\t{1}'.format(i[0],i[1]))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('url: URL of the txt file to analyze')
        print('topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        url = sys.argv[1]
        text = urlopen(url)
        lines = text.read().decode()
        text.close()
        if len(sys.argv) >= 3:
            topn = int(sys.argv[2])
            wcount(lines, topn)
        else:
            wcount(lines)
    except Exception as error:
        print(error)