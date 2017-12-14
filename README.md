# Bricklayer [![Build Status](https://travis-ci.org/cbrentharris/bricklayer.svg?branch=master)](https://travis-ci.org/cbrentharris/bricklayer) [![codecov.io](https://codecov.io/github/cbrentharris/bricklayer/coverage.svg?branch=master)](https://codecov.io/github/cbrentharris/bricklayer?branch=master)

An interactive python package leveraging [Lego Digital Designer](http://ldd.lego.com/en-us/) to help teach computer science.

### Examples:

```
from bricklayer.levels.level_1 import put_2D_2x1_RED, output

put_2D_2x1_RED(0,0)
output()
```


## Command Line

Bricklayer also comes with a commane line interface, allowing users to "diagnose" issues with their programs, collect data from the programs and send it to a Bricklayer backend, and download Lego Digital Designer

### Download

```
$ bricklayer --download
 99% |########################################################################################
 ```
 Will output a file called `ldd.zip` or `ldd.exe` in the directory you were in (zip for mac, exe for windows).
 
### Installation

```sh
python setup.py install
```
