#!/usr/bin/bash
#Fixed value decleration
naira=736

#Read user name and amount to convert
echo "Hello, i'm Mallam B, i'll help you convert your money
The current rate is $naira to 1 dollar"

read -p "what is your name? " name
read -p "How much dollar do you want to convert? " dollar

sleep 1
#calculate
result=$(($dollar*$naira))

#display output
echo "Hello $name, $ $dollar na $result naira"
sleep 2
echo "Thanks for your patronage"
