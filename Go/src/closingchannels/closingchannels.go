package main

import "fmt"

func main() {
	jobs := make(chan int, 5)
	done := make(chan bool)

	go func() {
		for {
			//more will be false if the channel has be closed and all the values
			//in the channel have been received
			j, more := <-jobs
			if more {
				fmt.Println("received job", j)
			} else {
				fmt.Println("received all jobs")
				done <- true
				return
			}
		}
	}()

	for j := 0; j <= 3; j++ {
		jobs <- j
		fmt.Println("sent job", j)
	}
	//means that no more values will be sent on this channel
	close(jobs)
	fmt.Println("sent all jobs")

	//channel sync
	<-done
}
