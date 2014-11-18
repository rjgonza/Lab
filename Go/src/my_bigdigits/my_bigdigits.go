package main

import (
    "fmt"
    "log"
    "os"
    "path/filepath"
    "flag"
    "strings"
)

var barPtr bool
var starPtr bool

func usage() {
    fmt.Printf("usage: %s [-b|-bar] [-s|-star] <whole-number>\n", filepath.Base(os.Args[0]))
    os.Exit(1)
}

func init() {
    flag.BoolVar(&barPtr, "bar", false, "Print a border around the numbers using the _ character")
    flag.BoolVar(&barPtr, "b", false, "Print a border around the numbers using the _ character")
    flag.BoolVar(&starPtr, "star", false, "Print a border around the numbers using the * character")
    flag.BoolVar(&starPtr, "s", false, "Print a border around the numbers using the * character")

    flag.Parse()

    if barPtr && starPtr {
        fmt.Print("Cannot choose both a * and _ for the border\n")
        usage()
    }
}

func main() {
    if len(os.Args) == 1 {
        usage()
    }

    var border string

    if barPtr {
        border = "_"
    } else if starPtr {
        border = "*"
    } else {
        border = ""
    }

    stringOfDigits := os.Args[len(os.Args) - 1]
    for row := range bigDigits[0] {
        line := ""
        for column := range stringOfDigits {
            digit := stringOfDigits[column] - '0'
            if 0 <= digit && digit <= 9 {
                line += bigDigits[digit][row] + "  "
            } else {
                log.Fatal("invalid whole number")
            }
        }
        if row == 0 {
            fmt.Println(strings.Repeat(border, len(line)))
        }
        fmt.Println(line)
        if row + 1 == len(bigDigits[0]){
            fmt.Println(strings.Repeat(border, len(line)))
        }
    }
}

var bigDigits = [][]string{
    {"  000  ",
     " 0   0 ",
     "0     0",
     "0     0",
     "0     0",
     " 0   0 ",
     "  000  "},

    {" 1 ",
     "11 ",
     " 1 ", 
     " 1 ", 
     " 1 ", 
     " 1 ", 
     "111"},

    {" 222 ", 
     "2   2", 
     "   2 ", 
     "  2  ", 
     " 2   ", 
     "2    ", 
     "22222"},

    {" 333 ", 
    "3   3", 
    "    3", 
    "  33 ", 
    "    3", 
    "3   3", 
    " 333 "},

    {"   4  ", 
     "  44  ", 
     " 4 4  ", 
     "4  4  ", 
     "444444", 
     "   4  ",
     "   4  "},

    {"55555", 
     "5    ", 
     "5    ", 
     " 555 ", 
     "    5", 
     "5   5", 
     " 555 "},

    {" 666 ", 
    "6    ", 
    "6    ", 
    "6666 ", 
    "6   6", 
    "6   6", 
    " 666 "},

    {"77777", 
     "    7", 
     "   7 ", 
     "  7  ", 
     " 7   ", 
     "7    ", 
     "7    "},

    {" 888 ", 
     "8   8", 
     "8   8", 
     " 888 ", 
     "8   8", 
     "8   8", 
     " 888 "},

    {" 9999", 
     "9   9", 
     "9   9", 
     " 9999", 
     "    9", 
     "    9", 
     "    9"},
}