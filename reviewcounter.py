def main():
    reviewsFile = open("restaurant_reviews.txt")
    
    reviewsCountDict ={}
    
    for line in reviewsFile:
        line =line.strip()
        
        name, rating, comment = line.split(";")
        
        #Get is a method that checks if there is a key, if there is no key, creates a key
        ratingComments =reviewsCountDict.get(rating, [])
        ratingComments.append(comment)
        reviewsCountDict[rating]= ratingComments
        
    print(reviewsCountDict["Fair"])
    for ratingKey in reviewsCountDict:
        commentsList = reviewsCountDict[ratingKey]
        print("{}: {}".format(ratingKey, len(commentsList)))
main()