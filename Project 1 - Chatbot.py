
name = ('what is your name?')

#Chatbot Information
print('hello. I am Royely 01. I am a chatbot')
print('I like animals and I love to talk about food')
print ('Hi', name, 'nice to meet you')

#get year information
year = input('I am not very good at dates. What is the year?: ')
print('Yes,I think that is correct. Thanks!')

#ask user to guess the age
my_age = ('Can you guess my age? - Enter a number : ')
print('Yes, you are right. I am ', my_age)

#do math to calculate when chatbot will be 100
my_age = int(my_age)
nyears = 100 - my_age
print('I will be 100 in ', nyears, 'years')
print('That will be the year', int(year) + nyears)

#food conversation
print('I love chocolate and I also like trying out new kinds of food')
food = input('How about you? What is your favorite food? : ')
print('I like ',food,'too.')
question = 'how often do you eat' + food + '? :'
howoften = input(question)
print('Interesting. I wonder if that is good for your health')

#animal conversation
animal = input('My favorite anima is dog. What is yours?:')
print(animal, '!I do not like them.')
print('I wonder if a ', animal, 'likes to eat', food,'?')

#conversation about feelings
feeling = input('how are you feeling today?:')
print('Why are you feeling', feeling,'now?')
reason = input('Please tell me : ')
print('I Understand. Thanks for sharing')

#goodbye
print('It has been a long day')
print('I am too tired to talk. We can chat again later.')
print('Goodbye',name,'I liked chatting with you')




