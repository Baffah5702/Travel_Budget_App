
class TripBudget:
    def __init__(self, total_budget, duration, exchange_rate):
        self.total_budget = total_budget
        self.duration = duration
        self.exchange_rate = exchange_rate

        if total_budget <= 0:
            raise ValueError("Budget must be greater than zero.")

        if duration <= 0:
            raise ValueError("Travel duration must be greater than zero.")

        if exchange_rate <= 0:
            raise ValueError("Exchange rate must be greater than zero.")

    def calculate_daily_budget(self):
        return self.total_budget / self.duration

    def calculate_destination_budget(self):
        return self.total_budget / self.exchange_rate

    def calculate_daily_destination_budget(self):
        return self.calculate_destination_budget() / self.duration

    def calculate_remaining_budget(self, amount_spent):
        if amount_spent < 0:
            raise ValueError("Amount spent cannot be negative.")

        return self.total_budget - amount_spent

    def get_budget_summary(self, amount_spent=0):
        return {
            "Total Budget": self.total_budget,
            "Travel Duration": self.duration,
            "Daily Spending Limit": self.calculate_daily_budget(),
            "Destination Budget": self.calculate_destination_budget(),
            "Daily Destination Limit": self.calculate_daily_destination_budget(),
            "Amount Spent": amount_spent,
            "Remaining Budget": self.calculate_remaining_budget(amount_spent)
        }




        
        
        
        
        


