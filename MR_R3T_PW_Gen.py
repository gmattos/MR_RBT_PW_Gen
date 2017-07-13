#!/usr/bin/python
#!python3
# -*- coding: utf-8 -*-
#
#  MR_R3T_PW_Gen.py
#  
#  Copyright 2017 gmattos <gmattos@protonmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
# 
#  
#  

import sys, os
import itertools


def clnw(modelos, palavra):
	
	for a in modelos:
		
		palavra = palavra.replace(a, "")
		
	lx = palavra
	
	if lx != "":
		return lx 
	else: return ""	

def fixw(rst, plvr,total):
	if total == plvr.rfind(rst):
		return plvr
	else:
		st = plvr.rfind(rst)
		fn = len(plvr) -1
		
		plvrl = list(plvr)
		rstl = list(rst)
		
		while fn >= st:
			
			del plvrl[fn]
			 
			fn = fn-1
		fix = ''.join(plvrl)
		
		return fix
	
mini = sys.argv[1]
print(mini)
maxi = sys.argv[2]
print(maxi)
if int(maxi) > 24:
	print(">>For secure, the max of range of string was setup as 24<<")
	print("Old value: " + maxi)
	maxi = 24

maxi = int(maxi)
mini = int(mini)	

words = sys.argv[3:]
words.sort()
words.sort(key=len, reverse=True)
print(words)
wn = len(words)
i=0

while i != wn:
	words[i] = words[i].title()
	i=i+1

print("Inserted Words: " + str(len(words)))
print("Loading...")
cw = 0
cutd = 0
nwords = []
tmp = ""
for word in map(''.join, itertools.permutations(words, r=wn)):
	cw = cw+1
	if len(word) <= maxi:
		nwords.append(word)
		nwords = list(set(nwords))
			
	else:
				#Permutations, slicing of the big ones
		z = mini
		
		while z <= maxi:
		
			word2 = word[:z]
			tmp = clnw(words, word2)
			word2 = fixw(tmp,word2,z)
			nwords.append(word2)
			nwords = list(set(nwords))
			nwords.sort(key=len, reverse=True)
			z = z+1
			wn = wn-1

#print(sorted(nwords))

temp = "temp.txt"

f = open(temp, "w")

for w in nwords:
	w = w.strip()
	f.write(w + '\n')

f.close()

inp = "temp.txt" #input file
outp =  "MR_R3T_PW_Gen.txt"

i = -1
f = open(inp, "r") #input file
f2 = open(outp, "w") #output file

for line in f:
	line = line.strip()
	n_line = line #title change
	f2.write(n_line + '\n')
	n_line = line.lower() #lower change
	f2.write(n_line + '\n')
	n_line = line.upper() #upper change
	f2.write(n_line + '\n')

f.close()
f2.close()

os.remove("temp.txt")

print('\n' + "Finished!")
print("\n Rough Combinations Words Count: " + str(cw))

print("\n Total Pure Combinations: " + str(len(nwords)))

print("\n With UPPERED lowered and Titled words: " + str(len(nwords)*3))