from collections import defaultdict
class SplitwiseApplication:

    def __init__(self) -> None:
        self.user_balances = defaultdict(defaultdict)

    def add_user(self,username):
        self.user_balances[username] = defaultdict()

    def get_all_balances(self):
        for username in self.user_balances:
            self.get_user_balance(username)

        
    def get_user_balance(self,username):
        user_balance = self.user_balances[username]

        if not (user_balance):
            print(f"{username} owes 0")

        for owed_user in user_balance:
            amount_owed = user_balance[owed_user]
            print(f"{username} owes {owed_user} {amount_owed}")
    
    def calculate_equal_split(self,amount_paid,number_users_involved):
        return amount_paid / float(number_users_involved)

    def calculate_percent_split(self,amount_paid, split):
        return amount_paid * 0.01 * split
    
    def add_balance_to_user(self,spent_user,paid_user,amount_owed):
        current_user_balance = self.user_balances[spent_user]
        if paid_user in current_user_balance:
            current_user_balance[paid_user] += amount_owed
        else:
            current_user_balance[paid_user] = amount_owed


    def add_expense(self,expense_string):
        expense_string_split = expense_string.split()
        paid_user = expense_string_split[0]
        amount_paid = float(expense_string_split[1])
        number_users_involved = int(expense_string_split[2])
        users_involved = expense_string_split[3:3 + number_users_involved]
        expense_type = expense_string_split[3 + number_users_involved]
        splits = expense_string_split[4 + number_users_involved:]
        if len(splits) > 2:
            splits = [float(x) for x in splits]

        if expense_type == "EQUAL":
            for user in users_involved:
                if user == paid_user:
                    continue
                amount_owed = self.calculate_equal_split(amount_paid,number_users_involved)
                self.add_balance_to_user(user,paid_user,amount_owed)
        
        elif expense_type == "PERCENT":
            if sum(splits) != 100.0:
                print("Invalid Split")
                return 

            for index, user in enumerate(users_involved):
                if user == paid_user:
                    continue
                amount_owed = self.calculate_percent_split(amount_paid,splits[index])
                self.add_balance_to_user(user,paid_user,amount_owed)
        
        
                
if __name__ == '__main__':
    app = SplitwiseApplication()
    app.add_user('u1')
    app.add_user('u2')
    app.add_user('u3')
    app.add_user('u4')
    # app.get_all_balances()
    app.add_expense("u1 1000 4 u1 u2 u3 u4 EQUAL")
    # app.get_all_balances()
    app.add_expense("u2 1000 4 u1 u2 u3 u4 PERCENT 30 20 20 30")
    app.get_all_balances()
