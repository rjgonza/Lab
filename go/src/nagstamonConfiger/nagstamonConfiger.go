package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"os/user"
	"path"
	"path/filepath"
	"strings"
	"time"
)

var nagstamonConfigs = [2]string{"nagstamon.conf", "servers"}

func main() {
	var backup bool
	now := time.Now()
	usr, err := user.Current()
	if err != nil {
		log.Fatal(err)
	}

	configDir := path.Join(usr.HomeDir, ".nagstamon")
	_, err = os.Stat(configDir)
	if err != nil {
		log.Fatal(err)
	}

	var newNagstamonConfigsSource = path.Join(usr.HomeDir, "repos", "IEX", "sre-nagios")
	reader := bufio.NewReader(os.Stdin)
	fmt.Printf("Location of NEW nagstamon configs (Default %s):", newNagstamonConfigsSource)
	answer, _ := reader.ReadString('\n')
	fmt.Printf("Answer: '%s'", answer)
	if answer != "\n" {
		newNagstamonConfigsSource = answer
	}
	for _, conf := range nagstamonConfigs {
		fmt.Printf("Going to use %s from %s", conf, newNagstamonConfigsSource)
	}

	dir, err := filepath.Abs(filepath.Dir(os.Args[0]))
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(dir)

	reader = bufio.NewReader(os.Stdin)
	fmt.Print("Would you like to backup the current configs? [Y/N]:")
	answer, _ = reader.ReadString('\n')
	if strings.Contains(answer, "Y") || strings.Contains(answer, "y") {
		backup = true
	}

	for _, confFile := range nagstamonConfigs {
		if _, err = os.Stat(path.Join(configDir, confFile)); err == nil && backup {
			err = os.Rename(path.Join(configDir, confFile),
				path.Join(configDir, fmt.Sprintf("%s_rollback_%d%02d%02d_%02d%02d%02d",
					confFile,
					now.Year(), now.Month(), now.Day(),
					now.Hour(), now.Minute(), now.Second())))
			if err != nil {
				log.Fatal(err)
			}
		}

		err = os.Rename(confFile, configDir)
		if err != nil {
			log.Fatal(err)
		}
	}
}
