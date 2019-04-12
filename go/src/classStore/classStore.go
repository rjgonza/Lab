package main

import (
	"bufio"
	"encoding/csv"
	"fmt"
	"io"
	"log"
	"os"
	"strconv"
)

type Student struct {
	StudentName string `json:"studentName"`
	SpentPoints int    `json:"spentPoints"`
	Positive    int    `json:"positive"`
	NeedsWork   int    `json:"needsWork"`
	TotalPoints int    `json:"totalPoints"`
}

func main() {
	csvFile, _ := os.Open("C:\\Users\\rjgonza\\Desktop\\test.csv")
	reader := csv.NewReader(bufio.NewReader(csvFile))
	var student []Student

	for {
		line, error := reader.Read()
		if error == io.EOF {
			break
		} else if error != nil {
			log.Fatal(error)
		}

		if line[0] == "Student" {
			continue
		}

		spentPointsDB, _ := os.Open("C:\\Users\\rjgonza\\Desktop\\spent.csv")
		spentPointsreader := csv.NewReader(bufio.NewReader(spentPointsDB))
		var spentPoints int
		for {
			spentLine, err := spentPointsreader.Read()
			if err == io.EOF {
				break
			} else if error != nil {
				log.Fatal(err)
			}

			if line[0] == spentLine[0] {
				spentPoints, err = strconv.Atoi(spentLine[1])
				if err != nil {
					log.Fatal(err)
				}
				break
			}
		}

		positive, err := strconv.Atoi(line[32])
		if err != nil {
			log.Fatal(err)
		}
		needsWork, err := strconv.Atoi(line[33])
		if err != nil {
			log.Fatal(err)
		}

		totalPoints := positive - needsWork - spentPoints

		student = append(student, Student{
			StudentName: line[0],
			SpentPoints: spentPoints,
			Positive:    positive,
			NeedsWork:   needsWork,
			TotalPoints: totalPoints,
		})
	}
	// studentJSON, _ := json.Marshal(student)
	// fmt.Println(string(studentJSON))

	for _, s := range student {
		fmt.Printf("%s has %d to spend and has already spent %d points\n", s.StudentName, s.TotalPoints, s.SpentPoints)
	}
}
