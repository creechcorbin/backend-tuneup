#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment

Use the timeit and cProfile libraries to find bad code.
"""

__author__ = 
            """
                Corbin Creech, worked with Peyton Glover,
                got help with cprofile and timeit docs from Jack Detke,
                got help with refactoring for efficiency from Mike A. Coach
            """

import cProfile
import pstats
import functools
import timeit


def profile(func):
    """A cProfile decorator function that can be used to
    measure performance.
    """
    def c_profile(*args, **kwargs):

        profile = cProfile.Profile()

        try:
            profile.enable()
            result = func(*args, **kwargs)
            profile.disable()
            return result
        finally:
            stats = pstats.Stats(profile)
            stats.sort_stats('cumulative')
            stats.print_stats()
    return c_profile
            



    # Be sure to review the lesson material on decorators.
    # You need to understand how they are constructed and used.
    # raise NotImplementedError("Complete this decorator function")


def read_movies(src):
    """Returns a list of movie titles."""
    print(f'Reading file: {src}')
    movie_dict = {}
    with open(src, 'r') as f:
        for movie in f.read().splitlines():
            if movie not in movie_dict:
                movie_dict[movie] = 1
            else:
                movie_dict[movie] += 1
        return movie_dict


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list."""
    movies = read_movies(src)
    duplicates = []
    for movie in movies:
        if movies[movie] == 2:
            duplicates.append(movie)
    return duplicates


def timeit_helper():
    """Part A: Obtain some profiling measurements using timeit."""
    t = timeit.Timer(
        stmt='find_duplicate_movies("movies.txt")', 
        setup="from tuneup import find_duplicate_movies"
    )

    result = t.repeat(repeat=7, number=5)
    return result


def main():
    """Computes a list of duplicate movie entries."""
    result = find_duplicate_movies('movies.txt')
    print(f'Found {len(result)} duplicate movies:')
    print('\n'.join(result))


if __name__ == '__main__':
    main()
