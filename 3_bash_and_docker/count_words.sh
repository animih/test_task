#!/bin/bash
#Desc: Find out frequency of words in a file

if [ $# -ne 1 ];
then
  echo "Usage: $0 filename1";
  exit -1
fi

filename1=$1

egrep -o "\b[[:alpha:]]+\b" $filename1 | \

tr -sc '[:alnum:]' '\n'  < $filename1 | tr  '[:upper:'] '[:lower:]' | sort | uniq -c 
