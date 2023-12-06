import os.path
import webbrowser

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
        # add image
        pdf.image(name='house.png', w=30, h=30)
        # Insert Title
        pdf.set_font(family='Times', style='B', size=24)
        pdf.cell(w=0, h=80, txt='Flatmates Bill', align='C', border=0, ln=1)
        pdf.set_font(family='Times', style='B', size=16)
        pdf.cell(w=100, h=40, txt='Period:', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert name of 1st user and amount to pay
        pdf.set_font(family='Times', style='I', size=16)
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=40, txt=str(round(flatmate1.pays(bill=bill, flatmate2=flatmate2), 2)), border=0, ln=1)

        # Insert name of 2nd user and amount to pay
        pdf.set_font(family='Times', style='I', size=16)
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=40, txt=str(round(flatmate2.pays(bill=bill, flatmate2=flatmate1), 2)), border=0, ln=1)


        pdf.output(name=self.filename)
        webbrowser.open_new_tab('file://'+ os.path.realpath(self.filename))
ask_the_bill = float(input('Hey, what is total amount ?: '))
ask_the_period = input('What was the datum?: ')
first_user = input(f'What is name of first user?: ')
first_period = int(input('How long has he been living there?: '))
second_user = input('What is name of second user?: ')
second_period = int(input('How long has he been living there?: '))


the_bill = Bill(amount=ask_the_bill, period=ask_the_period)
first_flatmate = Flatmate(name=first_user, days_in_house=first_period)
second_flatmate = Flatmate(name=second_user, days_in_house=second_period)

print(f'{first_flatmate.name} has to pay', first_flatmate.pays(bill=the_bill, flatmate2=second_flatmate))
print(f'{second_flatmate.name} has to pay', second_flatmate.pays(bill=the_bill, flatmate2=first_flatmate))
pdf_report = PdfReport(filename='report1.pdf')
pdf_report.generate(flatmate1=first_flatmate, flatmate2=second_flatmate, bill=the_bill)
