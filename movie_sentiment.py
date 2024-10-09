"""
Module: movie_sentiment

Program to analyze movie reviews and predict the sentiment of new reviews.

Authors:
1) Sawyer Dentz - sdentz@sandiego.edu
2) Matthew Oderlin - moderlin@sandiego.edu
"""

def average_review(word, review_filename):
    """
    finds the average score of a review containing the word

    Parameters:
    word (type: string): The word to look for in the reviews.
    review_filename (type: string): The review file that the word is looked for in

    Returns:
    (type: float) the average score of the reviews containing the word
    """

    review_file = open(review_filename, 'r')

    sum = 0
    lines = 0

    for line in review_file:
        # make lower case to avoid case sensitivity
        lower_line = line.lower()  
        lower_word = word.lower()

        vals = lower_line.split()
        review = int(vals[0])
        vals = vals[1:]
    
        if lower_word in vals:
            sum += review
            lines += 1
        if lines == 0:
            return 2


    # done reading file, so close it
    review_file.close()

    average_score = sum / lines

    return average_score


def estimate_review_score(movie_review, review_filename):
    """
    estimates the score of a review based on average scores of the words in the review

    Parameters:
    movie_review (type: string): the review that will be scored
    review_filename (type: string): the file that will be used to calculate average scores of words

    Returns:
    (type: float): the estimated score of the review
    """
    total = 0
    words = movie_review.split()
    for word in words:
        total += average_review(word, review_filename)

    return (total / len(words))



def estimate_user_review():
    """
    Asks user to enter a movie review, then the name of a file with existing
    movie reviews.
    It then calculates the estimated rating of the review they entered, along
    with a description of that rating (e.g. "neutral" or "slightly positive").
    """

    review = input("Enter a movie review: ")

    new_review = ""
    for ch in review:
        if ch not in [".", ",", "!", "-"]:
            new_review += ch
    review = new_review
    print(review)

    file = input("Enter the name of the file containing reviews: ")
    score = estimate_review_score(review, file)

    if round(score) == 0:
        sentiment = "negative"
    elif round(score) == 1:
        sentiment = "somewhat negative"
    elif round(score) == 2:
        sentiment = "neutral"
    elif round(score) == 3:
        sentiment = "somewhat positive"
    elif round(score == 4):
        sentiment = "positive"

    print("Estimated score:", str(score) + " (" + sentiment + ")")


# Do not modify anything after this point.
if __name__ == "__main__":
    estimate_user_review()
