from neuspell.noising import WordReplacementNoiser

example_texts = [
    "This is an example sentence to demonstrate noising in the neuspell repository.",
    "Here is another such amazing example!!"
]

noisers = [
    WordReplacementNoiser,
]

for noiser in noisers:

    my_noiser = noiser(language="english")
    my_noiser.load_resources()
    noise_texts = my_noiser.noise(example_texts)
    print(noise_texts)

    preprocessor = noiser.create_preprocessor(lower_case=True, remove_accents=True)
    retokenizer = noiser.create_retokenizer()
    noise_texts = my_noiser.noise(example_texts, preprocessor=preprocessor, retokenizer=retokenizer)
    print(noise_texts)

    preprocessor = noiser.create_preprocessor(lower_case=True, remove_accents=True)
    retokenizer = noiser.create_retokenizer(use_spacy_retokenization=True)
    noise_texts = my_noiser.noise(example_texts, preprocessor=preprocessor, retokenizer=retokenizer)
    print(noise_texts)