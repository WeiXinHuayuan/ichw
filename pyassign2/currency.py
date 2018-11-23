#!/user/bin/env python3

"""currecy.py:Module for currency exchange

__author__ = "Weixin"
__pkuid__  = "1800011764"
__email__  = "1800011764@pku.edu.cn"
"""

"""Module for currency exchange
This module provides several string parsing functions to implement a 
simple currency exchange routine using an online currency service. 
The primary function in this module is exchange."""

def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange."""
    from urllib.request import urlopen
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from={0}&to={1}&amt={2}'.format(currency_from, currency_to, amount_from))
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    jstr = jstr.replace('true', 'True')
    jstr = jstr.replace('false', 'False')
    dict = eval(jstr)
    str1 = dict['to']
    list1 = str1.split()
    result = float(list1[0])
    return result


def test_exchange():
	"""test exchange()"""
	assert(2.1589225 == exchange('USD', 'EUR', 2.5))


def textAll():
	"""test all cases"""
	test_exchange()
	print('All tests passed')

a = input('currency_from: ')
b = input('currecy_to: ')
c = input('amount_from: ')
amount = exchange(a, b, c)
print(amount)


if __name__ == '__main__':
	textAll()


