'''1. Product Review Analysis

Task 1: Keyword Highlighter 
Write a program that searches through reviews list and looks for 
keywords such as "good", "excellent", "bad", "poor", and "average". 
We want you to capitalize those keywords then print out each review. 
Print out each review with the keywords in uppercase so they stand out.
So for the first string in the reviews list, we want it to say: "This product is really GOOD. I'm impressed with its quality."

'''

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."]
    

keywords =  ["good", "excellent", "bad", "Poor", "average"]
for review in reviews:
    for keyword in keywords:
        review = review.replace(keyword, keyword.upper())
    print(review)

'''
Task 2: Sentiment Tally

Develop a function that tallies the number of positive and negative words in each review. 
The function should return the total count of positive and negative words

'''
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def  sentiment_tally(reviews, positive_words, negative_words):
    tallies = []
    for review in reviews:
        review_words = review.lower().split()
        for iteration in range(len(review_words)):
            review_words[iteration] = review_words[iteration].strip('.,!?"\'')
        positive_count = sum(1 for word in review_words if word in positive_words)
        negative_count = sum(1 for word in review_words if word in negative_words)
        tallies.append([positive_count, negative_count])
    return tallies

tallies = sentiment_tally(reviews, positive_words, negative_words)
for i, [positive_count, negative_count] in enumerate(tallies):
    print(f"Review {i+1}: Positive words = {positive_count}, Negative words = {negative_count}")

'''
Task 3: Review Summary

Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. 
Ensure that the summary does not cut off in the middle of a word.
'''
print("\n============================================")
counter = 0
new_list = []
modified_review = ""
for review in reviews:
    review_words = review.lower().split(" ")
    for word in review_words:
        counter += len(word) + 1
        modified_review +=  word + " "
        if counter >= 30:
            new_list.append(modified_review[0:-1] + "...")
            modified_review = ""
            counter = 0
            break
    
for item in new_list:
    print(item)
print("============================================\n")
print(new_list)

'''
2. User Input Data Processor

Task 1: Input Length Validator Write a script that asks for and checks the length of the user's first name and last name. 
Both should be at least 2 characters long.
If not, print an error message.
'''
first_name =  input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
if len(first_name) < 2 or len(last_name) < 2:
    print("Error: Both first and last name must be at least 2 characters long.")
else:
    print(f"Hello, {first_name} {last_name}!")
    print(f"Your first name has {len(first_name)} characters and your last name has {len(last_name )} characters.")



