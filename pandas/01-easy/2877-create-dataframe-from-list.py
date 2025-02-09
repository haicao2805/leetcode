import pandas as pd
import numpy as np
from typing import List


def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df = pd.DataFrame(student_data, columns=np.array(["student_id", "age"]))
    return df


if __name__ == "__main__":
    print(createDataframe([[1, 15], [2, 11], [3, 11], [4, 20]]))
