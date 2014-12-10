package main

import "fmt"

func main() {
	ae := ""
	for _, char := range []rune{1, 0xE6, 0346, 230, '\xE6', '\u00E6'} {
		fmt.Printf("[0x%X '%c'] ", char, char)
		ae += string(char)
		fmt.Print(char)
	}

	fmt.Print(ae)
}