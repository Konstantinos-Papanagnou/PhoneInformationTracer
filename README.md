# PhoneInformationTracer

# Installation Tips

### Linux
This script is written in python3 so python3 is required.

Clone the git repository to your local machine.

```bash
git clone https://github.com/Konstantinos-Papanagnou/PhoneInformationTracer.git
```
Install the phonenumbers library from pip
```bash
pip install phonenumbers
```
or use pip3 in case you have both python2 and python3 install on your system
```bash
pip3 install phonenumbers
```
Everything is set! Now you can fire up the script.
### Windows
In order to run this script on windows, download the repository to your computer and make sure you have python3 installed or anaconda.

Install phonenumbers library
```batch
pip install phonenumbers
```
Install argparse library
```batch
pip install argparse
```

Everything is set! Now you can fire up the script.

# Usage

```bash
============================================================
Welcome to Phone Information Tracer made by Konstantinos Pap
============================================================
usage: Phone Information Tracer [-h] [-cc COUNTRY_CODE] [-v] phoneNumber

positional arguments:
  phoneNumber           The Phone Number to Examine

optional arguments:
  -h, --help            show this help message and exit
  -cc COUNTRY_CODE, --country-code COUNTRY_CODE
                        The Country Code, Default=+30 (GR)
  -v, --verbose         increase output verbosity
```

Usage Example:
```bash
python3 PhoneInformationTracker.py 6985456254
```

If you want to change the country code you can simply add the -cc flag and set the flag.
```bash
python3 PhoneInformationTracker.py 6985456254 -cc +30
```
Country code by default is +30.
