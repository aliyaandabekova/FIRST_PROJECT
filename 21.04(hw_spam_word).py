data = [
    {'text':'oh hi duuuude how r uy??check this 1xbet'},
    {'text':'Dear Harry Potter, i am Frodo Baggins i represent 1xbet company.Best bet service'},
    {'text':'wooooh yoow harry look at my jackpot 100000000$ at 1xbet service'},
    {'text':'Harry , today i saw the man who looks like Hawkeye from Avengers on 100% and he dont use 1xbet service'},
]
final_mail = 'Hello Harry, my name is Maksim, Im still waiting for the letter from Hogwarts 1XBet'



spam_word = " "
database = []
qspam = 0
for mail in data:
    # print(data)
    str = mail['text'].lower().split()
    database.extend(str)
for word in database:
    quantity = database.count(word)
    if quantity > qspam:
        qspam = quantity
        spam_word = word
print(qspam, spam_word)
if spam_word in final_mail.lower():
    print("NOT OK")
else:
    print("Ok")
