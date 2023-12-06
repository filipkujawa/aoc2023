package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"strings"
	"strconv"
)

func getInput(filePath string) []string {
	content, err := ioutil.ReadFile(filePath)
	if err != nil {
		panic(err)
	}
	lines := strings.Split(string(content), "\n")
	return lines
}

func main() {
	lines := getInput("input.txt")

	timeStr := strings.Split(lines[0], ":")[1]
	distanceStr := strings.Split(lines[1], ":")[1]

	time, err := strconv.Atoi(strings.ReplaceAll(timeStr, " ", ""))
	if err != nil {
		panic(err)
	}

	distance, err := strconv.Atoi(strings.ReplaceAll(distanceStr, " ", ""))
	if err != nil {
		panic(err)
	}

	a := -1
	b := time
	c := -1 * distance

	d := (b * b) - (4 * a * c)

	sol1 := int(math.Ceil((-float64(b) - math.Sqrt(float64(d))) / (2 * float64(a))))
	sol2 := int(math.Ceil((-float64(b) + math.Sqrt(float64(d))) / (2 * float64(a))))

	result := int(math.Abs(float64(sol1 - sol2)))

	fmt.Println(result)
}
