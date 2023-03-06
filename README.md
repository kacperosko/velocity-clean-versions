# Vlocity Versions Clean

This is unofficial module to clean Omniscripts and Integration Procedures versions


## Features

- Select which object clean OmniScript or Integration Procedure (or You can do all 😎)
- Define how many version You want to leave
- Define target Org to use it in deploy process

## Requirement

**Vlocity Versions Clean** is using:

- Python 3.10
- [Salesforce CLI >= 7.188.1](https://developer.salesforce.com/tools/sfdxcli)
- Authorized Org


## Installation



Download repository and install requirements
```commandline
git clone https://github.com/kacperosko/vlocity-clean-versions.git
cd vlocity-clean-versions
pip install -r requirements.txt 
```

Run command inside **vlocity-clean-versions** folder

```commandline
python vlocity-clean-versions --user <user> --type <type> --count <count>
```

## Usage

```commandline
python vlocity-clean-versions -h
              
>> usage: Vlocity Clean Versions [-h] -u USER -t TYPE -c COUNT
>> 
>> Clean unused versions from Org and keep -n only
>> 
>> options:
  -h, --help                            show this help message and exit
  -u USER, --user USER                  Target Org username or sfdx alias authorized on computer
  -t {os,ip,all}, --type {os,ip,all}    Which element's versions to delete ('os' 'ip' 'all')
  -c COUNT, --count COUNT               Number greater greater than or equal to 0 of versions to leave on target Org excluding Activated Version
```

## Exampple
```sh
python vlocity-clean-versions -u username@salesforce.com -t all -c 4
```

```sh
python vlocity-clean-versions --user test.qa@salesforce.com --type ip --count 1
```


## License

MIT

**Free Software, Hell Yeah!**

