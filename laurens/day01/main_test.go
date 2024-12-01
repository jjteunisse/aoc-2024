package main

import (
	"os"
	"testing"
)

func TestSolve(t *testing.T) {
	data, err := os.ReadFile("example.txt")
	if err != nil {
		t.Fatalf("failed to read file: %v", err)
	}

	part1, part2 := solve(string(data))

	expectedPart1 := 11
	expectedPart2 := 31

	if part1 != expectedPart1 {
		t.Fatalf("Part 1 failed: got %d, expected %d", part1, expectedPart1)
	}
	if part2 != expectedPart2 {
		t.Fatalf("Part 2 failed: got %d, expected %d", part2, expectedPart2)
	}
}
