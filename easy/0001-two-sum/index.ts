export function twoSum(nums: number[], target: number): number[] {
  const map = new Map<number, number>();

  for (let i = 0; i < nums.length; i++) {
    map.set(target - nums[i], i);
  }

  for (let i = 0; i < nums.length; i++) {
    const j = map.get(nums[i]);
    if (j && i !== j) {
      return [i, j];
    }
  }

  return [0, 1];
}
