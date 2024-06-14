#Product Review AnalysisThe aim of this assignment is to extract insights from product reviews by using string manipulation to categorize and summarize customer feedback for a SaaS product.

#Task 1: Keyword Highlighter Write a program that searches through a series of product reviews for keywords such as "good", "excellent", "bad", "poor", and "average". Print out each review with the keywords in uppercase so they stand out.
keywords=["GOOD", "EXCELLENT", "BAD", "POOR","AVERAGE"]
python_reviews = [ "This product is really " + keywords[0],"I'm impressed with its quality.", 
                  "The performance of this product is, "+ keywords[1], "Highly recommended!",
                  "I had a " + keywords[2], "experience with this product. It didn't meet my expectations.", 
                  keywords[3],"quality product. Wouldn't recommend it to anyone.",
                  "The product was " + keywords[4], "Nothing extraordinary about it." ] 
key=[i.lower() for i in keywords]

good_review=keywords[:2]
bad_reviews=keywords[2:]
script1=[ "The performance of this product is"]
script2=["EXCELLENT, Highly recommended! - VERIFIED USER. (**only trust verified users**)"]
new_script=script1+script2
             
print(key)
print(python_reviews)
#Task 2: Sentiment Tally Develop a function that tallies the number of positive and negative words in each review. 
print(good_review,",are the only good reviews.")
print (bad_reviews,", are negative reviews....")
#Task 3: Review Summary Implement a script that takes the first 30 characters of a review and appends "…" to create a summary.
for script in new_script:
    print(new_script)
    break


