package main

import "math"

func s(a, b, c []int) float64 {
	return 0.5 * math.Abs((float64)(b[0]-a[0])*(float64)(c[1]-a[1])-(float64)(c[0]-a[0])*(float64)(b[1]-a[1]))
}

func largestTriangleArea(points [][]int) float64 {
	n := len(points)
	res := 0.0
	for i := 0; i < n-2; i++ {
		for j := i + 1; j < n-1; j++ {
			for k := j + 1; k < n; k++ {
				res = math.Max(res, s(points[i], points[j], points[k]))
			}
		}
	}
	return res
}

func main() {
	println(largestTriangleArea([][]int{{0, 0}, {0, 1}, {1, 0}, {0, 2}, {2, 0}}))
	println(largestTriangleArea([][]int{{1, 0}, {0, 0}, {0, 1}}))
}
