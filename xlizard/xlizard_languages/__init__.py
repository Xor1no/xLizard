''' programming languages of xlizard '''

from .clike import CLikeReader


__all__ = ['languages', 'get_reader_for']


def languages():
    return [
        CLikeReader
    ]


def get_reader_for(filename):
    """Находит подходящий Reader для файла"""
    for lan in languages():
        if lan.match_filename(filename):
            return lan