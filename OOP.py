class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    # Define a repair() method that will update the condition of the podracer to "repaired".
    def repair(self):
        self.condition = "repaired"

# Define a new class, AnakinsPod that inherits the Podracer class.
class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)  # Fixed syntax here

    def boost(self):
        self.max_speed *= 2

# Define another class that inherits Podracer and call this one SebulbasPod.
class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)  # Fixed syntax here

    def flame_jet(self, other):
        other.condition = "trashed"

# '''
# Make sure to answer the following prompts about your coding experience:

# How does this solution demonstrate the four pillars of OOP?
# Encapsulation: Each class (Podracer, AnakinsPod, SebulbasPod) encapsulates its attributes and methods, keeping related data and functionality together.
# Inheritance: AnakinsPod and SebulbasPod inherit from the Podracer class, allowing them to reuse its attributes and methods while adding their own unique features.
# Polymorphism: The flame_jet method in SebulbasPod can act on any instance of Podracer, showcasing how methods can operate on different objects.
# Abstraction: The Podracer class provides a simple interface for managing podracers without exposing the complexity of how each method works.
# Would it have been easier to implement a solution to this problem using a different coding style?
# Using a different coding style, like functional programming, could be easier for simple tasks. However, since we're dealing with distinct types of podracers with shared behaviors, OOP makes it clearer and more organized.

# How in particular did Object Oriented Programming assist in the solving of this problem?
# OOP helped by allowing us to create a structured way to model podracers. We can define shared behaviors in the Podracer class and then extend them in the child classes. This makes the code reusable and easier to maintain, especially as we add more features or types of podracers in the future.