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

	timesStr := strings.Split(lines[0], ":")[1]
	distancesStr := strings.Split(lines[1], ":")[1]

	times := make([]int, 0)
	distances := make([]int, 0)

	for _, t := range strings.Fields(timesStr) {
		val, err := strconv.Atoi(t)
		if err != nil {
			panic(err)
		}
		times = append(times, val)
	}

	for _, d := range strings.Fields(distancesStr) {
		val, err := strconv.Atoi(d)
		if err != nil {
			panic(err)
		}
		distances = append(distances, val)
	}

	x := make([]int, 0)

	for r := 0; r < len(times); r++ {
		a := -1
		b := times[r]
		c := -1 * distances[r]

		d := (b*b) - (4*a*c)

		sol1 := int(math.Ceil((-float64(b) - math.Sqrt(float64(d))) / (2 * float64(a))))
		sol2 := int(math.Ceil((-float64(b) + math.Sqrt(float64(d))) / (2 * float64(a))))

		x = append(x, int(math.Abs(float64(sol1 - sol2))))
	}

	result := 1
	for _, i := range x {
		result *= i
	}

	fmt.Println(result)
}
