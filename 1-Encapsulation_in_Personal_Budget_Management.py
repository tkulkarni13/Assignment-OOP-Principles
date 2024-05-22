# Task 1: Define Budget Category Class

# BudgetCategory class allows for creation of a budget category to track expenses in a specific area.
class BudgetCategory:
    # Constructor
    def __init__(self, category, budget):
        self.__category = category # Keeps track of name of category
        self.__budget = budget # Keeps track of remaining budget
        self.__original_budget = budget # Keeps track of original allocated budget

    # Task 2: Implement Getters and Setters

    def get_category(self):
        return self.__category
    
    def set_category(self, new_category):
        self.__category = new_category

    def get_budget(self):
        return self.__budget
    
    def set_budget(self, new_budget):
        self.__budget = new_budget
    
    def get_original_budget(self):
        return self.__original_budget
    
    def set_original_budget(self, new_budget):
        self.__original_budget = new_budget
    
    # Task 3: Add Budget Functionality

    # Function to add an expense. Will subtract expense from budget if input value is within the remaining budget
    def add_expense(self, amount):
        if (amount > self.get_budget()):
            # Notify user if they attempt to make an expense that is too large
            print(f"The expense of ${amount} is greater than the remaining budget.")
        else:
            new_budget = self.get_budget() - amount
            self.set_budget(new_budget)
    
    # Task 4: Display Budget Details

    def display_category_summary(self):
        # Display all budget information for user
        print(f"Category: {self.get_category()} - Allocated Budget: ${self.get_original_budget()} - Remaining Budget: ${self.get_budget()}")

#Testing
food_category = BudgetCategory("Food", 500)
food_category.display_category_summary()
food_category.add_expense(170)
food_category.display_category_summary()
food_category.add_expense(450)