import { minGroupsForValidAssignment } from "./medium/2910-minimun-number-of-groups-to-create-a-valid-assignment";

console.log(minGroupsForValidAssignment([3, 2, 3, 2, 3]) === 2);
console.log(minGroupsForValidAssignment([10, 10, 10, 3, 1, 1]) === 4);
console.log(minGroupsForValidAssignment([2, 3, 2, 2, 2]) === 3);
console.log(minGroupsForValidAssignment([3, 2, 2, 1, 1, 1, 2]) === 5);
console.log(minGroupsForValidAssignment([1, 2, 3, 1, 1, 3, 1, 3]) === 5);
console.log(
  minGroupsForValidAssignment([1, 1, 3, 3, 1, 1, 2, 2, 3, 1, 3, 2]) === 5,
);

console.log(
  minGroupsForValidAssignment([3, 1, 3, 2, 3, 2, 2, 1, 1, 2, 2, 2, 3, 2, 2]) ===
    4,
);

console.log(
  minGroupsForValidAssignment([
    1, 1, 2, 2, 3, 3, 2, 2, 2, 3, 2, 2, 3, 1, 2, 2, 2, 2,
  ]) === 5,
);
