export function minOperations(nums: number[], x: number): number {
  const left: number[] = [];
  const right: number[] = [];

  let res = nums.length + 1;

  left[0] = nums[0];
  for (let i = 1; i < nums.length; i++) {
    left[i] = nums[i] + left[i - 1];
  }
  right[0] = nums[nums.length - 1];
  for (let i = 1; i < nums.length; i++) {
    right[i] = nums[nums.length - 1 - i] + right[i - 1];
  }

  for (let i = 0; i < left.length; i++) {
    if (left[i] === x) {
      res = Math.min(res, i + 1);
      break;
    }

    for (let j = 0; j < right.length; j++) {
      if (left[i] + right[j] === x) {
        res = Math.min(res, i + j + 2);
        break;
      }

      if (left[i] + right[j] > x) {
        break;
      }
    }
  }

  for (let i = 0; i < right.length; i++) {
    if (right[i] === x) {
      res = Math.min(res, i + 1);
      break;
    }

    for (let j = 0; j < left.length; j++) {
      if (right[i] + left[j] === x) {
        res = Math.min(res, i + j + 2);
        break;
      }

      if (right[i] + left[j] > x) {
        break;
      }
    }
  }

  return res <= nums.length ? res : -1;
}
