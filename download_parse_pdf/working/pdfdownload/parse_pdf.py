import PyPDF2

pdfFileObj = open('pdfs/5-ASA_Derivatives_Criteria.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)
search_word = "CRITERIA FOR APPROVAL"
search_word_count = 0
for pageNum in range(0, pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    text = pageObj.extractText().encode('utf-8')
    search_text = text.lower().split()
    # if search_word in text.decode("utf-8"):
    #     search_word_count += 1
    return_txt = text.decode("utf-8")[text.decode("utf-8").find(search_word):]
    print(return_txt)


# print("The word {} was found {} times".format(search_word, search_word_count))
