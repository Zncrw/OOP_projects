from fpdf import FPDF
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

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()
        # Insert text
        pdf.set_font(family='Times', style='B', size=24)
        # Title
        pdf.cell(w=0, h=80, txt='Flatmates Bill', align='C', border=1, ln=1)
        # text in cells
        pdf.cell(w=100, h=40, txt='Period:', border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)
        # Insert name of 1st user and amount to pay
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=150, h=40, txt=str(flatmate1.pays(bill=bill, flatmate2=flatmate2)), border=1, ln=1)

        pdf.output(name=self.filename)


the_bill = Bill(amount=120, period='July 2023')
john = Flatmate(name='John', days_in_house=20)
marry = Flatmate(name='Marry', days_in_house=25)

print('john has to pay', john.pays(bill=the_bill, flatmate2=marry))
print('marry has to pay', marry.pays(bill=the_bill, flatmate2=john))
pdf_report = PdfReport(filename='report1.pdf')
pdf_report.generate(flatmate1=john, flatmate2=marry, bill=the_bill)
