from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request

# initialize flask app
app = Flask(__name__)

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
        self.name = name

    def pays(self, bill, flatmate2):
        """
        method that returns amount of money that has to be paid by user.
        """
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight

        return round(to_pay)


class HomePage(MethodView):
    
    def get(self):
        return render_template('index.html')


class BillFormPage(MethodView):

    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html',
                               billform=bill_form,)


class ResultsPage(MethodView):

    def post(self):
        # getting user input
        bill_form = BillForm(request.form)

        # amount n period
        inputed_amount = float(bill_form.amount.data)
        inputed_period = float(bill_form.period.data)
        # initializing Bill class and passing arguments
        the_bill = Bill(amount=inputed_amount, period=inputed_period)

        # data for first flatmate
        inputed_name1 = bill_form.name1.data
        inputed_days_in_house1 = float(bill_form.days_in_house1.data)
        # initializing Flatmate class and passing arguments for first flatmate
        first_flatmate = Flatmate(name=inputed_name1, days_in_house=inputed_days_in_house1)

        # data for second user
        inputed_name2 = bill_form.name2.data
        inputed_days_in_house2 = float(bill_form.days_in_house2.data)
        # initializing Flatmate class and passing arguments for second flatmate
        second_flatmate = Flatmate(name=inputed_name2, days_in_house=inputed_days_in_house2)

        pay1 = first_flatmate.pays(the_bill, flatmate2=second_flatmate)
        pay2 = second_flatmate.pays(the_bill, flatmate2=first_flatmate)

        return render_template('results.html',
                               name1=inputed_name1, name2=inputed_name2, pay1=pay1, pay2=pay2)






class BillForm(Form):

    # making fields in python instead of HTML
    amount = StringField('Bill Amount: ')
    period = StringField('Bill Period: ')

    # first flatmate
    name1 = StringField('Name: ')
    days_in_house1 = StringField('How many days in house: ')

    # second flatmate
    name2 = StringField('Name: ')
    days_in_house2 = StringField('How many days in house: ')

    # adding button for submit info
    calculate_button = SubmitField('Calculate')


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill_form', view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule('/results', view_func=ResultsPage.as_view('results_page'))

app.run(debug=True)
