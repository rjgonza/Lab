package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"os/user"
	"path/filepath"
	"strings"
	"time"
)

var nagstamonConfigs = [2]string{"nagstamon.conf", "servers"}
var src, dst string

func main() {
	backup := true
	now := time.Now()
	usr, err := user.Current()
	if err != nil {
		log.Fatal(err)
	}

	configDir := filepath.Join(usr.HomeDir, ".nagstamon")
	_, err = os.Stat(configDir)
	if err != nil {
		log.Fatal(err)
	}

	var newNagstamonConfigsSource = filepath.Join(usr.HomeDir, "repos", "IEX", "sre-nagios")
	reader := bufio.NewReader(os.Stdin)

	fmt.Printf("Enter NEW location of nagstamon configs (Default:s %s) [Y/N]?:", newNagstamonConfigsSource)
	answer, err := reader.ReadString('\n')
	if err != nil {
		log.Fatal(err)
	}
	if strings.Contains(answer, "Y") || strings.Contains(answer, "y") {
		fmt.Printf("NEW path:")
		answer, err = reader.ReadString('\n')
		newNagstamonConfigsSource = answer
	}

	for _, conf := range nagstamonConfigs {
		fmt.Printf("Going to use %s from %s\n", conf, newNagstamonConfigsSource)
	}

	fmt.Printf("\nWould you like to backup the current configs? (Default: %t) [Y/N]:", backup)
	answer, err = reader.ReadString('\n')
	if err != nil {
		log.Fatal(err)
	}
	if strings.Contains(answer, "N") || strings.Contains(answer, "n") {
		backup = false
	}

	for _, confFile := range nagstamonConfigs {
		if _, err = os.Stat(filepath.Join(configDir, confFile)); err == nil && backup {
			err = os.Rename(filepath.Join(configDir, confFile),
				filepath.Join(configDir, fmt.Sprintf("%s_rollback_%d%02d%02d_%02d%02d%02d",
					confFile,
					now.Year(), now.Month(), now.Day(),
					now.Hour(), now.Minute(), now.Second())))
			if err != nil {
				log.Fatal(err)
			}
		} else {
			err = os.RemoveAll(filepath.Join(configDir, confFile))
			if err != nil {
				log.Fatal(err)
			}
		}

		src = filepath.Join(newNagstamonConfigsSource, confFile)
		dst = filepath.Join(configDir, confFile)
		srcInfo, err := os.Stat(src)
		if err != nil {
			log.Fatal(err)
		}
		if srcInfo.IsDir() {
			srcFiles, err := ioutil.ReadDir(src)
			if err != nil {
				log.Fatal(err)
			}

			err = os.Mkdir(dst, 0755)
			if err != nil {
				log.Fatal(err)
			}

			for _, srcFile := range srcFiles {
				fmt.Printf("Moving %s from %s to %s\n", srcFile.Name(), dst)
				err = os.Link(filepath.Join(src, srcFile.Name()), filepath.Join(dst, srcFile.Name()))
				if err != nil {
					log.Fatal(err)
				}
			}
		} else {
			fmt.Printf("Moving %s from %s to %s\n", confFile, newNagstamonConfigsSource, dst)
			err = os.Link(src, dst)
			if err != nil {
				log.Fatal(err)
			}
		}
	}
}
