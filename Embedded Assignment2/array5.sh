#!/bin/bash
# Write a shell scripts to count number of vowels in file ignoring the case.
re='^[aeoiuAEIOU]+$'
echo "Enter the file name"
read file
filecontent=$(cat $file)
contentArray $filecontent
count=0
echo $filecontent
for ((i= 0; i<${#filecontent}; i++));
do
  if [[ "${filecontent:i:1}" =~ $re ]];
  then
    echo $((count+=1));
  fi
done
echo "Number of vowels: "$count
