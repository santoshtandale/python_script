import word_funcs
sentence = "All good things come to those who wait."
words = word_funcs.break_words(sentence)
words
sorted_words = word_funcs.sort_words(words)
sorted_words
word_funcs.print_first_word(words)
word_funcs.print_last_word(words)
words
word_funcs.print_first_word(sorted_words)
word_funcs.print_last_word(sorted_words)
sorted_words
sorted_words = word_funcs.sort_sentence(sentence)
sorted_words
word_funcs.print_first_and_last(sentence)
word_funcs.print_first_and_last_sorted(sentence)
