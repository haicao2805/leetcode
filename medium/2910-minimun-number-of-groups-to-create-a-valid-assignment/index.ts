type BallNumber = number;
type Seq = number;

function findSmallestAvailable(initial: number, map: Map<BallNumber, Seq>) {
  for (let i = initial; i >= 1; i--) {
    let flag = true;
    for (const [, seq] of map) {
      if (seq % i > (seq - (seq % i)) / i) {
        flag = false;
        break;
      }
    }
    if (flag) {
      return i;
    }
  }

  return 1;
}

export function minGroupsForValidAssignment(balls: number[]): number {
  // Mapping ball -> sequences
  const map: Map<BallNumber, Seq> = new Map();
  for (const ball of balls) {
    const currentSeq = map.get(ball) ?? 0;
    const newCSeq = currentSeq + 1;

    map.set(ball, newCSeq);
  }

  // Find min seq
  let minSeq = balls.length;
  for (const [ball, seq] of map) {
    if (minSeq > seq) {
      minSeq = seq;
    }
  }

  // Find smallest group that available
  const smallest = findSmallestAvailable(minSeq, map);

  // Group ball with this smallest
  let res = 0;
  for (const [, seq] of map) {
    const mod = seq % (smallest + 1);
    res += (seq - mod) / (smallest + 1);

    if (mod !== 0) {
      res++;
    }
  }

  return res;
}
