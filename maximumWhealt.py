class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        customer_max = 0
        for account in accounts:
            customer_sum = sum(account)
            customer_max = max(customer_max, customer_sum)
        return customer_max 

