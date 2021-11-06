PISKVORKY by dancejod

Hra piskvorky pre dvoch hracov, vytvorene v korytnacej grafike v sestuholnikovej sieti.
Hra v tejto verzii nevyhodnocuje vitaza, ani prekryvanie sa tahov jednotlivych hracov.


HRA

Pri spusteni programu ma pouzivatel moznost prisposobit si velkost hracieho pola cez vstupy. Vstup je osetreny tak, aby bol pocet riadkov a stlpcov nezaporne cele cislo rozne od nuly. Pouzivatel moze zadat lubovolne cele cislo.

Hraci sa striedaju, kazdy hrac musi zadat dva vstupy: jeden je suradnica riadka, druhy je suradnica stlpca. Kontrolny cyklus osetruje vstupy tak, aby bol tah prevedeny, len ak zada suradnice vo vnutri hracieho pola; suradnice su cele cisla.
Ak hrac zada float, program spadne.
Ak hrac zada prazdny vstup, program spadne.
Ak sa predvedie tolko tahov, kolko je v hre hernych policok, hra sa ukonci a nie je mozne do nej dalej vkladat symboly.


PREVEDENIE

Dlzka strany sestuholnika (t. j. jednej bunky hracieho pola) je zamerne mala, aby bolo miesto pre vacsi pocet policok.
V programe su premenne, v ktorych su ulozene vypocty pre lokalizaciu suradnic; vyuzivaju sa pri tom vlastnosti rovnostrannych trojuholnikov, z ktorych sestuholnik pozostava.