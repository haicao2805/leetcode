export function waysToSplitArray(nums: number[]): number {
  const preSumLeft: number[] = [];
  const preSumRight: number[] = [];

  preSumLeft[0] = nums[0];
  for (let i = 1; i < nums.length; i++) {
    preSumLeft[i] = nums[i] + preSumLeft[i - 1];
  }

  preSumRight[nums.length - 1] = nums[nums.length - 1];
  for (let i = nums.length - 2; i >= 0; i--) {
    preSumRight[i] = nums[i] + preSumRight[i + 1];
  }

  let res = 0;
  for (let i = 0; i < nums.length - 1; i++) {
    if (preSumLeft[i] >= preSumRight[i + 1]) {
      res++;
    }
  }

  return res;
}
