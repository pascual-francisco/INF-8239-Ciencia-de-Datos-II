FILE reviews_cod_all.txt 

The file contains the set of reviews. 
The separator between reviews is the line “%%”.
Each review is defined by a sequence of words. Each word is defined in a row.
Each word is encoded as a sequence of feature identifiers: 
"id_Dict" "Next1" "Next2" "Next3" "Next4" "Next5" "Back1" "Back2" "Back3" "Back4" "Back5" "Frec1" "Frec2"

id_Dict: identifier of the current word (dictionary ID).
Next1: identifier of the next word in the review (shift = +1).
Next2: identifier of the word following Next1 (shift = +2 relative to id_Dict).
Next3: identifier of the word following Next2 (shift = +3 relative to id_Dict).
Next4: identifier of the word following Next3 (shift = +4 relative to id_Dict).
Next5: identifier of the word following Next4 (shift = +5 relative to id_Dict).
Back1: identifier of the previous word in the review (shift = −1).
Back2: identifier of the word preceding Back1 (shift = −2 relative to id_Dict).
Back3: identifier of the word preceding Back2 (shift = −3 relative to id_Dict).
Back4: identifier of the word preceding Back3 (shift = −4 relative to id_Dict).
Back5: identifier of the word preceding Back4 (shift = −5 relative to id_Dict).
Frec1: empty field (reserved).
Frec2: frequency of the word in the set of reviews.

FILE reviews_tw_definitivo.txt
The file consists of 63,237 rows
Each row encodes a review with the fields: identifier; set; label

Set values only for internal use 

Label values:
4=NONE;
3=Good (P)
2=Regular(NEU)
1=Bad (N)




FILE words_cod_all.txt
The file consists of 53,385 rows. 
Each row contains the word and its identifier "id_Dict".
