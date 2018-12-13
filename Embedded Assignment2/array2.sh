#!/bin/bash
# Write a shell script that accepts 10 integers from a user into an array.
# Sort this array in both descending and ascending order.
Int=()
re='^[0-9]+$'

echo "Enter a number"

while [[ $i -lt 10 ]]; do
  echo "Number: "
  read io
  if ! [[ $io =~ $re ]] ;
  then
    echo 'error: Not a valid input' >&2; exit 1
  else
    Int[$i]=${io}
    let i+=1
  fi
done

IFS=$'\n' sorted=($(sort -n <<<"${Int[*]}"))
echo "Array in asecending order" "${sorted[@]}"

IFS=$'\n' sorted=($(sort -r -n <<<"${Int[*]}"))
echo "Array in desecending order" "${sorted[@]}"
