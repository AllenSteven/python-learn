#!/usr/bin/env python3
#-*-coding:utf-8-*-

from io import StringIO

f = StringIO()
f.write('hello')
f.write(' world!')
print(f.getvalue())
f.close()

f = StringIO('Hello !\nHi!\nGoodbye!')
while True:
	s = f.readline()
	if s == '':
		break
	print(s.strip())
f.close()