def calculate_gnp_gdp():
    # Insert components to list
    components = ['GNP/GDP', 'C', 'G', 'I', 'X', 'M']
    # Join all components with a newline character
    prompt_options = '\n'.join(components)
    # Asks the user which component should be calculated
    component_to_calculate = input(f"Which component would you like to calculate?\n{prompt_options}\nYour Choice? ")
    component_to_calculate = component_to_calculate.upper()  # Convert user input to uppercase letters to avoid errors

    # Check if user selection is one of the options
    if component_to_calculate not in ['GNP/GDP', 'C', 'G', 'I', 'X', 'M', 'GNP', 'GDP']:
        print("Your choice is incorrect")
        return  # Exit the function if the input is not valid

    # Initialize an empty dictionary to store the values of the variables
    values = {}
    # Checking if user selection is one of the options
    gn = ['GNP', 'GDP']
    if component_to_calculate in gn:
        gn = component_to_calculate
        components.pop(0)  # Remove GNP/GDP from the list
        components.append(gn)  # Add user selection to the list

    for component in components:
        # Removes the user's selection from the list
        if component != component_to_calculate:
            # Request a value from the user for each component
            value = float(input(f"Enter value for {component}: "))  # Convert the input from the user to float var
            values[component] = value  # Saving the value in the dictionary under the key of the component name

    # Calculate the value for the selected component
    if component_to_calculate in gn:
        result = values['C'] + values['G'] + values['I'] + values['X'] - values['M']
    elif component_to_calculate == 'C':
        result = values['GNP/GDP'] - (values['G'] + values['I'] + values['X'] - values['M'])
    elif component_to_calculate == 'G':
        result = values['GNP/GDP'] - (values['C'] + values['I'] + values['X'] - values['M'])
    elif component_to_calculate == 'I':
        result = values['GNP/GDP'] - (values['C'] + values['G'] + values['X'] - values['M'])
    elif component_to_calculate == 'X':
        result = values['GNP/GDP'] - (values['C'] + values['G'] + values['I'] - values['M'])
    elif component_to_calculate == 'M':
        result = -values['GNP/GDP'] + (values['C'] + values['G'] + values['I'] + values['X'])

    print(f"The value of {component_to_calculate} is {result}")

calculate_gnp_gdp()