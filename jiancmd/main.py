#!/usr/bin/env python
""" a command line tool to do simple everyday tasks for developers

Usage:
    jiancmd currency convert FROM TO [-a AMOUNT]
    jiancmd currency list
    jiancmd currency -h | --help

Options:
    -h --help               display help screen
    -a --amount==AMOUNT     specify the amount to be converted [default:1]

"""
import docopt
import requests

api_fixer = "http://api.fixer.io/latest?"

def parse_arguments():
    return docopt.docopt(__doc__)

def formulate_request(url,base,to):
    request = url + 'base='+base+'&symbols='+to
    return request

def main():
    arguments = parse_arguments()
    if arguments['convert']:
        base = arguments['FROM']
        to = arguments['TO']
        amount = arguments['--amount']
        url = formulate_request(api_fixer,base,to)
        response = requests.get(url).json()
        for to, rate in response["rates"].iteritems():
            amount_in_to = float(rate)*float(amount);
            print ('{amount} {base} is converted to: {rate} {to}').format(amount=amount,base=base,
                                                                   rate=amount_in_to,to=to)
    elif arguments['list']:
        response = requests.get(api_fixer).json()
        encoded_res = [x.encode('utf-8') for x in response['rates'].keys()]
        print encoded_res


if __name__ == '__main__':
    main()
