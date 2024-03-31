import sys

from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        _, _, w, h = draw.textbbox((0, 0), letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        # Loop to every variables
        # Check node-consistent
        # If consistent
        # Update
        # If not consisten
        # Remove by self.domains[v].remove(x)
        for v in self.domains:
            for x in self.domains[v].copy():
                if len(x) == v.length:
                    pass
                else:
                    self.domains[v].remove(x)

        # raise NotImplementedError

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        # Initial boolean variable
        revision = False
        # Compute overlap (None, if the two variables do not overlap)
        overlap = self.crossword.overlaps[x, y]
        # Check overlap variable is not None
        if overlap is not None:
            i, j = overlap
            # Loop to x (copy version because will be remove later in case not consistent)
            for _x in self.domains[x].copy():
                # Initial consist
                consist = False
                # Loop to y
                for _y in self.domains[y]:
                    # Check consist
                    if _x[i] == _y[j]:
                        # Update consist
                        consist = True
                        break
                # In case consist = False
                if consist == False:
                    self.domains[x].remove(_x)
                    # Update the revision
                    revision = True

        return revision

        # raise NotImplementedError

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        # Check the arcs is None (Initial state)
        if arcs is None:
            # Initial the arcs variable
            arcs = []
            for i in self.domains:
                for j in self.domains:
                    if i != j:
                        # append value to the arcs list
                        arcs.append((i, j))
        # Not initial state
        else:
            pass
        # Loop to arcs then pop() the value out until empty
        while arcs:
            # Pop value then assign to variable
            variable_i, variable_j = arcs.pop()
            # Check revise
            if self.revise(variable_i, variable_j):
                # Return False, if domains is empty
                if not self.domains[variable_i]:
                    return False
                # Add variable to the list for each neighbor
                for variable_k in self.crossword.neighbors(variable_i) - {variable_j}:
                    arcs.append((variable_k, variable_i))
        return True

        # raise NotImplementedError

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        # Check whether each value is in assignment
        for _ in self.domains:
            if _ not in assignment:
                return False
        return True

        # raise NotImplementedError

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        # Loop to every item in the assignment dictionatry
        for variable, word in assignment.items():
            # Check the length
            if variable.length != len(word):
                return False

            # Check conflicts
            for neighbor in self.crossword.neighbors(variable):
                if neighbor in assignment.keys():
                    x, y = self.crossword.overlaps[variable, neighbor]
                    if neighbor in assignment:
                        if word[x] != assignment[neighbor][y]:
                            return False

        # Check the distinct value
        if len(set(assignment.values())) != len(assignment):
            return False

        return True
        # raise NotImplementedError

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        # Create empty dictionary
        word_dict = {}
        # get the neighbor from crossword.neighbor
        neighbors = self.crossword.neighbors(var)
        # Loop to every domains via var
        for _ in self.domains[var]:
            # Check the word is in assignment
            if _ not in assignment:
                counter = 0
                # Check in Neighbors
                for neighbor in neighbors:
                    if _ in self.domains[neighbor]:
                        counter += 1
                # Update the word_dict value
                word_dict[_] = counter

        # Sorted the dict before return
        return sorted(word_dict, key=lambda key: word_dict[key])
        # return sorted_dict
        # raise NotImplementedError

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """

        # Create unassign dict
        unassign_dict = {}
        # Loop to every variable in self.domains
        for _ in self.domains:
            if _ not in assignment:
                unassign_dict[_] = self.domains[_]

        # Choose the minimum number to return
        # Get the list from dictionary
        items = unassign_dict.items()
        # Sorted the items
        sorted_items = sorted(items, key=lambda item: len(item[1]))
        # Sorted the keys
        sorted_keys = []
        for key, value in sorted_items:
            sorted_keys.append(key)

        return sorted_keys[0]
        # raise NotImplementedError

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        # Check the assignment, if complete then return assignment
        if self.assignment_complete(assignment):
            return assignment
        # If not complete
        # Try a new variable
        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var, assignment):
            new_assignment = assignment.copy()
            new_assignment[var] = value
            if self.consistent(new_assignment):
                result = self.backtrack(new_assignment)
                if result is not None:
                    return result
        return None
        # raise NotImplementedError


def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
