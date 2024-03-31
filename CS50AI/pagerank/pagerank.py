import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    # Dictionaty output with probabilities value
    output = {}

    # Calculate total pages and total links
    total_pages = len(corpus)
    total_links = len(corpus[page])

    # Add the key to dict output and initial probabiliities
    # If in the current page + additional probabilities
    for _ in corpus:
        if _ in corpus[page]:
            output[_] = round(((1 - damping_factor) / total_pages) + (damping_factor / total_links), 3)
        else:
            output[_] = round((1 - damping_factor) / total_pages, 3)
    return output

    # raise NotImplementedError


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # Dictionary Output
    output = {}

    # Initialize the first random
    first_page = random.choice(list(corpus.keys()))
    output[first_page] = 1
    generate_out = transition_model(corpus, first_page, damping_factor)

    # Generate sample with n samples via transition_model
    for _ in range(n - 1):
        page = random.choices(list(generate_out.keys()), list(generate_out.values()))[0]
        if page not in output:
            output[page] = 1
        else:
            output[page] += 1
        generate_out = transition_model(corpus, page, damping_factor)

    # Devide every accumulative value by n before return
    for _ in sorted(output):
        output[_] /= n
    return output

    # raise NotImplementedError


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    # Dictionary Ouput
    output = {}

    # total number of pages in the corpus
    N = len(corpus)

    # damping factor
    d = damping_factor

    # initial the page rank
    for _ in corpus:
        output[_] = 1 / N

    # Converge Status
    Con_status = True
    # Iteration loop until converge
    while Con_status:
        new_output = {}
        for _ in output:
            Sum_rank = 0

            for page in corpus:
                # With link
                if _ in corpus[page]:
                    Sum_rank += output[page] / len(corpus[page])
                # Without link
                if not corpus[page]:
                    Sum_rank += output[page] / N
            new_output[_] = ((1 - d) / N) + d * Sum_rank

        # Complete all output
        Con_status = False

        for check in output:
            # If find just one page that not converge loop again
            if abs(output[check] - new_output[check]) > 0.001:
                Con_status = True

            output[check] = new_output[check]

    return output
    # raise NotImplementedError


if __name__ == "__main__":
    main()
