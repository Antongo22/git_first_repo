class Employee:
    def __init__(self, hourly_rate):
        self.hourly_rate = hourly_rate

    def earnings_for_days(self, days):
        daily_earnings = 8 * self.hourly_rate
        total_earnings = daily_earnings * days
        return total_earnings

    def taxes_for_days(self, days):
        earnings = self.earnings_for_days(days)
        tax_rate = 0.13
        taxes = earnings * tax_rate
        return taxes