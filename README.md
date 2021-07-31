# Card Games*

Gist of the Python Package linked [here](https://gist.github.com/geovanilopesdias/f1075636694a844d58e6939b52ac2e05).

The program simulates a Brazilian card game known as Cacheta (aka Pife, for the southest state folk, as myself). Its strings and docstrings are all in Portuguese for region issues.

Basically, every player receives nine cards from two standard 52-card decks (previously shuffled). The first player discard one card and gets another from the stock (or from the discard pile, as the game goes on): he/she may take it or discard it, ending his/her turn. The objetive is, by getting and discarding, in his/her own turn, to build three "trincas" of any kind (there are two kinds of trincas, as I further mention). As soon as a player build them, he/she wins the game and "bate": literally "slaps" the hand (and cards) on the table, ending that round.

A "trinca" is a set of three cards. In Cacheta, there are two types of "trincas": (I) a simple natural sequence (e.g. A, 2, 3 or 7, 8, 9) of the same suit or (II) same number, but all different suit (e.g. A gold, A spade, A heart or 5 spade, 5 bat, 5 gold).

## Methods
When I wrote it (2020), I was learning to implement packages and handle exceptions (try statements), but I haven't learned Unit Test yet. Back than, I was able to build the following methods (between parenthesis, I bring their names in the Gits .py files):

**Deck Builder** (cria_baralho): creates a list of (two, by default) standard 52-card decks.
**Game Generator** (cria_jogo): generates the list "jogo" nesting two lists: "mao", with inner lists (one for each player hand), and "monte" (the stock) with the remaining cards.
**Trinca Setter II** (arruma_trinca): receive a list with a player hand and adjusts all the trincas of the type II in the list.
**Trinca Setter I** (arruma_sequencia): adjust a trinca of the type I; it isn't fully implemented. No, it is not as simple as sort the player hand list: this would undo the later mentioned settlement (_Trinca Setter II_).
**Card Getter** (compra_carta): adjusts the lists "mao" (the player hand on turn) accordingly with his/her decision: (a) pick the top card on the discard pile or (b) pick a random card from the stock, as weel as (b1) throwing it away or (b2) taking it. The method also refreshs the discard pile list ("descarte") and the stock list ("monte").

As I abandon this script (because, back then, I was too bored to improve it), I didn't write the following methods (besides making _Trinca Setter I_ functional):

**Reshuffle**: as the name suggests, the method would receive the discard pile list and would refresh it as its top card and would shuffle the rest as the new stock list.
**Victory**: a method to identify that a player hand is a winner, finishing the game.

A distant possibility would be to generate an AI to play it, but I currently don't know any Machine Learning feature to make this possible - far from it!

\*Note: There is a method (called "cria_baralho_truco") to serve for another common Brazilian game (common, at least, bewtween elderly in my region): "Truco", but it was never written. Forseeing it, I tried to write the methods above to serve as many card games as possible (of course, of the hand check-pick-discard-turn type of game).
