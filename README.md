This is a repository for the participants of the topology study group at [/r/GroupStudy](http://www.reddit.com/r/GroupStudy/comments/37bxf0/) using the 2nd edition of *Topology* by James Munkres.

### Table of Contents
**[Software Prerequisites](#software-prerequisites)**  
**[Using the Software](#using-the-software)**  
**[General Guidelines](#general-guidelines)**  


## Software Prerequisites

You will need the following:

* Register an account with GitHub;
* Set up the Git version control system to pull/push changes from/to the repository to/from your local computer. See the [GitHub help pages](https://help.github.com/articles/set-up-git/) for instructions;
    - An alternative to the above would be to edit the markdown files via the GitHub web interface and to copy-and-paste the relevant snippets into a web-based markdown editor such as [StackEdit](https://stackedit.io/) for preview;
* Optionally, if you are planning to convert the pandoc markdown files into PDF on your own computer:
    - Install the document converter [pandoc](http://pandoc.org/); 
    - Install a TeX distribution such as [MikTex](http://miktex.org/) for pandoc to call;
    - Install Python to use the Python script `convert.py` that takes care of collating multiple markdown files into a single one and calling pandoc to deal with it.


## Using the Software

### Git

First you will need to clone the repository onto your local computer. Open the command line in a directory of your choice and invoke the following:

```
git clone https://github.com/kellhus/munkres-study-notes.git
```

Once you have a copy of the repository, you can make changes to it locally. Open the markdown files in a text editor of your choice and edit them. When you are satisfied with your work, push the changes into the remote (GitHub) repository by opening the command line in the `munkres-study-notes` directory and typing the following:

```
git add .
git commit -m "Describe the nature of your edits here"
git push
```

If the remote repository has been updated by someone else while you were working on your local copy, you will need to do the following instead:

```
git pull
git add .
git commit -m "Describe the nature of your edits here"
git push
```

### Markdown to PDF
A Python script is provided that takes care of combining the markdown files and invoking the pandoc converter on the combined file. Simply open the command line in `munkres-study-notes` and call:

```
python convert.py Munkres
```

## Use the Issue Tracker
The [issue tracker](https://github.com/kellhus/munkres-study-notes/issues) can be used for requesting clarification from more knowledgeable participants on any issues that might arise, be they unclear wording in the text, unsufficient motivation of theorems or definitions, or problems with exercises. If you know the solution to an issue, make suitable changes to the markdown files and close the issue. The issues can also be discussed in the process. An example issue is available [here](https://github.com/kellhus/munkres-study-notes/issues/1).

## General Guidelines

The notation `3.12.1` refers to Chapter 3, Section 12, Theorem / Exercise / Lemma 1. Use `### Comment on Lemma 2.5.4` to add commentary to the respective theorem or lemma. Use `### Exercise 1.12.5` to add a solution to an exercise. Use `### Freestyle Heading` to add something that does not fall into the above categories.
