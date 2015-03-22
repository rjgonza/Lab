package main

import "os"
import "fmt"

func main() {
	argsWithProg := os.Args
	argsWithoutProg := os.Args[1:]

	args := os.Args[3]

	fmt.Println(argsWithProg)
	fmt.Println(argsWithoutProg)
	fmt.Println(args)
}
