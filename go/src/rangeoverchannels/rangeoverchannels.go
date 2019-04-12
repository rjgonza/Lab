package main

import "fmt"

func main() {
	queue := make(chan string, 2)
	queue <- "one"
	queue <- "two"
	close(queue)

	//if the channel was not closed then we would block after one and two
	for elem := range queue {
		fmt.Println(elem)
	}
}
