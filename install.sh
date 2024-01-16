#!/bin/bash

# pip install -y click
INSTALLDIR=$HOME/common
mkdir -p ${INSTALLDIR}/common/bin ${INSTALLDIR}/common/share/dicts
cp wordle.py ${INSTALLDIR}/common/bin/
chmod 755  ${INSTALLDIR}/common/bin/wordle.py
cp eng_words_alpha_5.txt ${INSTALLDIR}/common/share/dicts

