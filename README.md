# FuchsiaCultivarDataCleaning

With Tabuls I could not correctly parse new lines within one cell, therefoer I have switched to PDFplumber. It appeared though that in the original file some data in columns were interchanged or mistyped. 

The code parses PDF file with Tabula library. But the parcing is incorrect: if a text in a cell is broken into multiple lines, Tabula understands it as a completely new line. LATTICE option is not working, unfortunately.

