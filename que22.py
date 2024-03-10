""""Spam comment is defined as txt containing 
following keywords(Make a lot of money, Buy 
now, Subscribe this, Click this)Write a program 
to detect this spams"""

def detect_spam(file_path):
    keywords = ["Make a lot of money", "Buy now", "Subscribe this", "Click this"]

    with open(file_path, "r") as file:
        comments = file.readlines()

    spam_comments =[]

    for i in comments:
        for j in keywords:
            if j in i :
                spam_comments.append(i)
                break 

    return spam_comments 


file_path = "comment.txt"
spam_comments = detect_spam(file_path)

if spam_comments:
    print("Spam Comments")
    for comment in spam_comments:
        print(comment)
else :
    print("Np spam comments found ")        