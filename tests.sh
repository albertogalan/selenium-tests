#!/bin/bash 


FILE=output
HEADLESS=true
HEADLESS=false
SEARCH="site:www.tecnalia.com"
SEARCHKEYS="laboratory:iec:voltage"
KEYWORDS="laboratory;iec:iec:61439"
IDENTIFIER="www.tecnalia.com"
TEST="false"
./generaltests.py --file $FILE --headless $HEADLESS --search "$SEARCH" --searchkeys "$SEARCHKEYS" --keyword "$KEYWORDS" --identifier $IDENTIFIER --test $TEST


