# ROYIN Dictionary Parser
Parser for CSV file from ROYIN Thai-Thai dictionary. Part of research under CTFL (Center for Thai as a Foreign Language) internship with Professor Nattanun Chanchaochai. 

## Background
This program is written as part of making a Thai learner's textbook. The main idea is to identify words that are essential for learners and rank its difficulty based on definition. This model is similar to the [CEFR](https://www.englishprofile.org/wordlists/evp) (Common European Framework of Reference for Languages), which classify its vocabulary into levels from A1 (beginner) to C2 (upper advanced). As part of the research, we classified vocabulary words based on frequency using the [Thai National Corpus](https://www.arts.chula.ac.th/ling/tnc3/) and the definition using the [Thai national dictionary](https://dictionary.orst.go.th/) (ROYIN dictionary). 

## What is this parser for?
Before beginning to determine vocabulary difficulties, we needed to pull the dictionary data from the [Thai national dictionary](https://dictionary.orst.go.th/) website. We have a list of 5000 most frequently-used words, and we want to match definitions of these words in this order. This parser is the first step in this process. We obtained a CSV file scraped from an online dictionary source, ordered alphabetically. From this file, I separated each entry into numbered lists, based on our system of a valid definition. 

For more context, the Royal Institute sometimes combine two separate definitions into one entry, which poses a problem to our team. This is where the parser comes in, reducing hand-parsing time from an estimated 6 to 1 month.
