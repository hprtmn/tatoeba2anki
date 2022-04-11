# pre-requisite = generate the raw file of sentence pairs in your language combination from https://tatoeba.org/en/downloads. Go to 'Sentence pairs' then hit 'Download sentence pairs'.
import pandas as pd

# read the Tatoeba .tsv file into Pandas. Subtitute your file for the example one below. If you are running this Python script outside the directory where it is saved locally, you will need to include its full file path.
raw_sentence_pairs = pd.read_table('sentence-pairs-es-en.tsv', header=None)

# drop the English sentence identifier column. The source language identifier column will be used instead, and as an index for the whole row.
raw_sentence_pairs.drop(columns=2, inplace=True)

# rename the columns and set the index as the ID of the sentence pair
raw_sentence_pairs.columns = ['Id', 'sourceLanguage', 'English']
raw_sentence_pairs.set_index('Id', inplace=True)

# remove duplicate sentence pairs
raw_sentence_pairs.drop_duplicates(subset=['sourceLanguage','English'], inplace=True)
raw_sentence_pairs.drop_duplicates(subset=['English'], inplace=True)

# narrow the dataset by keywords. Each keyword must be separated by '|'. Substitute or add your target language keywords to the example values in Spanish below.
export_sentence_pairs = raw_sentence_pairs[raw_sentence_pairs['sourceLanguage'].str.contains("ejemplo|frase")]

# finding sentences by the right complexity level
# create a new column containing the length of each sentence (by default in English, but you can change this for your target language).
raw_sentence_pairs['sentence_length'] = raw_sentence_pairs['English'].str.len()

# mean centre the results of the above
average_sentence_length = raw_sentence_pairs['sentence_length'].mean()
raw_sentence_pairs['sentence_length_mean_centered'] = raw_sentence_pairs['sentence_length'] - average_sentence_length

# make into quantiles based on complexity of the sentence. Here, 5 quantiles have been chosen, but this is flexible. If you change this, make sure the number of labels is the same as the number of quantiles.
raw_sentence_pairs['quantiles'] = pd.qcut(raw_sentence_pairs['sentence_length_mean_centered'], 5, labels=["most_simple", "simple", "medium", "complex", "most_complex"])

# isolate the simple and medium complexity sentences
raw_sentence_pairs[raw_sentence_pairs['quantiles'].str.match("simple|medium")]

# add the sentences with the level of complexity you want to a new dataframe which will later be used to merge this data with the final export dataframe
additions_by_complexity = raw_sentence_pairs[raw_sentence_pairs['quantiles'].str.contains("simple|medium")]

# remove irrelevant columns before merging
additions_by_complexity.drop(columns=['sentence_length','sentence_length_mean_centered','quantiles'],inplace=True)

# merge the new additions into the export dataframe
export_sentence_pairs = pd.concat([export_sentence_pairs, additions_by_complexity],ignore_index=True)

# remove duplicates
export_sentence_pairs.drop_duplicates(subset=['English'], inplace=True)

# the last step is to export the final dataframe to a .csv file. The default encoding will be utf-8, which is what Anki requires. header=False ensures the column names won't be added as a card in Anki too. Finally, to get this as a new deck, simply go to 'import file' in your Anki application and select 'anki_import.csv'
export_sentence_pairs.to_csv('anki_import.csv',index=False, index_label=False, header=False)
