from csv import DictReader

class TransactionAnalyzer:

    def __init__(self):
        
        fr = open("14. OOPS\\bankanalyzer\\bank_transactions_500_records.csv")

        self.transactions = list(DictReader(fr))
        print(len(self.transactions),"records found")


    def debit_transactions(self):

        for t in self.transactions:# t = {id:,name:,type:,amount}

            if t.get("type") == "debit":

                print(t)

    def credit_transactions(self):

        for t in self.transactions:

            if t.get("type") == "credit":

                print(t)

    def high_value_transactions(self): # amount > 75000
        
        for t in self.transactions:

            if int(t.get("amount")) > 75000:

                print(t)

         
    def high_debit_transactions(self): 

        # self.debits = [t for t in self.transactions if t.get("type") == "debit"]

        # self.sorted_debits =  sorted(self.debits, key=lambda x:int(x["amount"]),reverse=True)

        # print(self.sorted_debits[0])

        debits = [t for t in self.transactions if t.get("type") == "debit"]

        max_amt = max(int(t.get("amount")) for t in debits)

        for t in debits:
            if int(t.get("amount")) == max_amt:
                print(t)


    def high_credit_transactions(self): 

        self.credits = [t for t in self.transactions if t.get("type") == "credit"]

        self.sorted_credits = sorted(self.credits,key=lambda x:int(x["amount"]),reverse=True)

        print(self.sorted_credits)

analysis = TransactionAnalyzer()
# analysis.debit_transactions()
# analysis.credit_transactions()
analysis.high_value_transactions()
# analysis.high_debit_transactions()
# analysis.high_credit_transactions()


