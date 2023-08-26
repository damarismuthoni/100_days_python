my_str = "I am learning to code"
words = my_str.split()

for word in words:
    print(word)

# EXAMPLE 2

my_par = '''Lorem ipsum dolor sit amet, consectetur 
            adipiscing elit, sed do eiusmod tempor 
              ut labore et dolore magna aliqua. Ut enim 
              ad minim veniam, quis nostrud exercitation 
              in reprehenderit in voluptate velit esse c
                '''

sentences = my_par.split("\n")

for sentences in sentences:
    print(sentences)