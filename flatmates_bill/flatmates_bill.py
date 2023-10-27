class Bill:
    """
    Object that has data about a bill(amount,period)
    """

    def __init__(self, amount, period):
        self.period = period
        self.amount = amount


class Flatmate:
    """
    Creates a flatmate person who lives in the flat and will pay.
    """

    def __init__(self, name, days_in_house):
        self.days_in_house = days_in_house
        assert isinstance(name, object)
        self.name = name

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight

        return to_pay


class PdfReport:
    """
    Creates a pdf file with bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass


the_bill = Bill(amount=120, period='March 2021')
john = Flatmate(name='John', days_in_house=20)
marry = Flatmate(name='Marry', days_in_house=25)

print('john has to pay', john.pays(bill=the_bill, flatmate2=marry))
print('marry has to pay', marry.pays(bill=the_bill, flatmate2=john))
