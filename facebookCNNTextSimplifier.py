from transformers import pipeline, BartForConditionalGeneration, BartTokenizer
import warnings

def Simplify(filename):
    warnings.filterwarnings("ignore", category=UserWarning, module="transformers.configuration_utils")
    print("Generating model")
    model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn", do_sample=True)
    print("Generating tokenizer")
    tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
    print("Generating simplifier")
    simplifier = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

    print("Reading file")
    with open(filename, 'r', encoding='utf-8') as file:
        input_text = file.read()

    max_text_length = 1024  # Maximum length for BART

    # Truncate the text if it's too long
    if len(input_text) > max_text_length:
        input_text = input_text[:max_text_length]

    print("Simplifying...")
    # Generate simplified text
    simplified_output = simplifier(input_text, max_length=max_text_length, min_length=int(max_text_length/2), temperature=0.7)

    # Extract the generated text from the output
    simplified_text = simplified_output[0]['generated_text'] if simplified_output else "Failed to simplify the text"

    return simplified_text
