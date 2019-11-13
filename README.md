# Part Of Speech Tagger

Part-of-speech (POS) tagging is one of the most important addressed areas in the natural language processing (NLP). There are effective POS taggers for many languages. We tried to develop a POS tagger for the Arabic language, specifically for the modern standard Arabic (MSA), because it’s the language used in the formal textbooks and news. 
The objective of our solution is to firstly create a tokenizer that splits any file you choose into a list of words with removing any punctuations and numbers from the list. And secondly create a POS tagger which takes the list of words from tokenizer and then tag each word with its appropriate POS(verb, noun, particle) based on a combination of rules. Finally we created a golden corpus from a sample of the actual corpus folder to test our algorithm and see how accurate and precise with its tagging. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them

```
python, pip, pandas, matplotlib, xlrd
```

### Installing


__Python:__

https://www.python.org/downloads/


__pip:__

_If you're running Python 2.7.9+ or Python 3.4+_
Congrats, you should already have pip installed. If you do not, read onward.

1. Download get-pip.py(https://bootstrap.pypa.io/get-pip.py) to a folder on your computer.
2. Open a command prompt and navigate to the folder containing get-pip.py.
3. Run the following command:
```
python get-pip.py
```
4. Pip is now installed!


__pandas, matplotlib and xlrd:__

```
pip install pandas matplotlib xlrd
```

## Running the program

Now you can double-click the .bat file and this window should pop up:
![Initial State of the Program](/ScreenShots/InitialsState.PNG?raw=true "Initial State")

After testing one of the files:
![Running State of the Program](/ScreenShots/RunningState.PNG?raw=true "Running State")

## Built With

* [Tkinter](https://docs.python.org/2/library/tkinter.html) - Tkinter is Python's de-facto standard GUI (Graphical User Interface) package

## Developers

* **Omar AlQaisi**     - [OmarQaisi](https://github.com/OmarQaisi)
* **Marwan AlRamahi**  - [Marwan998](https://github.com/Marwan998)
* **Motassem Naqawah** - [moenaqawah](https://github.com/moenaqawah)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
