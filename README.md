# Sheety-Rarity-Generator

As the title sort of says... An NFT trait rarity sheet generator. Also an abomination of a thing... 
About as far from originally planned as one can imagine... but... it will read a folder full of jsons for "trait_type", their "value", and then their percentage of the whole.
It is important to set the total number of jsons in the directory currently, especially as it will add a "None" in to make up for those compilers which do not include a "NONE" layer in the metadata and thus break the maths.
It outputs to an HTML file with some very basic navigation from a drop down menu at the top.

Usage is:
generate_stats.py "OPTIONAL PAGE TITLE"

I may have another go at gussying it up when I have the time but it does currently provide a near immediate and accurate breakdown in a fashion from which the numbers can easily be harvested for prettying up if needed.
