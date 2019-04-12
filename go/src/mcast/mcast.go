package main

import (
	"net"
	"log"
)

func main() {
	socket, err := net.ListenUDP("udp4", &net.UDPAddr{
		IP:   net.IPv4zero,
		Port: 8888,
	})
	if err != nil {
		log.Fatal(err)
	}
	defer socket.Close()

	err = socket.JoinGroup(net.IPv4(239, 1, 1, 3))
	if err != nil {
		log.Fatal(err)

	}
	for {
		buff := make([]byte, 4096)
		read, err := socket.Read(buff)
		if err != nil {
			log.Fatal(err)
		}
		//msg := &dns.Msg{}
		//msg.Unpack(buff[:read])
		//log.Println(msg.String())
	}
}