stire="Python este în continuare cel mai popular limbaj de programare datorită dezvoltării tehnologiilor AI."
mij=len(stire)//2
prima_jumatate=stire[:mij]
doi_jumatate=stire[mij:]
prima_jumatate=prima_jumatate.upper()
prima_jumatate=prima_jumatate.strip()
doi_jumatate=doi_jumatate[::-1]
doi_jumatate=doi_jumatate[0].upper()+doi_jumatate[1:]
doi_jumatate=doi_jumatate.replace(",", "")
doi_jumatate=doi_jumatate.replace(".", "")
doi_jumatate=doi_jumatate.replace("!", "")
doi_jumatate=doi_jumatate.replace("?", "")
text_final=prima_jumatate+doi_jumatate
print(text_final)