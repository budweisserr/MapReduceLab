MapReduce Python Simulator

Sample
```bash 
python -m src.cli.main run --workers 4 --input data/input --output data/output/wordcount --job src.student_jobs.word_count.mapper:WordCountMapper,src.student_jobs.word_count.reducer:WordCountReducer --reducers 4
```
    
Task 1
-
cleaning garbage (punctuation etc), lowercase, count words
```bash 
python -m src.cli.main run --workers 4 --input data/input --output data/output/clean_word_count --job src.student_jobs.clean_word_count.mapper:CleanWordCountMapper,src.student_jobs.clean_word_count.reducer:CleanWordCountReducer --reducers 4
```

Task 2
-
clean text like previous task, count word only > 5 symbols
```bash 
python -m src.cli.main run --workers 4 --input data/input --output data/output/long_words --job src.student_jobs.long_words.mapper:LongWordsMapper,src.student_jobs.long_words.reducer:LongWordsReducer --reducers 4
```

Task 3
-
for each word count symbol from vowel/consonant. output includes % of each
```bash 
python -m src.cli.main run --workers 4 --input data/input --output data/output/vowel_cons --job src.student_jobs.vowel_consonant.mapper:VowelConsMapper,src.student_jobs.vowel_consonant.reducer:VowelConsReducer --reducers 4
```


