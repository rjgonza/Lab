package main

import "fmt"

//only accept a channel for sending
func ping(pings chan<- string, msg string) {
	pings <- msg
}

//pong accept a channel for receiving and one for sending
func pong(pings <-chan string, pongs chan<- string) {
	msg := <-pings
	pongs <- msg
}

func main() {
	pings := make(chan string, 1)
	pongs := make(chan string, 1)
	ping(pings, "passed message")
	pong(pings, pongs)
	fmt.Println(<-pongs)
}
