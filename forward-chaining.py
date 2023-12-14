# Initialize empty lists to store rules and facts
rules = []
facts = []


# Function to add a new fact to the facts list
def add_facts(fact):
    if fact not in facts:
        facts.append(fact)
        print("\nInput has been added to facts.")

    else:
        print("\nInput is already in facts. Please input a new fact.") 


# Function to add a new rule to the rules list
def add_rules(rule):
    if rule not in rules:
        rules.append(rule)
        print("Input has been added to rules.")

    else:
        print("Input already exist in rules. Please input a new rule.")


# Function to display the current knowledge base
def display_knowledge_base():
    print("\n################## KNOWLEDGE BASE ##################\n")
    print("Current facts: ", *facts, sep="\n")
    print("\n\nCurrent rules: ", *rules, sep="\n")
    print("\n\n####################################################\n")


# Function to generate new facts based on rules and existing facts
def generate_new_facts():

    # Initialize a flag to track whether a new fact has been added during this iteration
    new_fact_added = True

    # Continue this loop until no new facts can be added in an iteration
    while new_fact_added:
        new_fact_added = False

        # Iterate through each rule in the 'rules' list and
        # split the rule into its antecedent and consequent parts
        # then extract the conditions
        for rule in rules:
            antecedent, consequent = rule.split(", then ")
            conditions = antecedent[3:].split(" and ")

            # Check if all conditions are met based on the current facts
            if all(condition in facts for condition in conditions):
                new_fact = consequent

                # Check if the new fact is not already in the 'facts' list
                if new_fact not in facts:
                    facts.append(new_fact)
                    new_fact_added = True


# Function to display user options
def display_options():
    print("\n[1] Add fact\n"
          "[2] Add rule\n"
          "[3] Generate new facts\n"
          "[4] Delete current facts\n"
          "[5] Delete current rules\n"
          "[6] Exit program\n")
    print("----------------------------------")


def main():
    while True:

        display_knowledge_base()

        print("What would you like to do?")
        display_options()

        user_choice = input("\nEnter your choice: ")

        if user_choice == '1':
            new_fact = input(
                "Enter a new fact: ").lower()
            add_facts(new_fact)

        elif user_choice == '2':
            new_rule = input(
                "Enter a new rule: ").lower()
            add_rules(new_rule)

        elif user_choice == '3':
            generate_new_facts()

        elif user_choice == '4':
            facts.clear()

        elif user_choice == '5':
            rules.clear()

        elif user_choice == '6':
            break


if __name__ == "__main__":
    main()
