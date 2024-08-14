 

"""
3.2PP Fill in the Blanks: Paris Olympics
"""

__author__ = "Najmul Uddin"

def main():
    # Display the title of the program
    print("Paris 2024 Medal Tally ")
    print()

    #  Display for and read the required details from the user
    first_place: str = input("Enter the name of the country in first place:")
    capital_city: str = input(f"Enter the capital City of  {first_place}: ")
    second_place: str = input("Enter the name of the Country in second place: ")
    gold_medals_1: int = int(input(f"How many gold medals has {first_place} won? "))
    gold_medals_2: int = int(input(f"How many gold medals has {second_place} won? "))

    # Calculate the margin between the gold medal counts
    margin: int = gold_medals_1 - gold_medals_2

    # Display the  output
    print(f"\n{first_place} currently tops the 2024 Paris Olympics' medal tally with {gold_medals_1} gold.")
    print(f"Citizens of {capital_city} are overjoyed at beating arch-rivals {second_place}.")
    print(f"Their lead of {margin} gold looks secure with only competitive programming left.")

if __name__ == "__main__":
    main()
