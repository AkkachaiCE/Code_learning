import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    # Read data in from file
    with open(filename) as file:
        reader = csv.reader(file)
        next(reader)

        # Create the list variable to store the data then will be convert to tuple before return
        data = []
        # Loop to append the data
        for row in reader:
            data.append({
                "evidence": [int(i) for i in [row[0]]] +
                            [float(i) for i in [row[1]]] +
                            [int(i) for i in [row[2]]] +
                            [float(i) for i in [row[3]]] +
                            [int(i) for i in [row[4]]] +
                            [float(i) for i in [row[5]]] +
                            [float(i) for i in [row[6]]] +
                            [float(i) for i in [row[7]]] +
                            [float(i) for i in [row[8]]] +
                            [float(i) for i in [row[9]]] +
                            [0 if row[10] == "Jan" else 1 if row[10] == "Feb" else 2 if row[10] == "Mar" else 3 if row[10] == "Apr" else 4 if row[10] == "May" else 5 if row[10] == "Jun" else 6 if row[10] == "Jul" else 7 if row[10] == "Aug" else 8 if row[10] == "Sep" else 9 if row[10] == "Oct" else 10 if row[10] == "Nov" else 11] +
                            [int(i) for i in [row[11]]] +
                            [int(i) for i in [row[12]]] +
                            [int(i) for i in [row[13]]] +
                            [int(i) for i in [row[14]]] +
                            [int(0) if row[15] == "New_Visitor" else int(1)] +
                            [int(0) if row[16] == "FALSE" else int(1)],
                "label": 1 if row[17] == "TRUE" else 0
            })
        # Separate data into training and testing groups
        evidence = [row["evidence"] for row in data]
        labels = [row["label"] for row in data]

        return (evidence, labels)

    # raise NotImplementedError


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    # Choose the model
    model = KNeighborsClassifier(n_neighbors=1)

    # Fit model
    trained_model = model.fit(evidence, labels)

    return trained_model
    # raise NotImplementedError


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    sensitivity = 0
    positive = 0
    specificity = 0
    negative = 0
    # Loop to every labels
    for i in range(len(labels)):
        # Check for positive
        if labels[i] == 1:
            if labels[i] == predictions[i]:
                sensitivity += 1
            positive += 1
        # For negative
        else:
            if labels[i] == predictions[i]:
                specificity += 1
            negative += 1
    # return tuple of them
    return (sensitivity/positive, specificity/negative)

    # raise NotImplementedError


if __name__ == "__main__":
    main()
