#!/usr/bin/python

def Print1():
	print "Hello World1";
	Print2();

def Print2():
	print "Hello World2";
	Print3();

def Print3():
	print "Hello World3";

def PrintMaster():
	Print1();
	Print2();
	Print3();

PrintMaster();




