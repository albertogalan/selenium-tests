#!/bin/bash 


FILE=output
HEADLESS=true
HEADLESS=false
SEARCH="site:www.tecnalia.com"
SEARCHKEYS="laboratory:iec:doit"
KEYWORDS="alber;berto:test;laboratory:doit now"
IDENTIFIER="www.tecnalia.com"
TEST="true"
./generaltests.py --file $FILE --headless $HEADLESS --search "$SEARCH" --searchkeys "$SEARCHKEYS" --keyword "$KEYWORDS" --identifier $IDENTIFIER --test $TEST


