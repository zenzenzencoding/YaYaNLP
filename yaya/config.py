# coding=utf-8
__author__ = 'tony'
import os

DICT_BIN_EXT = '.ya'
DICT_BIN_REVERSE_EXT = '.reverse.ya'
DATA_ROOT = "/home/tony/MyProject/YaYaNLP/data"

CUSTOM_DICT_NAME = [os.path.join(DATA_ROOT, "dictionary", "custom", f) for f in [
    u"CustomDictionary.txt",
    u"上海地名.txt",
    u"人名词典.txt",
    u"全国地名大全.txt",
    u"机构名词典.txt",
    u"现代汉语补充词库.txt"]]

CORE_DICT_NAME = os.path.join(DATA_ROOT, "dictionary", "CoreNatureDictionary.txt")
CORE_BIGRAM_NAME = os.path.join(DATA_ROOT, "dictionary", "CoreNatureDictionary.ngram.txt")
CORE_TR_PATH = os.path.join(DATA_ROOT, "dictionary", "person", "CoreNatureDictionary.tr.txt")

CHAR_TYPE_PATH = os.path.join(DATA_ROOT, "dictionary", "other", "CharType.dat.yes")

PERSON_TR_PATH = os.path.join(DATA_ROOT, "dictionary", "person", "nr.tr.txt")
PERSON_DICT_NAME = os.path.join(DATA_ROOT, "dictionary", "person", "nr.txt")

ORG_TR_PATH = os.path.join(DATA_ROOT, "dictionary", "organization", "nt.tr.txt")
ORG_DICT_NAME = os.path.join(DATA_ROOT, "dictionary", "organization", "nt.txt")

PLACE_TR_PATH = os.path.join(DATA_ROOT, "dictionary", "place", "ns.tr.txt")
PLACE_DICT_NAME = os.path.join(DATA_ROOT, "dictionary", "place", "ns.txt")

TRADITIONAL_CHINESE_DICT_NAME = os.path.join(DATA_ROOT, "dictionary", "tc", "TraditionalChinese.txt")

# 全局配置
class _Config:
    # 是否优先使用缓存字典
    use_dict_cache = True

    # 是否使用用户字典
    use_custom_dict = True

    # 中国人名识别
    name_recognize = True

    # 地名识别
    place_recognize = True

    # 机构识别
    org_recognize = True

    debug = True


Config = _Config()
