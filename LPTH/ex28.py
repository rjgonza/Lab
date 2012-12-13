print "Test\t\tRays Answer"

print "1. True and True\tTrue"
print "%r\n" % (True and True)

print "2. False and True\tFalse"
print "%r\n" % (False and True)

print "3. 1 == 1 and 2 == 1\tFalse"
print "%r\n" % ( 1 == 1 and 2 == 1 )

print "4. \"test\" == \"test\"\tTrue"
print "%r\n" % ( "test" == "test")

print "5. 1 == 1 or 2 != 1\tTrue"
print "%r\n" % ( 1 == 1 or 2 != 1 )

print "6. True and 1 == 1\tTrue"
print "%r\n" % ( True and 1 == 1 )

print "7. False and 0 != 0\tFalse"
print "%r\n" % ( False and 0 != 0 )

print "8. True or 1 == 1\tTrue"
print "%r\n" % ( True or 1 == 1 )

print "9. \"test\" == \"testing\"\tFalse"
print "%r\n" % ( "test" == "testing" )

print "10. 1 != 0 and 2 == 1\tFalse"
print "%r\n" % (1 != 0 and 2 == 1 )

print "11. \"test\" != \"testing\"\tTrue"
print "%r\n" % ( "test" != "testing" )

print "12. \"test\" == 1\tFalse"
print "%r\n" % ( "test" == 1 )

print "13. not (True and False)\tTrue"
print "%r\n" % ( not (True and False) )

print "14. not (1 == 1 and 0 != 1)\tFalse"
print "%r\n" % ( not ( 1 == 1 and 0 != 1 ) )

print "15. not (10 == 1 or 1000 == 1000)\tFalse"
print "%r\n" % ( not ( 10 == 1 or 1000 == 1000 ) )

print "16. not (1 != 10 or 3 == 4)\tFalse"
print "%r\n" % ( not (1 != 10 or 3 == 4) )

print "17. not (\"testing\" == \"testing\" and \"Zed\" == \"Cool Guy\")\tTrue"
print "%r\n" % ( not ("testing" == "testing" and "Zed" == "Cool Guy" ) )

print "18. 1 == 1 and not (\"testing\" == 1 or 1 == 0)\tTrue"
print "%r\n" % ( 1 == 1 and not ( "testing" == 1 or 1 == 0 ) )

print "19. \"chunky\" == \"bacon\" and not (3 == 4 or 3 == 3)\tFalse"
print "%r\n" % ( "chunky" == "bacon" and not (3 == 4 or 3 == 3) )

print "20. 3 == 3 and not (\"testing\" == \"testing\" or \"Python\" == \"Fun\")\tFalse"
print "%r\n" % ( 3 == 3 and not ("testing" == "testing" or "Python" == "Fun") )
