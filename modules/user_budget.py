from time import sleep


class UserBudget:

    def __init__(self, budget):
        self.budget = budget

    def compare(self, price):
        if price <= self.budget:
            return [True, budget-price]
        else:
            return [False, price-budget]
