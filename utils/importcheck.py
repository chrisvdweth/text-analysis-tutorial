#
# These packages should be part of a basic Python installation
#
import os
import sys
import re
import math
import time
import datetime
import string
import random

#
# These packages should be part of an Anaconda installation
#
import nltk
import numpy
import pandas
import sklearn
import matplotlib

#
# These packages need to be installed individually
#
import spacy
import tensorflow
import keras
import twython
import newspaper


#
# The following lines check the Python version
#
python_version = "{}.{}".format(sys.version_info[0], sys.version_info[1])

print("{} <== If this says 3.5 or 3.6 then all should be good.".format(python_version))


print("Import test done.")
