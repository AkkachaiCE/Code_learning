import itertools
import random
import copy


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        # Only one case that number of cells == count of mines
        if len(self.cells) == self.count and self.count != 0:
            return self.cells
        else:
            return set()
        # raise NotImplementedError

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        # Only one case that safe for sure is no count of mines
        if self.count == 0:
            return self.cells
        else:
            return set()
        # raise NotImplementedError

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        if cell in self.cells:
            self.cells.remove(cell)
            # decrease the amount of remainding mines
            self.count -= 1
        # raise NotImplementedError

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        if cell in self.cells:
            # remove the safe cell only
            self.cells.remove(cell)
        # raise NotImplementedError


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        # Step 1
        self.moves_made.add(cell)

        # Setp 2
        self.mark_safe(cell)

        # Step 3
        # new cell for collecting before add to new knowledge
        new_cells = set()
        countm = 0
        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue
                if (i, j) in self.mines:
                    countm += 1
                if (i, j) in self.safes:
                    continue

                # Update to new_cells before add to Sentence then knowlwdge
                if 0 <= i < self.height and 0 <= j < self.width and (i, j) not in self.safes and (i, j) not in self.mines:
                    new_cells.add((i, j))

        # if len(new_cells) != 0:
        self.knowledge.append(Sentence(new_cells, count - countm))

        # Step 4
        # Check evey knowledge
        for sentence in self.knowledge:
            # Access to known_safes for using check
            cell_safes = sentence.known_safes()
            # loop through every copy cell
            if cell_safes:
                for cell in cell_safes.copy():
                    # if cell not in self.safes:
                    self.mark_safe(cell)

           # Access to known_mines for using check
            cell_mines = sentence.known_mines()
            # loop through every copy cell
            if cell_mines:
                for cell in cell_mines.copy():
                    # if cell not in self.mines:
                    self.mark_mine(cell)

        # Step 5
        # Loop through 2 sentences in self.knowledge for infer new sentence
        knowledge_copy = copy.deepcopy(self.knowledge)
        for sentenceA in knowledge_copy:
            for sentenceB in knowledge_copy:
                if sentenceA == sentenceB:
                    continue
                if len(sentenceA.cells) == 0 or len(sentenceB.cells) == 0:
                    continue
                if sentenceA.cells.issubset(sentenceB.cells):
                    new_cells = sentenceB.cells - sentenceA.cells
                    new_count = sentenceB.count - sentenceA.count
                    sentence = Sentence(new_cells, new_count)
                    if sentence not in self.knowledge:
                        self.knowledge.append(sentence)
                """
                if sentenceB.cells.issubset(sentenceA.cells):
                    new_cells = sentenceA.cells - sentenceB.cells
                    new_count = sentenceA.count - sentenceB.count
                    sentence = Sentence(new_cells, new_count)
                    if sentence not in self.knowledge:
                        self.knowledge.append(sentence)
                """
        # raise NotImplementedError

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        for cell in self.safes:
            if cell not in self.moves_made:
                return cell
        return None

        # raise NotImplementedError

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        all_cells = set(itertools.product(range(self.height), range(self.width)))
        available_cells = all_cells - self.moves_made - self.mines
        return random.choice(list(available_cells))

        # raise NotImplementedError
