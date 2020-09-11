import argparse
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print("============================================================")
print("Welcome to Phone Information Tracer made by Konstantinos Pap")
print("============================================================")

parser = argparse.ArgumentParser(prog='Phone Information Tracer')
parser.add_argument('phoneNumber', action='store', type=str, help='The Phone Number to Examine')

parser.add_argument('-cc', '--country-code', help='The Country Code, Default=+30 (GR)')

parser.add_argument('-v', '--verbose', action='store_true', help='increase output verbosity')

args = parser.parse_args()


countryCode = '+30'

verbosity = args.verbose
phoneNumber = args.phoneNumber
if args.country_code is not None:
	countryCode = args.country_code
	
if verbosity:
	print(f'{bcolors.BOLD}Examining: ', phoneNumber, f'{bcolors.ENDC}')
	print(f'{bcolors.BOLD}Country Code set: ', countryCode, f'{bcolors.ENDC}')
	print('\n\n')

try:
	print(f'{bcolors.BOLD}Validating...{bcolors.ENDC}\n')
	meta = phonenumbers.parse(countryCode + phoneNumber, None)
	if not phonenumbers.is_valid_number(meta):
		print(f'{bcolors.FAIL} Phone Number could not be Validated. Exiting... {bcolors.ENDC}')
		exit()
	print(f'{bcolors.BOLD}', meta, f'{bcolors.ENDC}\n\n')
except phonenumbers.NumberParseException:
	print(f'{bcolors.FAIL} Phone Number could not be Validated. Exiting... {bcolors.ENDC}')
	exit()

if verbosity:
	print(f'{bcolors.BOLD} Retrieving Country {bcolors.ENDC}')

print(f'{bcolors.BOLD} Area: ', geocoder.description_for_number(meta, 'en'), f'{bcolors.ENDC}\n')

if verbosity:
	print(f'{bcolors.BOLD} Attempting to get Carrier Informaion {bcolors.ENDC}')
carrier_info = carrier.name_for_number(meta, 'en')
if carrier_info is not None and not carrier_info == "":
	if verbosity:
		print(f'{bcolors.BOLD} Success {bcolors.ENDC}')
	print(f'{bcolors.BOLD}Carrier: ', carrier_info, f'{bcolors.ENDC}\n')
else: 
	print(f'{bcolors.FAIL}Carrier could not be Traced!{bcolors.ENDC}\n')
	
if verbosity:
	print(f'{bcolors.BOLD} Attempting to get TimeZone Information {bcolors.ENDC}')
	
timezone_info = timezone.time_zones_for_number(meta)
if timezone_info is not None and not timezone_info == "":
	if verbosity:
		print(f'{bcolors.BOLD} Success {bcolors.ENDC}')
	print(f'{bcolors.BOLD}Timezone: ', timezone_info, f'{bcolors.ENDC}\n')
else: 
	print(f'{bcolors.FAIL}Timezone could not be Traced!{bcolors.ENDC}\n')
if verbosity:
	print(f'{bcolors.BOLD}Information Trace Completed Successfully!{bcolors.ENDC}')