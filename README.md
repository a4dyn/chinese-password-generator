# Password Generator

**README.md [中文版](README_CN.md)**

## Before Use

Install [python-pinyin](https://github.com/mozillazg/python-pinyin#id2) for your python.

Fail to do so will cause the program unable to run.

Quick install: ```pip install pypinyin```


## Usage
```
generate.py [-c]/[-complex] N [-f]/[-file] File
```
[-c] defines the complexity level, and there are level 1/2/3 to be choose.

**Level 1:** Basic password generation, no custom information will be considered (1388 results).

**Level 2:** Including all the passwords from level 1, generate more passwords according to the custom file given. 
Also combine custom information with typical numbers, symbols and top 100 password dictionary.
         
**Level 3:** Including all the passwords from level 2, adds more passwords from top 100, top 500 and typical numbers.

If no [-c] or [-f] is specified, password file with level 1 complexity will be generated.
If no [-c] is specified, but [-f] is specified, password file with level 2 complexity will be generated.

Generated password will be written to Result.txt.

## Usage Example
```
python3 generate.py
python3 -c 3 generate.py
python3 -c 2 -f Custom.txt generate.py
```

## Rules of Custom File
Chinese character is supported! You are welcome to include Chinese character in the custom file.

The input custom file should include only the information needed, and each information should be separated by a new line

```
Correcct example: Tom
                  1234567
Wrong example: name：Tom
               phone：1234567
```
#### Legal Disclaimer
**1.** Usage of this program for attacking targets without prior mutual consent is illegal.
**2.** It is the end user's responsibility to obey all applicable local, state and federal laws.
**3.** Developers assume no liability and are not responsible for any misuse or damage caused by this program.
