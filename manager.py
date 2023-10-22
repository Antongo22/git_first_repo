class Manager:
    def __init__(self, hourly_rate, bonus_percentage):
        self.hourly_rate = hourly_rate
        self.bonus_percentage = bonus_percentage

    def earnings_for_days(self, days):
        daily_earnings = (self.hourly_rate * 8) * (1 + self.bonus_percentage / 100)
        total_earnings = daily_earnings * days
        return total_earnings

    def taxes_for_days(self, days):
        earnings_without_bonus = (self.hourly_rate * 8) * days
        tax_rate = 0.13
        taxes = earnings_without_bonus * tax_rate
        return taxes
