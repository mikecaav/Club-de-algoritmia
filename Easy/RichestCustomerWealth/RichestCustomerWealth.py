def solution1(self, accounts):
    maxWealth = 0
    for account in accounts:
        maxWealth = max(sum(account), maxWealth)
    return maxWealth

def solution2(self, accounts):
    return max([sum(account) for account in accounts])