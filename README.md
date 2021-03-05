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

If you want to add it to your path simply run `chmod +x setup.sh` and `sudo ./setup.sh`.

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
usage: PhoneInformationTracer.py [-h] [-i INPUT] [-cc COUNTRY_CODE] [-v] [-l LIST] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        The Phone Number imput to Examine
  -cc COUNTRY_CODE, --country-code COUNTRY_CODE
                        The Country Code, Default=+30 (GR)
  -v, --verbose         increase output verbosity
  -l LIST, --list LIST  Specify a phone list to enumerate
  -o OUTPUT, --output OUTPUT
                        Specify a file to export the data

```

Usage Example:
```bash
python3 PhoneInformationTracer.py -i 6985456254
```

If you want to change the country code you can simply add the -cc flag and set the flag.
```bash
python3 PhoneInformationTracer.py -i 6985456254 -cc +30
```
Or you can pass a file to the program with phone numbers on each line and specify a output file
```bash
python3 PhoneInformationTracer.py -l input -o output
```
Country code by default is +30.
