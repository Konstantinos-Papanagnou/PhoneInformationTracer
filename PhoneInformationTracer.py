#!/usr/bin/python3

import argparse
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
import sys
from bannermagic import printBannerPadding, printMessage


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class ParserData:

    def __init__(self):
        self.print_banner()
        parser = self.configureParser()
        args = parser.parse_args()
        self.verbosity = args.verbose
        
        if args.input:
            self.list = False
            self.phoneNumber = args.input
        else :
            if not args.list:
                #parser.echo()
                sys.stderr.write('You need to specify at least -i or -l option!\n\nRun PhoneInformationTracer.py -h for more help\n')
                exit()
            self.list = True
            self.phoneNumbers = args.list
        self.outputfile = args.output
        if args.country_code is not None:
            self.countryCode = args.country_code
        else :
            self.countryCode = '+30'
 

    def configureParser(self):
        parser = argparse.ArgumentParser(prog='PhoneInformationTracer.py')
        parser.add_argument('-i', '--input', help='The Phone Number imput to Examine')
        parser.add_argument('-cc', '--country-code', help='The Country Code, Default=+30 (GR)')
        parser.add_argument('-v', '--verbose', action='store_true', help='increase output verbosity')
        parser.add_argument('-l', '--list', help='Specify a phone list to enumerate')
        parser.add_argument('-o', '--output', help='Specify a file to export the data')
        return parser

    def print_banner(self):
        printBannerPadding('*')
        printMessage("Welcome to Phone Information Tracer made by Konstantinos Pap")
        printBannerPadding('*')


def ExamineNumber(phoneNumber, countryCode, verbosity=False):
    if verbosity:
        print(f'{bcolors.BOLD}Examining: ', phoneNumber, f'{bcolors.ENDC}')
        print(f'{bcolors.BOLD}Country Code set: ', countryCode, f'{bcolors.ENDC}')  
        print('\n\n')

    try:
        print(f'{bcolors.BOLD}Validating...{bcolors.ENDC}\n')
        meta = phonenumbers.parse(countryCode + phoneNumber, None)
        if not phonenumbers.is_valid_number(meta):
            print(f'{bcolors.FAIL} Phone Number could not be Validated. Exiting... {bcolors.ENDC}')
            return "Invalid", "Invalid", "Invalid"
        print(f'{bcolors.BOLD}', meta, f'{bcolors.ENDC}\n\n')
    except phonenumbers.NumberParseException:
        print(f'{bcolors.FAIL} Phone Number could not be Validated. Exiting... {bcolors.ENDC}')
        return 'Invalid', 'Invalid', 'Invalid'
    if verbosity:
        print(f'{bcolors.BOLD} Retrieving Country {bcolors.ENDC}')
    area = geocoder.description_for_number(meta, 'en')
    print(f'{bcolors.BOLD} Area: ', area, f'{bcolors.ENDC}\n')

    if verbosity:
        print(f'{bcolors.BOLD} Attempting to get Carrier Informaion {bcolors.ENDC}')
    carrier_info = carrier.name_for_number(meta, 'en')
    if carrier_info is not None and not carrier_info == "":
        if verbosity:
            print(f'{bcolors.BOLD} Success {bcolors.ENDC}')
        print(f'{bcolors.BOLD}Carrier: ', carrier_info, f'{bcolors.ENDC}\n')
    else:
        carrier_info = 'Could Not Be Traced'
        print(f'{bcolors.FAIL}Carrier could not be Traced!{bcolors.ENDC}\n')
	
    if verbosity:
        print(f'{bcolors.BOLD} Attempting to get TimeZone Information {bcolors.ENDC}')
	
    timezone_info = timezone.time_zones_for_number(meta)
    if timezone_info is not None and not timezone_info == "":
        if verbosity:
            print(f'{bcolors.BOLD} Success {bcolors.ENDC}')
        print(f'{bcolors.BOLD}Timezone: ', timezone_info, f'{bcolors.ENDC}\n')
    else:
        timezone_info = "Could Not Be Traced"
        print(f'{bcolors.FAIL}Timezone could not be Traced!{bcolors.ENDC}\n')

    return area, carrier_info, timezone_info


if __name__ == "__main__":
    data = ParserData()
    print (data.list)
    if not data.list:
        a, c, t = ExamineNumber(data.phoneNumber, data.countryCode, data.verbosity)
        if data.outputfile is not None:
           with open(data.outputfile, 'w') as f:
               f.write('Number\t\t: Area\t | Carrier\t | timezone\n')
               f.write(f'{data.phoneNumber}\t: {a}\t | {c}\t | {t}\n')
    else:
        if data.outputfile is None:
            sys.stderr.write('-l flag requires -o flag as well\n')
            exit()
        with open(data.outputfile, 'w') as of:
            of.write('Number\t\t: Area\t | Carrier\t | timezone\n')
            with open(data.phoneNumbers, 'r') as ifl:
                lines = ifl.read()
            lines = lines.split('\n')
            lines = lines[:-1]
            for line in lines:
                if '+' in line:
                    number = line[3:]
                    countryCode = line[:3]
                else:
                    number = line
                    countryCode = data.countryCode
                a, c, t = ExamineNumber(number, countryCode, data.verbosity) 
                if data.outputfile is not None:
                    of.write(f'{number}\t: {a}\t | {c}\t | {t}\n')

    if data.verbosity:
        print(f'{bcolors.BOLD}Information Trace Completed Successfully!{bcolors.ENDC}')















