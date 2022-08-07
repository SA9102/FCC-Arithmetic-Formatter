def arithmetic_arranger(problems, answer=False):
    # Check if there are more than five problems
    if len(problems) > 5:
        return "Error: Too many problems."

    # Each problem is stored in its own list, which itself is
    # split, separating the operands and operators from each other
    opds_and_opts = [problem.split(" ") for problem in problems]

    first_row = "" # first operands
    second_row = "" # operators and second operands
    third_row = "" # dashed lines
    if answer == True:
        fourth_row = "" # answers

    # Stores the lengths of each vertical problem. This is needed
    # in order to calculate the number of hyphens, and also to
    # calculate the whitespace if displaying the answer.
    lengths = list()

    # Keeps track of the current problem.
    problem_index = 0

    for problem in opds_and_opts:

    # Check if both operands are integers.
        try:
          int(problem[0])
          int(problem[2])
        except:
          return "Error: Numbers must only contain digits."

        # Check if the operator is either a "+" or "-".
        if problem[1] != "+" and problem[1] != "-":
          return "Error: Operator must be '+' or '-'."

        # Check if each operand has four digits or less.
        if len(problem[0]) > 4 or len(problem[2]) > 4:
          return "Error: Numbers cannot be more than four digits."

        # Check if the first operand has more digits than the second.
        if len(problem[0]) > len(problem[2]):
          # This is the current piece for the first row.
          # Create a string that will first have two whitespaces
          # (because of the operator and single space), and then
          # concatenate the first operand. This is stored in its
          # own string so that we can get the length of this string
          # (which is the length of the current problem). It is also
          # possible to get the length from the current piece of the
          # second row.
          piece_to_get_length = "  " + problem[0]
          # Concatenate this to the entire row of the first operands.
          first_row += piece_to_get_length
          # Store this length.
          lengths.append(len(piece_to_get_length))

          # This is the current piece for the second row.
          # Create a string that contains the operator, then a single
          # space, then some whitespaces, the number of which is
          # determined by subtracting the number of digits of the second
          # operand from the first. Then, concatenate the second operand.
          # Finally concatenate this to the entire row of the second
          # operands.
          second_row += problem[1] + " " + (" " * (len(problem[0]) - len(problem[2]))) + problem[2]

        # Check if the second operand has more digits than the first.
        elif len(problem[0]) < len(problem[2]):
          piece_to_get_length = "  " + (" " * (len(problem[2]) - len(problem[0]))) + problem[0]
          first_row += piece_to_get_length
          lengths.append(len(piece_to_get_length))

          second_row += problem[1] + " " + problem[2]

        # Check if both operands have equal number of digits.
        elif len(problem[0]) == len(problem[2]):
          piece_to_get_length = "  " + problem[0]
          first_row += piece_to_get_length
          lengths.append(len(piece_to_get_length))

          second_row += problem[1] + " " + problem[2]

        # Retrieve the number of hyphens for the current problem
        # by retrieving its length, then concatenate this to the
        # entire row of hyphens.
        third_row += ("-" * lengths[problem_index])

        # If the user wants the answers displayed
        if answer == True:
          # Check the operator to perform the appropriate calculation
          if problem[1] == "+":
            result = str(int(problem[0]) + int(problem[2]))
          elif problem[1] == "-":
            result = str(int(problem[0]) - int(problem[2]))

          # Calculate the whitespace for the answer by subtracting
          # the number of digits of the result from the length of the
          # problem.
          whitespaces = lengths[problem_index] - len(result)
          
          # Concatenate the answer to the entire row of answers.
          fourth_row += (" " * whitespaces) + result

        # Increment the problem number by one.
        problem_index += 1

        # Check if the program has not reached the last problem
        if problem_index < len(problems):
          # Add the four whitespaces after each row.
          first_row += "    "
          second_row += "    "
          third_row += "    "
          if answer == True:
            fourth_row += "    "

    # This variable contains the problems stored in the vertical format
    arranged_problems = first_row + "\n" + second_row + "\n" + third_row + ("\n" + fourth_row if answer == True else "")

    return arranged_problems



# EXAMPLES:

#print(arithmetic_arranger(['3801 - 2', '123 + 49']))
#print(arithmetic_arranger(['1 + 2', '1 - 9380']))
#print(arithmetic_arranger(['3 + 855', '3801 - 2', '45 + 43', '123 + 49']))
#print(arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']))
#print(arithmetic_arranger(['44 + 815', '909 - 2', '45 + 43', '123 + 49', '888 + 40', '653 + 87'])) # Will raise an exception
#print(arithmetic_arranger(['3 / 855', '3801 - 2', '45 + 43', '123 + 49'])) # Will raise an exception
#print(arithmetic_arranger(['24 + 85215', '3801 - 2', '45 + 43', '123 + 49'])) # Will raise an exception
#print(arithmetic_arranger(['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49'])) # Will raise an exception
#print(arithmetic_arranger(['3 + 855', '988 + 40'], True))
#print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))
