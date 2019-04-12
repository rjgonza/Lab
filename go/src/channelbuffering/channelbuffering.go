package main

import "fmt"

//by default channels are unbuffered, meaning that
//they will only accept sends (chan <- ) if there
//is a corresponding receive(<- chan) reaady to
//receive the send value.
func main() {
	messages := make(chan string, 2)

	messages <- "buffered"
	messages <- "channel"

	fmt.Println(<-messages)
	fmt.Println(<-messages)
}
