#!/usr/bin/python

print "content-type: text/plain\n\n"
import cgi

form = cgi.FieldStorage()
number = form.getvalue("number")

print "You entered the number: " + number
print

command = "result = " + number + "*2"
print "I am running the following python code: "
print command
print

exec(command)

print "I got the following result:"
print result
