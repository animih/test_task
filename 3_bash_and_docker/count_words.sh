#!/bin/bash
#Desc: Find out frequency of words in a file

if [ $# -ne 2 ];
then
  echo "Usage: $0 filename1, filename2";
  exit -1
fi

filename1=$1
filename2=$2
egrep -o "\b[[:alpha:]]+\b" $filename1 | \

tr -sc '[:alnum:]' '\n'  < $filename1 | tr  '[:upper:'] '[:lower:]' | sort | uniq -c | tee count_words.txt
IFS=$'\n'
for name in $(sort -k 1 -n -r count_words.txt | head -10)
do
    IFS=$' '
    read -r -a array <<< $name
    num="${array[0]}"
    word="${array[1]}"
    IFS=$'\n'
    dir_name="./${filename2}/${word}_${num}"
    touch $dir_name
done

rm count_words.txt