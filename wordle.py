#!/usr/bin/env python

import os
import click
import re

"""
Examples:
wordle.py -i alyn -nl1 aly -nl2 al -nl3 y -nl4 n -l5 y
or equivalently:
wordle.py -i alyn -nl1 aly -nl2 al -nl3 y -nl4 n -p ....y
"""

@click.command()
@click.option('-l1', help='First letter', )
@click.option('-l2', help='Second letter', )
@click.option('-l3', help='Third letter', )
@click.option('-l4', help='Fourth letter', )
@click.option('-l5', help='Fifth letter', )
@click.option('-p', help='Pattern, must be 5 characters (e.g. ".p.le" for "apple"', )
@click.option('-nl1', help='Letters that are not the first letter', )
@click.option('-nl2', help='Letters that are not the second letter', )
@click.option('-nl3', help='Letters that are not the third letter', )
@click.option('-nl4', help='Letters that are not the fourth letter', )
@click.option('-nl5', help='Letters that are not the fifth letter', )
@click.option('-i', help='Include words with letters', )
@click.option('-e', '-x', help='Exclude words with letters', )
def find_matches(**kwargs):
    print(kwargs)
    with open(os.environ('HOME')+"/common/share/dicts/eng_words_alpha_5.txt", "r") as f:
        words = f.read().splitlines()
    print(f"{len(words)} words in dictionary")
    # Exclude
    if kwargs['e']:
        for letter in kwargs['e']:
            words = [ word for word in words if letter not in word ]
        print(f"{len(words)} words remain after excluding {kwargs['e']}")
    # Include
    if kwargs['i']:
        for letter in kwargs['i']:
            words = [ word for word in words if letter in word ]
        print(f"{len(words)} words remain after including {kwargs['i']}")
    # Fixed matching pattern
    if kwargs['p'] is not None:
        pattern = kwargs['p']
    else:
        pattern = ''
        for position in ['l1', 'l2', 'l3', 'l4', 'l5']:
            pattern = pattern + (kwargs[position] if kwargs[position] is not None else '.')
            # print(f"   {pattern} after analysis of {position}")
    if pattern != '.....':
        p_regex = re.compile(pattern)
        words = [ word for word in words if p_regex.match(word)]
    print(f"{len(words)} words remain after matching with {pattern}")
    # Anti-patterns
    for position in range(5):
        if kwargs['nl' + str(1+position)] is not None:
            for letter in kwargs['nl' + str(1+position)]:
                words = [ word for word in words if word[position] != letter]
        pass
    print(f"{len(words)} candidates:")
    print(words)


if __name__ == '__main__':
    find_matches()

