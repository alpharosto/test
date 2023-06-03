import re
import language_tool_python
from autocorrect import Speller

def correct_text(text):
    tool = language_tool_python.LanguageTool('en-US')
    spell = Speller()

    # Correct spacing
    text = re.sub(r'\s+', ' ', text.strip())

    # Split the text into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text)

    # Correct each sentence
    corrected_sentences = []
    for sentence in sentences:
        # Check grammar and get suggestions
        grammar_errors = tool.check(sentence)
        corrected_sentence = sentence

        # Replace grammar errors with suggestions
        for error in grammar_errors:
            if error.replacements:
                corrected_sentence = corrected_sentence.replace(error.context, error.replacements[0])

        # Correct words
        corrected_words = [spell(word) if word.isalpha() else word for word in corrected_sentence.split()]

        # Join the corrected words back into a sentence
        corrected_sentences.append(' '.join(corrected_words))

    # Join the corrected sentences back into a text
    corrected_text = ' '.join(corrected_sentences)

    return corrected_text

def main():
    input_text = input("Enter the text to correct: ")
    corrected_text = correct_text(input_text)
    print("Corrected text:")
    print(corrected_text)

if __name__ == "__main__":
    main()
