package main

import "time"
import "fmt"

func main() {
	//tickers are used to do something repetedly at regular intervals

	//same deal as timers, they create a channel for you to send values on
	ticker := time.NewTicker(time.Millisecond * 500)
	go func() {
		for t := range ticker.C {
			fmt.Println("Tick at", t)
		}
	}()

	time.Sleep(time.Millisecond * 1500)
	ticker.Stop()
	fmt.Println("Ticker stopped")
}
