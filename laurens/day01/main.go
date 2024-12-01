package main

import (
	"fmt"
	"log"
	"os"
	"slices"
	"strconv"
	"strings"
)

func main() {
	filename := "challenge.txt"
	if len(os.Args) > 1 {
		filename = os.Args[1]
	}

	data, err := os.ReadFile(filename)
	if err != nil {
		log.Fatalf("failed to read file: %v", err)
	}

	part1, part2 := solve(string(data))
	fmt.Printf("Part 1: %d\n", part1)
	fmt.Printf("Part 2: %d\n", part2)
}

func solve(input string) (int, int) {
	lines := strings.Split(strings.TrimSpace(input), "\n")

	listOne := make([]int, len(lines))
	listTwo := make([]int, len(lines))

	for i := 0; i < len(lines); i++ {
		values := strings.Split(lines[i], "   ")

		listOne[i], _ = strconv.Atoi(values[0])
		listTwo[i], _ = strconv.Atoi(values[1])
	}

	part1 := part1(listOne, listTwo)
	part2 := part2(listOne, listTwo)

	return part1, part2
}

func part1(listOne []int, listTwo []int) int {
	slices.Sort(listOne)
	slices.Sort(listTwo)

	totalDifference := 0
	for i := 0; i < len(listOne); i++ {
		totalDifference += getDifference(listOne[i], listTwo[i])
	}

	return totalDifference
}

func part2(listOne []int, listTwo []int) int {
	totalSimilarity := 0

	for _, value := range listOne {
		totalSimilarity += getSimilarityScore(value, listTwo)
	}

	return totalSimilarity
}

func getDifference(int1 int, int2 int) int {
	if int1 > int2 {
		return int1 - int2
	}

	return int2 - int1
}

func getSimilarityScore(int int, values []int) int {
	occurrence := 0

	for _, value := range values {
		if int == value {
			occurrence++
		}
	}

	return int * occurrence
}
