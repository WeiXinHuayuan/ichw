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


# Part A: Breaking Up Strings

def before_space(s):
    """Return substring of s;up to, but not including, the first space"""
    list = s.split(' ', 1)
    strbefore = list[0]
    return strbefore


def after_space(s):
    """Return substring of s after the first space"""
    list = s.split(' ', 1)
    strafter = list[1]
    return strafter


def testA():
    """text functinons in Part A"""
    assert('2.24075' == before_space('2.24075 Euros'))
    assert('Euros' == after_space('2.24075 Euros'))


# Part B: Processing a JSON String

def first_inside_quotes(s):
    """Return the first substring of s between two (double) quote characters"""
    s = s[s.index('"')+1:]
    strfirst = s[:s.index('"')]
    return strfirst


def get_from(json):
    """Return the FROM value in the response to a currency query"""
    json = json[json.index(':')+1:]
    json_get_from = first_inside_quotes(json)
    return json_get_from


def get_to(json):
    """Return the TO value in the response to a currency query"""
    json = json[json.index(',')+1:]
    json = json[json.index(':')+1:]
    json_get_to = first_inside_quotes(json)
    return json_get_to


def has_error(json):
    """Return False if the query has an error; True otherwise"""
    if 'true' in json:
        return True
    if 'false' in json:
        return False


def textB():
    """text functions in Part B"""
    json = '{ "from" : "2.5 United States Dollars", "to" : "2.1589225 Euros", "success" : true, "error" : "" }'
    assert('2.5 United States Dollars' == get_from(json))
    assert('2.1589225 Euros' == get_to(json))
    assert(has_error(json) is True)


# Part C: Currency Query

def currency_response(currency_from, currency_to, amount_from):
    """Return a JSON string that is a response to a currency query"""
    from urllib.request import urlopen
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from={0}&to={1}&amt={2}'.format(currency_from, currency_to, amount_from))
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return jstr


def textC():
    """text functions in Part C"""
    json = '{ "from" : "2.5 United States Dollars", "to" : "2.1589225 Euros", "success" : true, "error" : "" }'
    assert(json == currency_response('USD', 'EUR', 2.5))


# Part D: Currency Exchange

def iscurrency(currency):
    """Return True if currency is a valid currency"""
    json = currency_response(currency, currency, 1)
    return has_error(json)


def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange."""
    def check_input():
        """check the user's input"""
        if iscurrency(currency_from):
            pass
        else:
            print('the first currency code is invalid')
        if iscurrency(currency_to):
            pass
        else:
            print('the second currency code is invalid')
        t = type(amount_from)
        if t == float or t == int:
            pass
        else:
            print('the amount is invalid')
        if iscurrency(currency_from) and iscurrency(currency_to) and (t == float or t == int):
            return True

    if check_input():
        json = currency_response(currency_from, currency_to, amount_from)
        s = get_to(json)
        amount = float(before_space(s))
        return amount


def textD():
    """text functions in Part D"""
    assert(iscurrency('USD') is True)
    assert(exchange('USD', 'EUR', 2.5) == 2.1589225)


def textAll():
    """test all cases"""
    testA()
    textB()
    textC()
    textD()
    print('All tests passed')

if __name__ == '__main__':
    textAll()
