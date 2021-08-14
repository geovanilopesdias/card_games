# Card Games

The files has code for simulation of card games that work in turns. Originally developed to simulate a Brazilian game known as Cacheta (aka Pife, for the southest state folk, as myself, or Pif-Paf). Therefore, strings and docstrings are all in Portuguese for region issues.

## Cacheta 
Basically, every player receives nine cards from two standard 52-card decks (previously shuffled). The first player discard one card and gets another from the stock (or from the discard pile, as the game goes on): he/she may take it or discard it, ending his/her turn. The objetive is, by getting and discarding, in his/her own turn, to build three "trincas" of any kind (there are two kinds of trincas, as I further mention). As soon as a player build them, he/she wins the game and "bate": literally "slaps" the hand (and cards) on the table, ending that round.

A "trinca" is a set of three cards. In Cacheta, there are two types of "trincas": (I) a simple natural sequence (e.g. A, 2, 3 or 7, 8, 9) of the same suit or (II) same number, but all different suit (e.g. A gold, A spade, A heart or 5 spade, 5 bat, 5 gold).

## Methods
When I wrote it (2020), I was learning to implement packages and handle exceptions (try statements), but I haven't learned Unit Test yet. Back than, I was able to build the following methods (between parenthesis, I bring their names in the Gits .py files):

### File card_methods
**Deck Builders** (cria_baralho_frances and cria_baralho_espanhol\*): creates a list of (two, by default) standard 52-card decks.
**Game Generator** (cria_jogo): generates the list "jogo" nesting two lists: "mao", with inner lists (one for each player hand), and "monte" (the stock) with the remaining cards.
**Trinca Setter** (arruma_mao)\*\*: receive a list with a player hand and adjusts all the trincas, primarily Trinca of type II, as they are easily to form, due to its larger sample space\*\*\*.
**Card Getter** (compra_carta): adjusts the lists "mao" (the player hand on turn) accordingly with his/her decision: (a) pick the top card on the discard pile or (b) pick a random card from the stock, as weel as (b1) throwing it away or (b2) taking it. The method also refreshs the discard pile list ("descarte") and the stock list ("monte"). It is currently on enhancement, due to bugs after Trinca Setter method update.

As I abandon this script (because, back then, I was too bored to improve it), I didn't write the following methods (besides making _Trinca Setter I_ functional):

**Reshuffle**: as the name suggests, the method would receive the discard pile list and would refresh it as its top card and would shuffle the rest as the new stock list.
**Victory**: a method to identify that a player hand is a winner, finishing the game.

A distant possibility would be to generate an AI to play it, but I currently don't know any Machine Learning feature to make this possible - far from it!

\*Note: There is a method (called "cria_baralho_truco") to serve for another common Brazilian game (common, at least, bewtween elderly in my region): "Truco", but it was never written. Forseeing it, I tried to write the methods above to serve as many card games as possible (of course, of the hand check-pick-discard-turn type of game).
\*\* Update (13/8/21): Originally, there was two separate methods, one for each trinca, but as they were inconsistent, I need to improve the code.
\*\*\*: The sample space for a trinca of the type I is 4n-8, but for the type II is 24n (for n cards in players hand).
