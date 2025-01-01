export function containsDuplicate(nums: number[]): boolean {
  const set: Set<number> = new Set();

  for (const num of nums) {
    const foundInSet = set.has(num);

    if (!foundInSet) {
      set.add(num);
      continue;
    }

    return true;
  }

  return false;
}
