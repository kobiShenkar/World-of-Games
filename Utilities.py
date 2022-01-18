# this line is to create conflict from master
def is_valid_input(input_str):
    while True:
        try:
            input_var = int(input(input_str))
            return input_var
        except ValueError:
            print("That's not a valid option!")
            continue


def is_valid_range(min_num, max_num, input_str):
    input_number = is_valid_input(input_str)
    if min_num < input_number <= max_num:
        return input_number
    else:
        print('That\'s not an option!')
        return is_valid_range(min_num, max_num, input_str)


def test_variables(variables):
    output = "-------Tests--------\n"
    for variable in variables:
        output += f"{variable} = {variables[variable]}\n"
    output += "-------Tests--------"
    return print(output)

