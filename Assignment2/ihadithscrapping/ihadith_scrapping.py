# -*- coding: utf-8 -*-
"""ihadith_scrapping.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ww6n-iffOPsI2RJxNAt_P_7FIugjTDmL
"""

!pip install requests-html

from requests_html import HTMLSession

session = HTMLSession()



"""**iHadith books and chapter**"""

def hadith_book_scrapping(book_name, url, total_chapter):
  # url = "http://ihadis.com/books/bukhari"
  for i in range(1, total_chapter+1):
    chapter_url = url + "/chapter/" + str(i)
    print(chapter_url)
    # chapter_url = http://ihadis.com/books/bukhari/chapter/2

    r = session.get(chapter_url)
    # define the patter
    no_pattern = "h3.hidden-print"
    arabic_text_pattern = "p.hadith-des2"
    bangla_text_pattern = ".hadith-des"
    narrator_pattern = ".narrated-by"
    hadith_status_pattern = ".label.validity"

    numbers = [i.text for i in r.html.find(no_pattern)]
    arabic_text = [i.text for i in r.html.find(arabic_text_pattern)]
    bangla_text = [i.text for i in r.html.find(bangla_text_pattern)]
    narrator = [i.text for i in r.html.find(narrator_pattern)]
    hadith_status = [i.text for i in r.html.find(hadith_status_pattern)]
    print("Chapter: ", i, len(numbers), len(arabic_text), len(bangla_text), len(narrator), len(hadith_status))

    with open(f"{book_name}/{book_name}_chapter_{i}.txt", "w") as f:
      f.write("No., Arabic Text, Bangla Text, Narrator, Hadith Status\n")
      for n, a, b, na, hs in zip(numbers, arabic_text, bangla_text, narrator, hadith_status):
        f.write(f"{n}, {a}, {b}, {na}, {hs}")
        f.write('\n')

import time

book_name = "muslim"
book_url = "http://ihadis.com/books/muslim"
total_chapter = 56
start = time.time()
hadith_book_scrapping(book_name, book_url, total_chapter)
print(f"=========={time.time()-start}=======")

book_name = "bukhari"
book_url = "http://ihadis.com/books/bukhari"
total_chapter = 97
start = time.time()
hadith_book_scrapping(book_name, book_url, total_chapter)
print(f"=========={time.time()-start}=======")

book_name = "nasayi"
book_url = "http://ihadis.com/books/nasayi"
total_chapter = 50
start = time.time()
hadith_book_scrapping(book_name, book_url, total_chapter)
print(f"=========={time.time()-start}=======")

book_name = "abi-dawud"
book_url = "http://ihadis.com/books/abi-dawud"
total_chapter = 43
start = time.time()
hadith_book_scrapping(book_name, book_url, total_chapter)
print(f"=========={time.time()-start}=======")

book_name = "tirmidi"
book_url = "http://ihadis.com/books/tirmidi"
total_chapter = 46
start = time.time()
hadith_book_scrapping(book_name, book_url, total_chapter)
print(f"=========={time.time()-start}=======")

book_name = "ibn-majah"
book_url = "http://ihadis.com/books/ibn-majah"
total_chapter = 37
start = time.time()
hadith_book_scrapping(book_name, book_url, total_chapter)
print(f"=========={time.time()-start}=======")

book_name = "muatta-malik"
book_url = "http://ihadis.com/books/muatta-malik"
total_chapter = 61
start = time.time()
hadith_book_scrapping(book_name, book_url, total_chapter)
print(f"=========={time.time()-start}=======")

book_name = "riadus-saalehin"
book_url = "http://ihadis.com/books/riadus-saalehin"
total_chapter = 20
start = time.time()
hadith_book_scrapping(book_name, book_url, total_chapter)
print(f"=========={time.time()-start}=======")

book_name = "bulugul-maram"
book_url = "http://ihadis.com/books/bulugul-maram"
total_chapter = 16
start = time.time()
hadith_book_scrapping(book_name, book_url, total_chapter)
print(f"=========={time.time()-start}=======")

book_name = "al-lulu-wal-marjan"
book_url = "http://ihadis.com/books/al-lulu-wal-marjan"
total_chapter = 54
start = time.time()
hadith_book_scrapping(book_name, book_url, total_chapter)
print(f"=========={time.time()-start}=======")

book_name = "hadis-somvar"
book_url = "http://ihadis.com/books/hadis-somvar"
total_chapter = 20
start = time.time()
hadith_book_scrapping(book_name, book_url, total_chapter)
print(f"=========={time.time()-start}=======")

book_name = "silsila-sahiha"
book_url = "http://ihadis.com/books/silsila-sahiha"
total_chapter = 1
start = time.time()
hadith_book_scrapping(book_name, book_url, total_chapter)
print(f"=========={time.time()-start}=======")

book_name = "jal-daif-hadis-serise"
book_url = "http://ihadis.com/books/jal-daif-hadis-serise"
total_chapter = 1
start = time.time()
hadith_book_scrapping(book_name, book_url, total_chapter)
print(f"=========={time.time()-start}=======")

book_name = "mishkatul-masabih"
book_url = "http://ihadis.com/books/mishkatul-masabih"
total_chapter = 11
start = time.time()
hadith_book_scrapping(book_name, book_url, total_chapter)
print(f"=========={time.time()-start}=======")

book_name = "40-hadis"
book_url = "http://ihadis.com/books/40-hadis"
total_chapter = 1
start = time.time()
hadith_book_scrapping(book_name, book_url, total_chapter)
print(f"=========={time.time()-start}=======")

book_name = "adabul-mufrad"
book_url = "http://ihadis.com/books/adabul-mufrad"
total_chapter = 22
start = time.time()
hadith_book_scrapping(book_name, book_url, total_chapter)
print(f"=========={time.time()-start}=======")

book_name = "juj-ul-rafaul-yadain"
book_url = "http://ihadis.com/books/juj-ul-rafaul-yadain"
total_chapter = 1
start = time.time()
hadith_book_scrapping(book_name, book_url, total_chapter)
print(f"=========={time.time()-start}=======")

