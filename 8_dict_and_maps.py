#!/bin/python3

import sys

# number of entries in phonebook
n = int(input().strip())
phone_book = {}

# make a phonebook
for num in range(n):
    name, phone = input().strip().split(" ")
    phone_book[name] = phone   

# find numbers 
while True:
    try:
        query_name = input().strip()
        if query_name in phone_book:
            print("{}={}".format(query_name, phone_book[query_name]))
        else:
            print("Not found")
    except EOFError:
        break
