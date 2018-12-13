#!/bin/bash
Grades=()
i=0
while [ $i -lt 6 ];
do
  echo 'Enter Grade'
  read io
  Grades[i]=$io
  ((++i))
done
echo ${Grades[@]}
