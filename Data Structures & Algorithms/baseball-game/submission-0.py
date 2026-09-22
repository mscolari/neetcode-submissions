class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        total_score = 0

        for op in operations:
            n = len(record)

            if op == '+':
                record.append(record[n-1] + record[n-2])
            elif op == 'D':
                record.append(2 * record[n-1])
            elif op =='C':
                    record.pop()
            else:
                record.append(int(op))

        return sum(record)