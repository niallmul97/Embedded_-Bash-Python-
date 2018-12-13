#!/bin/bash
# Write a shell script to accept 12 grades and display average,
# average for semester 1 (first six grades) and average for semester 2
# (second six grades) in the array (populated by the user).
# Also, calculate the max and min values in the array.
Grade=()
AVG=0
SEM1=0
SEM2=0
MIN=101
MAX=0
i=0
re='^[0-9]+$'

echo "Enter your grade for each module"

while [[ $i -lt 12 ]]; do
  echo "Grade: "
  read io
  if ! [[ $io =~ $re ]] ;
  then
    echo 'error: Not a valid input' >&2; exit 1
  elif [[ $io -gt 100 ]]; then
    echo "Grade entered was too high" >&2; exit 1
  else
    Grade[$i]=${io}
    if [[ $io -gt $MAX ]]; then
      MAX=$io
    fi
    if [[ $io -lt $MIN ]]; then
      MIN=$io
    fi
    let i+=1
    AVG=$(($AVG + $io))
  fi
done
echo "Average grade: " $(($AVG / 12))

for n in "${Grade[@]:0:6}"
do
  SEM1=$(($SEM1 + n))
done
echo "Semester 1 average: " $(($SEM1 / 6))

for n in "${Grade[@]:6:12}"
do
  SEM2=$(($SEM2 + n))
done
echo "Semester 2 average: " $(($SEM2 / 6))

echo "Your highest grade was: " $MAX

echo "Your lowest grade was: " $MIN
