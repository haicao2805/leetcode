class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = 1 if numerator * denominator > 0 else -1
        numerator = abs(numerator)
        denominator = abs(denominator)
        integral = numerator // denominator
        remainder = numerator % denominator

        if remainder == 0:
            return str("-" if sign == -1 and integral != 0 else "") + str(integral)
        integralStr = str("-" if sign == -1 else "") + str(integral)

        decimal = []
        trace = []

        remainderMap = {}
        while remainder != 0:
            if remainder in remainderMap and remainderMap.get(remainder):
                break

            if remainder not in remainderMap:
                remainderMap[remainder] = False

            remainder *= 10
            decimal.append(remainder // denominator)
            remainder = remainder % denominator
            trace.append(remainder)
            if remainder in remainderMap:
                remainderMap[remainder] = True

        if trace[-1] == 0:
            return integralStr + "." + "".join(str(d) for d in decimal)
        else:
            found = trace.index(trace[-1])
            if found == len(trace) - 1:
                return integralStr + "." + "(" + "".join(str(d) for d in decimal) + ")"
            else:
                return (
                    integralStr
                    + "."
                    + "".join(
                        str((str(decimal[i]) + "(") if i == found else decimal[i])
                        for i in range(len(decimal))
                    )
                    + ")"
                )


if __name__ == "__main__":
    s = Solution()
    print(s.fractionToDecimal(0, 3))
