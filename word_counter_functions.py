def get_sentence_input():
    sentence = input("Enter a sentence: ")
    return sentence

def count_words(sentence):
    word_count = len(sentence.split())
    return word_count

if __name__ == "__main__":
    output1 = get_sentence_input()
    output2 = count_words(output1)
    print(f"The sentence has {output2} words.")
