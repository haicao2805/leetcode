export function minOperations(nums: number[], x: number): number {
  const left: number[] = [];
  const right: number[] = [];
  const mapLeft: Map<number, number> = new Map();
  const mapRight: Map<number, number> = new Map();

  left[0] = nums[0];
  mapLeft.set(left[0], 1);
  for (let i = 1; i < nums.length; i++) {
    left[i] = nums[i] + left[i - 1];
    mapLeft.set(left[i], i + 1);
  }

  right[0] = nums[nums.length - 1];
  mapRight.set(right[0], 1);
  for (let i = 1; i < nums.length; i++) {
    right[i] = nums[nums.length - 1 - i] + right[i - 1];
    mapRight.set(right[i], i + 1);
  }

  let res = nums.length + 1;
  for (const value of left) {
    const l = mapLeft.get(value);
    if (l && value === x) {
      res = Math.min(res, l);
      continue;
    }

    const r = mapRight.get(x - value);
    if (l && r) {
      res = Math.min(res, l + r);
    }
  }

  for (const value of right) {
    const r = mapRight.get(value);
    if (r && value === x) {
      res = Math.min(res, r);
      continue;
    }

    const l = mapLeft.get(x - value);
    if (l && r) {
      res = Math.min(res, l + r);
    }
  }

  return res <= nums.length ? res : -1;
}
