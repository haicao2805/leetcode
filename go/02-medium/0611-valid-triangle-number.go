package main

import "sort"

func binarySearch(l int, r int, nums []int, sum int) int {
	for l <= r {
		m := l + (r-l)/2
		if nums[m] < sum {
			l = m + 1
		} else {
			r = m - 1
		}
	}
	return l
}

func triangleNumber(nums []int) int {
	n := len(nums)
	if n < 3 {
		return 0
	}

	sort.Slice(nums, func(i, j int) bool {
		return nums[i] < nums[j]
	})

	res := 0
	for i := 0; i < n-2; i++ {
		for j := i + 1; j < n-1; j++ {
			res += binarySearch(j+1, n-1, nums, nums[i]+nums[j]) - j - 1
		}
	}

	return res
}

func main() {
	println(triangleNumber([]int{2, 2, 3, 4}))
}
