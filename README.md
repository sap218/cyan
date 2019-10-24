# cyannotator

<img src="cyan.png" align="right" alt="cyan annotate logo" width="200">

Introducing `cyan` - an annotator for plain text files using a list of words/concepts.

Please **note**: as I am not an expert, the script may not work as expected. 

Author __Samantha C Pendleton__, [Twitter](https://twitter.com/sap218) & [GitHub](https://github.com/sap218) | **Python v3.5**

## Installation

**Prerequisite**

`$ sudo pip3 install re`

`$ sudo pip3 install click`

**GitClone**

`$ git clone https://github.com/sap218/cyan.git`

**Set Up**

`$ sudo python3 setup.py install` 

## Running

```
$ cyan -file yourtextinput.txt -lists yourconcepts.txt
```

**Help**

`$ cyan --help`

```
Usage: cyan.py [OPTIONS]

Options:
  --file TEXT   Text file.
  --lists TEXT  List of words.
  --help        Show this message and exit.
```

**Running the example**

`$ cd example` 

`$ cyan -file test_text.txt -lists test_words.txt`

## Thank you! :abcd:

Don't hesitate to create an issue or make a suggestion!

###### Todo List
- [x] Set-up repository
- [x] Improve code
- [ ] Fix minor issue with special chars
