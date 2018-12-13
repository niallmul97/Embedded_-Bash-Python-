#!/bin/bash
# Write a script to find out if a string entered by the user is
# palindrome or not.  A palindrome is a word that spells the same
# forwards and backwards.
echo "Enter a string"
read STR
Palindrome=True
for ((i=0; i<${#STR}; i++));
do
  FWD[$i]="${STR:i:1}";
done
j=0
for ((i=((${#STR} - 1)); i>=0; i--));
do
  REV[$j]=${FWD[i]};
  ((j++))
done
for ((i=0; i<=${#STR}; i++));
do
  if ! [[ ${FWD[$i]} == ${REV[$i]} ]]; then
    Palindrome=False
  fi
done
if [[ $Palindrome == True ]]; then
  echo "Your string is a palindrome"
else
  echo "Your string is not a palindrome"
fi
