# tatoeba2anki

This is a tool to wrangle raw Tatoeba data into a good quality Anki deck.
The purpose of this tool is to allow linguists to quickly and easily create Anki decks that help them learn their target language more efficiently. 

Learning a language through sentence pairs is a very effective technique. Many people are used to learning singular words or vocab lists, but the sentence pairs approach is helpful because it allows you to see each word in its semantic and grammatical context. You then start to build up a network of related words in your head, which makes them easier to remember.

Tatoeba (tatoeba.org) is an open source project where linguists build up collections of parallel language sentences. It is a valuable source of language learning data.

Instructions to download a raw dataset from Tatoeba are in this repo's code.

The raw Tatoeba data comes in the form of sentence pairs in the language you want to learn and English. 
If you are learning from a language other than English, this code will still work, but you may want to change some variable names.

The input is a raw csv file of sentence pairs from Tatoeba's website.
The output is a cleaned csv file which is ready to import from your Desktop straight into the Anki app. The instructions for this final step are included at the end of the Python script.

The four things this code does are:

- Cleans the data into a format suitable for Anki
- Drops any duplicate sentences
- Filters the sentence pairs by words/phrases you want to learn
- Filters the sentence pairs by their complexity

Each of the above are explained in more detail in the code. 

In addition to the Python script, this repo contains a Jupyter Notebook with the same code so you can experiment with each step and add more capability. The notebook contains a bit more documentation than the script. 

Pandas is the only library you need to install.
