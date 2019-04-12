package main

import "fmt"

func main() {
	æ := ""
	for _, char := range []rune{'æ', 0xE6, 0346, 230, '\xE6', '\u00E6'} {
		fmt.Printf("[0x%X '%c'] ", char, char)
		æ += string(char)
		fmt.Print(char)
	}

	fmt.Print(æ + "\n")
}