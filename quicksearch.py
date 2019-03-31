#!/usr/bin/python3

class QuickSearch:
    offset = 0
    steps = 0
    jumptable = dict()
    pattern = ""
    input = ""

    def __init__(self, input: str, pattern: str):
        self.input = input
        self.pattern = pattern

        self._getLanguage()
        self._calculateJumps()
        self._search()

    def _getLanguage(self):
        for c in self.input:
            self.jumptable[c] = 0

    def _calculateJumps(self) -> dict:
        count = 1
        for c in self.pattern[::-1]:
            self.jumptable[c] = count
            count = count + 1
        n = len(self.pattern) + 1
        for k in self.jumptable.keys():
            if self.jumptable[k] == 0:
                self.jumptable[k] = n

    def _search(self):
        while (True):
            i = 0
            while i < len(self.pattern):
                self.steps = self.steps + 1
                if self.input[self.offset + i] != self.pattern[i]:
                    if len(self.input) <= self.offset + len(self.pattern):
                        raise QuickSearch.NotFoundException()
                    self.offset = self.offset + self.jumptable[self.input[self.offset + len(self.pattern)]]
                    break
                i = i + 1
            if i == len(self.pattern):
                self.offset = self.offset + 1
                return
        raise QuickSearch.NotFoundException()

    class NotFoundException(Exception):
        def __init__(self):
            self.message = "Not found"
