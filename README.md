# Text Analysis Tutorial

## Requirements


### Python

This tutorial is written in Python and requires Python 3.5 or 3.6.

**Recommended:** The most convenient way is to install [Anaconda](https://www.anaconda.com/download/#linux):

> With over 6 million users, the open source Anaconda Distribution is the easiest way to do Python data science and machine learning. It includes hundreds of popular data science packages and the conda package and virtual environment manager for Windows, Linux, and MacOS. Conda makes it quick and easy to install, run, and upgrade complex data science and machine learning environments like Scikit-learn, TensorFlow, and SciPy. Anaconda Distribution is the foundation of millions of data science projects as well as Amazon Web Services' Machine Learning AMIs and Anaconda for Microsoft on Azure and Windows.


### Packages

This tutorial requires various packages. The following packages come already with Anaconda. If you use a standard Python installation, you can click on the links to the websites with the instructions for the installation.

+ [numpy](https://scipy.org/install.html)
+ [scikit-learn](http://scikit-learn.org/stable/install.html)
+ [pandas](https://pandas.pydata.org/pandas-docs/stable/install.html)
+ [nltk](https://www.nltk.org/install.html)
+ [matplotlib](https://matplotlib.org/users/installing.html)
+ [jupyter](http://jupyter.readthedocs.io/en/latest/install.html)

The following packages also need to be installed:

+ [spacy](https://spacy.io/usage/)
+ [tensorflow](https://www.tensorflow.org/install/)
+ [keras](https://keras.io/#installation)
+ [newspaper](https://github.com/codelucas/newspaper/)
+ [twython](https://twython.readthedocs.io/en/latest/usage/install.html)


### Data and Models

Some of the packages require some additional data

#### spacy

spacy comes with trained models for different languages (see [here](https://spacy.io/models/en) for more details). This tutorial requires the model for English. You can download and install the model using the following command:

```
python -m spacy download en_core_web_sm
```

#### nltk

Run the Python interpreter and type the commands:
```
>>> import nltk
>>> nltk.download()
```
A new window should open, showing the NLTK Downloader. In this new window, click in the Tab "All Packages" to see all available data and models. You can install packages by simply double-clicking them. Installed packages are marked as green. The following packages are needed:

+ averaged_perceptron_tagger
+ maxent_ne_chunk
+ punkt
+ tagset
+ treebank
+ stopwords
+ wordnet
+ words

For convenience, you can also simply download all packages using the following command:

```
python -m nltk.downloader all
```
