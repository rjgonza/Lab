package main

import "time"
import "fmt"

func main() {
	//Timer represent a single event in the future.
	//You tell the timer how long you want to wait, and it
	//provides a channel that will be notified as that time.
	timer1 := time.NewTimer(time.Second * 2)

	<-timer1.C
	fmt.Println("Timer 1 expired")

	timer2 := time.NewTimer(time.Second)
	go func() {
		<-timer2.C
		fmt.Println("Timer 2 expired")
	}()

	stop2 := timer2.Stop()
	if stop2 {
		fmt.Println("Timer 2 stopped")
	}
}
