#! /usr/bin/env python3

import argparse
import random

def run(num_of_words):
    word_map = get_word_map()
    words = get_words(num_of_words, word_map)

    capitalized = [word.capitalize() for word in words]
    print("".join(capitalized))


def get_words(num_of_words, word_map):
    words = []

    for i in range(num_of_words):
        rolls = [str(random.randint(1, 6)) for _ in range(5)]
        key = "".join(rolls)
        words.append(word_map[key])

    return words


def get_word_map():
    with open('word_list.txt') as f:
        lines = f.readlines()
       
        word_map = {}

        for item in lines:
            key, value = item.split(':')
            word_map[key] = value.replace('\n', '')

        return word_map


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=int, default=4, help='Number of words to generate')

    args = parser.parse_args()
    run(args.n)
