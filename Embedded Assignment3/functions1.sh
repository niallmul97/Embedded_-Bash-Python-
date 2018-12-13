#!/bin/bash
#!Write a shell script that accepts the year e.g. 1984 and then writes
#!that year vertically to the screen i.e. 1 on first line, 9 on next,
#! 8 on next and 4 on last line.

main(){
  re='^[0-9]+$'
  if [ $# -eq 1 ]
  then
   YEAR=$1
  else
   echo -n "Enter a year: "
   read YEAR
   if ! [[ $YEAR =~ $re ]] ;
   then
      echo "error: non number entered" >&2; exit 1
   elif [[ $YEAR -lt 0 ]];
   then
     echo "error: enter a valid year" >&2; exit 1
   fi
  fi
  seperate_line YEAR
}

seperate_line()
{
  for ((i=0; i<${#YEAR}; i++));
  do
    echo "${YEAR:i:1}";
  done
}
main
