# Vlocity Versions Clean

This is unofficial module to clean Omniscripts and Integration Procedures versions from provided Salesforce Org


## Features

- Select which objects You want to clean, OmniScripts or Integration Procedures (or You can do all 😎)
- Define how many version You want to leave
- Define target Org

## Requirement

**Vlocity Versions Clean** is using:

- Python 3.10


## Installation

Download repository and install requirements
```commandline
git clone https://github.com/kacperosko/vlocity-clean-versions.git
cd vlocity-clean-versions
pip install -r requirements.txt 
```

Run command inside **vlocity-clean-versions** folder

```commandline
python vlocity-clean-versions --username USERNAME --password PASSWORD --token TOKEN --domain DOMAIN --object OBJECT --count COUNT
```

## Usage

```commandline
python vlocity-clean-versions -h
              
>> usage: Vlocity Clean Versions [-h] -u USER -t TYPE -c COUNT
>> 
>> Clean unused versions from Org and keep -n only
>> 
>> options:
    -h, --help            show this help message and exit
    
    -u USERNAME, --username USERNAME
                        Username the user you want to log in to the selected Org
                        
    -p PASSWORD, --password PASSWORD
                        Password the user you want to log in to the selected Org
                        
    -t TOKEN, --token TOKEN
                        Security Token of the user you want to log in with
                        
    -d DOMAIN, --domain DOMAIN
                        Domain of selected Org. Provide 'test' if You try to log in to sandbox
    
    -o {os,ip,all}, --object {os,ip,all}
                        Which objects to delete ('os' 'ip' 'all')
    
    -c COUNT, --count COUNT
                        Number greater than or equal to 0 of versions to leave on target Org excluding Activated Version

```

## Example
```commandline
python vlocity-clean-versions -u username@salesforce.com -p TestQA123 -t AbCDFghiJ -d test -o all -c 4
```

```commandline
python vlocity-clean-versions --username test.qa@salesforce.com --password TestQA123 --token AbCDFghiJ --object ip --count 1
```


## License

MIT

**Free Software, Hell Yeah!**

