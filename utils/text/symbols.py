# -*- coding: utf-8 -*-
'''
Defines the set of symbols used in text input to the model.

The default is a set of ASCII characters that works well for English or text that has been run
through Unidecode. For other data, you can modify _characters. See TRAINING_DATA.md for details.
'''

_pad = '_'
_eos = '~'
_bos = '^'
_characters = "กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรลวศษสหฬอฮ(),-.:;? "
_punctuations = "ฤฦะ\u0e31าำ\u0e34\u0e35\u0e36\u0e37\u0e38\u0e39เแโใไ\u0e45\u0e47 "
_phoneme_punctuations = '.!;:,?'

# Phonemes definition
_vowels = 'iyɨʉɯuɪʏʊeøɘəɵɤoɛœɜɞʌɔæɐaɶɑɒᵻ'
_tonemarks = "\u0e48\u0e49\u0e4a\u0e4b"
_signs = "ฯๆ\u0e3a\u0e4c\u0e4d\u0e4e"
_digits = "๐๑๒๓๔๕๖๗๘๙"
_phonemes = sorted(list(_vowels +_tonemarks+_signs))

# Prepend "@" to ARPAbet symbols to ensure uniqueness (some are the same as uppercase letters):
_arpabet = _phonemes#['@' + s for s in _phonemes]

# Export all symbols:
symbols = [_pad, _eos, _bos] + list(_characters)+list(_digits) + _arpabet
phonemes = [_pad, _eos, _bos] + list(_phonemes) + list(_punctuations)

# Generate ALIEN language
# from random import shuffle
# shuffle(phonemes)

if __name__ == '__main__':
    print(" > TTS symbols {}".format(len(symbols)))
    print(symbols)
    print(" > TTS phonemes {}".format(len(phonemes)))
    print(phonemes)
