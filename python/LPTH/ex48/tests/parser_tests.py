#!/usr/bin/python

from nose.tools import *
from ex48 import parser

def test_peek():
	assert_equal(parser.peek([('noun', 'princess'), ('verb', 'kill')]), 'noun')
	assert_equal(parser.peek([]), None)

def test_match():
	assert_equal(parser.match([('noun', 'princess'), ('verb', 'kill')], 'noun'), ('noun', 'princess'))
	assert_equal(parser.match([('noun', 'princess'), ('verb', 'kill')], 'verb'), None)
	assert_equal(parser.match([], 'noun'), None)

def test_skip():
	test_list=[('noun', 'princess'), ('verb', 'kill')]
	parser.skip(test_list, 'noun')
	assert_equal(test_list[0], ('verb', 'kill'))

def test_parse_verb():
	test_list=[('stop', 'the'), ('verb', 'kill')]
	assert_equal(parser.parse_verb(test_list), ('verb' ,'kill'))
	assert_raises(parser.ParserError, parser.parse_verb, test_list)

def test_parse_object():
	test_list=[('stop', 'the'), ('noun', 'princess'), ('direction', 'north')]
	assert_equal(parser.parse_object(test_list), ('noun', 'princess'))
	assert_equal(parser.parse_object(test_list), ('direction', 'north'))
	assert_raises(parser.ParserError, parser.parse_object, test_list)

def test_parse_subject():
	test_list=[('verb', 'kill'), ('stop', 'the'), ('noun', 'bear')]
	test_object=parser.parse_subject(test_list, ('noun', 'princess'))
	assert_equal(test_object.subject, 'princess')
	assert_equal(test_object.verb, 'kill')
	assert_equal(test_object.object, 'bear')

def test_parse_sentence():
	test_list=[('noun', 'princess'), ('verb', 'kill'), ('stop', 'the'), ('noun', 'bear')]
	test_object=parser.parse_sentence(test_list)
	assert_equal(test_object.subject, 'princess')
	assert_equal(test_object.verb, 'kill')
	assert_equal(test_object.object, 'bear')
	assert_raises=(parser.ParserError, parser.parse_sentence,test_list)
	
def test_parse_sentence_player():
	test_list=[('verb', 'kill'), ('stop', 'the'), ('noun', 'bear')]
	test_object=parser.parse_sentence(test_list)
	assert_equal(test_object.subject, 'player')
	assert_equal(test_object.verb, 'kill')
	assert_equal(test_object.object, 'bear')
	assert_raises=(parser.ParserError, parser.parse_sentence,test_list)
