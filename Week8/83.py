def rephrase_sentence(sentence, synonym_dict):
    words = sentence.split()
    rephrased_words = ""
    for word in words:
        if synonym_dict.get(word)!=None:
            rephrased_words+=synonym_dict[word]+" "
        else:
            rephrased_words+=word+" "
    return rephrased_words

SYNONYM_DICTIONARY = {
    "great": "amazing",
    "quick": "rapid",
    "see": "observe",
    "start": "commence",
    "work": "task",
    "very": "extremely",
    "happy": "joyful",
    "idea": "concept",
    "build": "construct"
}
s=input("Enter a sentence:")
print(rephrase_sentence(s,SYNONYM_DICTIONARY))

