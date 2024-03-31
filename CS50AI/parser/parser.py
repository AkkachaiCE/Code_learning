import nltk
import sys

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> NP VP | S Conj S
NP -> Det N | Det N PP | Det AdjP N | N | AdjP N | Adj N PP | N PP | Det AdjP N PP
AdjP -> Adj | Adj AdjP
VP -> V | V NP | V PP | Adv VP | VP Adv | V NP PP | VP Conj VP
PP -> P NP
AP -> Adj | Adv Adj | Adj AP | Adv Adj AP
AdvP -> Adv | Adv Adv | Adv AdvP
"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    # Create words list to store the word
    words_list = []
    # Convert every word to lowercase
    sentence = sentence.lower()
    # Set the token
    tokens = nltk.word_tokenize(sentence)
    # Loop to every word in sentence then check whether is alphabetic
    for word in tokens:
        if word.isalpha():
            words_list.append(word)

    return words_list
    # raise NotImplementedError


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    # Create the NP list
    NP_list = []
    # Loop to every label in subtrees
    for subtree in tree.subtrees():
        # Check the label "NP"
        if subtree.label() == "NP" and not Np_Sub(subtree):
            # Add to the NP_list
            NP_list.append(subtree)
    return NP_list

# Defind help functin to check NP in other NP


def Np_Sub(tree):
    for subtree in tree.subtrees():
        if subtree != tree and subtree.label() == "NP":
            return True
    return False
    # raise NotImplementedError


if __name__ == "__main__":
    main()
