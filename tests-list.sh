#!/bin/bash


if [[ $# -eq 0 ]]; then
  echo "$red types=auto/manual  $reset"
  echo "Usage: ${FUNCNAME[0]} $green {testlist} $reset"
  exit 0
fi

TESTLIST=testlist.txt
MINCHAR=6

function tests(){

testname="$1"	
headless="$2"
list="$3"
searchkeys="$4"
keyword="$5"

# activate environment
source /data/src/test/selenium/env/bin/activate

./generaltests.py --testname $testname --headless $headless --searchkeys "$searchkeys" --list "$list" --keyword "$keyword" 
echo ./generaltests.py --testname $testname --headless $headless --searchkeys "$searchkeys" --list "$list" --keyword "$keyword" 
}

while read f
  do
  if [ ${#f} -gt $MINCHAR  ]; then
     tests $f  	  
  else
  	echo less than $MINCHAR characters
  fi
done < $TESTLIST


