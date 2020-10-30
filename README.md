# PassiveAggressiveYN
A small python module for passive-aggressive input of a boolean.
## Installation
Clone it and put it where you want.
## Usage
Import it and use the function, but first **PLEASE read the *Variables* section**.
## Content of repository
+ **YN.py**: A test function to showcase behaviour of the function.
+ **PassiveAggressive.py**: The juicy module.
## Variables
+ **Msg**: Message displayed at the first request of the boolean; default is `"y/n "`
+ **K0 to K4**: Must be in descending order for correct functioning, number of attempts allowed before each more passive aggressive comment; defaults are `20, 10, 8, 5, 3`.
+ **GiveUpN**: See *GiveUp*; default is `30`. 
+ **GiveUp**: If `False` the function will never get tired of asking for input, if `True` it will give up after *GiveUpN* attempts and **return a random boolean**; default is `False`.
## [License](https://unlicense.org/)
