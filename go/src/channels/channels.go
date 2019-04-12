package main

import "fmt"

func main() {
	messages := make(chan string)

	go func() { messages <- "ping" }()

	msg := <-messages
	fmt.Println(msg)

	//by default sends and receives block
	//until both the send and the receiver
	//are ready. This property allowed us
	//to wait at the end of our program for
	//the "ping" message without having to
	//us any other synchronization.
}
