#!/usr/bin/env python
# coding: utf-8

# <br><p style="margin-left: 25%; font-size:20px;">Machine Learning Camp: HomeWork 5</p><br>

# In[2]:


import nltk
nltk.download('stopwords')


# In[6]:


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from string import punctuation


# ##
# <span style="font-wight:bold;font-size:20px">1. Text Data analysis:</span> using “lincoln-last-speech.txt” which contains Lincoln’s last public address. Now answer the following questions and include your codes.

# ##### a) Read the text and store the text in lAddress. Show the first 70 characters from the first element of the text.

# In[7]:


with open("lincoln-last-speech.txt", "r") as file:
    print(file.read(70))
    


# ##### b) Now we are interested in the words used in his speech. Extract all the words from lAddress, convert all of them to lower case and store the result in vWord. Display first few words.

# In[8]:


with open("lincoln-last-speech.txt", "r") as file:
    IAddress  = (file.read())

vWord = word_tokenize(IAddress.lower())
vWord[0:11]


# ##### c) The words like am, is, my or through are not much of our interest and these types of words are called stop-words. Get all the English stop words and store them in sWord. Display few stop words in your report.

# In[9]:


swords = stopwords.words("english")
swords[:11]


# ##### d) Remove all the sWord from vWord and store the result in cleanWord. Display first few clean words.

# In[10]:


punctuation ='`` -- !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
remove_sword = []
for word in vWord:
    if word in swords:
        del word
    else:
        remove_sword.append(word)
remove_sword
clean_word = [w for w in remove_sword if w not in punctuation ]
clean_word[:11]


# ##### f) Construct a bar chart showing the count of each words for the 15 most frequently used words.

# In[11]:


import pandas as pd
from nltk import FreqDist
import seaborn as sns


# In[12]:


fdist = FreqDist(clean_word )
most_word = fdist.most_common(15)
most_word


# In[23]:


df_most_word = pd.DataFrame(most_word, columns=['word', "count"])
df_most_word


# In[27]:


sns.barplot(data= df_most_word, x="word", y="count",width= 0.7)


# ##### h) The plot in question (1f) uses bar plot to display the data. Can you think of another plot that delivers the same information but looks much simpler? Demonstrate your answer by generating such a plot.

# In[14]:


import matplotlib.pyplot as plt
from matplotlib.pyplot import figure


# In[15]:


from wordcloud import WordCloud
wordcloud = WordCloud(collocations=False,width = 800, height = 800,background_color ='white',min_font_size = 10).generate(" ".join(clean_word))
plt.figure(figsize = (5, 5), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
 
plt.show()


# ##
# <span style="font-wight:bold;font-size:20px">2. Answering Questions from Data:</span> Download the data from [ 
# https://github.com/MapsaBootCamp/useful_datasets/blob/master/structuralData/flights.csv ]. Answer the following questions using this data.
# 

# ##### a) What month had the highest proportion of cancelled flights? What month had the lowest? Interpretany seasonal patterns. Please produce a plot that illustrates the proportion of cancelled flights for each month.

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv('flights2.csv')
df.head()


# In[17]:


df["month"].isnull().count()


# ##### b) What plane (specified by the tailnum variable) traveled the most times from New York City airports in 2013? Plot the number of trips per week over the year.

# In[21]:


df.groupby('tailnum')
flights_df[(flights_df['origin'] == 'JFK')| (flights_df['origin'] == 'LGA') & (flights_df['year'] == 2013)].groupby(['tailnum'])['tailnum'].count().nlarg


# ##### c) Download the plane data from [ https://github.com/MapsaBootCamp/useful_datasets/blob/master/structuralData/planes.csv ]. Use the flights and planes tables to answer the following questions: What is the oldest plane (specified by the tailnum variable) that flew from New York City airports in 2013? How many airplanes that flew from New York City are included in the planes table?

# In[8]:


#TODO


# ##### d) Use the flights and planes tables to answer the following questions: How many planes have a missing date of manufacture? What are the five most common manufacturers (Note: pay close attention to the same manufacturer being represented multiple times)? Has the distribution of manufacturer changed over time as reflected by the airplanes flying from NYC in 2013? Produce a plot that backs up your claim.

# In[9]:


#TODO


# ##
# <span style="font-wight:bold;font-size:20px">3. Regular Expressions:</span> Write a regular expression to match patterns in the following strings. Demonstrate
# that your regular expression indeed matched that pattern by including codes and results.

# ##### a) We have a list vText as follows. Write a regular expression that matches g, og, go or ogo in vText and replace the matches with ‘.’.

# In[114]:


import re


# In[2]:


vText = ['google','logo','dig', 'blog', 'boogie']


# In[5]:


for v in vText:
    x = re.sub("[g]|[og]|[ogo]|[go]", ".", v)
    print(x)


# ##### b) Replace only the 5 or 6 digit numbers with the word “found” in the following list. Please make sure that 3, 4, or 7 digit numbers do not get changed.

# In[121]:


vPhone = ['874','6783','345345', '32120', '468349', '8149674']


# In[122]:


re.sub(pattern=r'\b\d{5,6}\b', string=str(vPhone), repl='found')


# ##### c) Replace all the characters that are not among the 26 English characters or a space. Please replace with an empty spring.

# In[15]:


myText = "#y%o$u @g!o*t t9h(e) so#lu!tio$n c%or_r+e%ct"


# In[16]:


re.sub(pattern=r'\b\w{3,4}\b', string=str(vPhone), repl='found')


# ##### d) In the following text, replace all the words that are exactly 3 or 4 characters long with triple dots ‘. . . ’

# In[123]:


myText = "Each of the three and four character words will be gone now"


# In[124]:


re.sub(pattern=r'\b\w{3,4}\b', string=str(myText), repl='...')


# ##### e) Extract all the three numbers embedded in the following text.

# In[19]:


bigText = 'There are four 20@14 numbers hid989den in the 500 texts'


# In[20]:


#TODO


# ##### f) Extract all the words between parenthesis from the following string text and count number of words.

# In[21]:


myText = 'The salries are reported (in millions) for every company.'


# In[22]:


#TODO


# ##### g) Extract the texts in between _ and dot(.) in the following list. Your output should be ‘bill’, ‘pay’, ‘fine-book’.

# In[23]:


myText = ["H_bill.xls", "Big_H_pay.xls", "Use_case_fine-book.pdf"]


# In[24]:


#TODO


# ##### h) Extract the numbers (return only integers) that are followed by the units ‘ml’ or ‘lb’ in the following text.

# In[120]:


myText = 'Received 10 apples with 200ml water at 8pm with 15 lb meat and 2lb salt'
re.findall(r'(\d*[0-9])[ml|lb|pm]', (myText))


# ##### i) Extract only the word in between pair of symbols \\$. Count number of words you have found between pairs of dollar sign \\$

# In[116]:


myText = 'Math symbols are $written$ in $between$ dollar $signs$'
re.findall(r'\$\w+\b\$', str(myText))


# In[28]:





# ##### j) Extract all the valid equations in the following text.

# In[115]:


myText = 'equation1: 2+3=5, equation2 is: 2*3=6, do not extract 2w3=6'
re.findall(r'\b\d[\+|\*]\d[\=]\d', str(myText))


# In[30]:




