# Vlocity Versions Clean

This is unofficial module to clean Omniscripts and Integration Procedures versions


## Features

- Select which object clean OmniScript or Integration Procedure (or You can do all 😎)
- Define how many version You want to leave
- Define target Org to use it in deploy process

## Requirement

**Vlocity Versions Clean** using:

- Python 3.10


## Installation



Download repository and install requirements
```sh
git clone https://github.com/kacperosko/velocity-clean-versions.git
cd velocity-clean-versions
pip install -r requirements.txt 
```

Run command

```sh
python vlocity-clean-versions.py --user <<user>> --type <<type>> --count <<count>>
```

## Usage

```sh
python vlocity-clean-versions.py -h
              
>> usage: Vlocity Clean Versions [-h] -u USER -t TYPE -c COUNT
>> 
>> Clean unused versions from Org and keep -n only
>> 
>> options:
>>   -h, --help            show this help message and exit
>>   -u USER, --user USER  Target Org username or sfdx alias
>>   -t TYPE, --type TYPE  which elements will you remove the version, 'os' 'ip' 'all'
>>   -c COUNT, --count COUNT
>>                         how many versions to leave on target Org
```

## License

MIT

**Free Software, Hell Yeah!**

