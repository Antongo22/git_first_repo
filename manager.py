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


hourly_rate = 20
bonus_percentage = 10

days_worked = 5

manager = Manager(hourly_rate, bonus_percentage)
earnings = manager.earnings_for_days(days_worked)
taxes = manager.taxes_for_days(days_worked)

print(f"Заработок за {days_worked} дней: ${earnings}")
print(f"Налоги за {days_worked} дней (13%): ${taxes}")
