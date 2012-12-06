#!/usr/bin/python

from nose.tools import *
from ex48 import parser

def test_peek():
	assert_equal(parser.peek(['first', 'second']), 'first')
	assert_equal(parser.peek([]), None)

def test_match():
	assert_equal(parser.match(['first', 'second'], 'first'), 'first')
	assert_equal(parser.match(['first', 'second'], 'third'), None)
	assert_equal(parser.match([], 'third'), None)

def test_skip():
	assert_equal(parser.skip(['first', 'second'], 'first'), 'first')
