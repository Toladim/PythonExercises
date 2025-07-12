def format_sentence(sentence: str) -> str:
    sentence = sentence.strip()
    sentence = sentence.capitalize()
    return sentence

example = "  wItAj Na KuRSie PYthonA  "
print(format_sentence(example))