# Notes
## To create [audio processing](./README.md/#audio-processing)
follow the process:
1. leverage the [audio neural network](https://colab.research.google.com/github/pytorch/tutorials/blob/gh-pages/_downloads/c64f4bad00653411821adcb75aea9015/speech_command_classification_with_torchaudio_tutorial.ipynb#scrollTo=4dXYSfCJmqb_)
2. The labels are "lex" and "non-lex"
3. leverage the youtube api in pythong to grab audio clips that correspond to the transcript timestamps
4. train an audio nn using this clips (you know that lex is the only speaker at the beginning and the end)
5. identify the speaker given the selected timestamp segment
6. collect only the segments that are from Lex Fridman
7. compile this data from ALL of the podcast videos
8. load this data into a notebook
9. define a function that will iterate through the data given an exact phrase or keyword
10. print the number of times this phrase or keyword is said by Lex

## To complete [Greatness](./README.md/#natural-language-processing)
follow the process:
1. find the topic based on a keyword
2. expand n-segments outward from the keyword
3. cut & paste into GPT-3 to produce the body
4. Query for results
  