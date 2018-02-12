#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
svakulenko
12 Feb 2017

Generate CSV for process mining the conversations
'''
import csv

from swda import CorpusReader
corpus = CorpusReader('swda')


def main():
    with open('swda.csv', 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';')
        # iterate over transcripts
        for trans in corpus.iter_transcripts():
            # iterate over messages
            # print trans.conversation_no
            for utt in trans.utterances:
                spamwriter.writerow([str(trans.conversation_no), utt.caller, utt.act_tag])


if __name__ == '__main__':
    main()
