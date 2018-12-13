#!/bin/bash
# Write a shell script that passes a person’s age to a function.
# If the age greater than 21 the script will display
# the message “Adult” otherwise, the script will display
# the message “Not an Adult”.
main(){
  re='^[0-9]+$'
  if [ $# -eq 1 ]
  then
   AGE=$1
  else
   echo -n "Enter your age: "
   read AGE
   if ! [[ $AGE =~ $re ]] ;
   then
      echo "error: non number entered" >&2; exit 1
   elif [[ $YEAR -le 0 ]];
   then
     echo "error: enter a valid age" >&2; exit 1
   fi
  fi
  age_check AGE
}

age_check()
{
  if [[ $AGE -ge 21 ]];
  then
    echo "Adult"
  else
    echo "Not an adult"
  fi
}
main
