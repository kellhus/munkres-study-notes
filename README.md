This is a repository for the participants of the topology study group at [/r/GroupStudy](http://www.reddit.com/r/GroupStudy/comments/37bxf0/) using the 2nd edition of *Topology* by James Munkres.

### Table of Contents
**[Software Prerequisites](#software-prerequisites)**  
**[Using the Software](#using-the-software)**  
**[Using the Issue Tracker](#using-the-issue-tracker)**  
**[Guidelines](#guidelines)**  


## Software Prerequisites

You will need the following:

* Register an account with GitHub;
* Set up the Git version control system to pull/push changes from/to the repository to/from your local computer. See the [GitHub help pages](https://help.github.com/articles/set-up-git/) for instructions;
    - A temporary alternative to the above -- until you have figured `git` out -- would be to edit the markdown files via the GitHub web interface and to copy-and-paste the relevant snippets into a web-based markdown editor such as [StackEdit](https://stackedit.io/) for preview.

* Optionally, if you are planning to convert the pandoc markdown files into PDF on your own computer:
    - Install the universal document converter [pandoc](http://pandoc.org/); 
    - Install a TeX distribution such as [MikTex](http://miktex.org/) for pandoc to use;
    - Install Python to use the Python script `convert.py` that takes care of collating multiple markdown files into a single one and calling pandoc to deal with it.
* Optionally, if you use Google Chrome and want to enable MathJax for the rendering of the TeX parts of the markdown files in the GitHub web interface, try [this extension](https://chrome.google.com/webstore/detail/tex-all-the-things/cbimabofgmfdkicghcadidpemeenbffn). Then inline TeX snippets should render like this:

![screenshot of TeX the World extension in action](https://raw.githubusercontent.com/kellhus/munkres-study-notes/master/assets/chrome-mathjax-example.png)


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

If the remote repository has been updated by someone else while you were working on your local copy, you will need to do the following instead (barring exceptional circumstances such as conflicting commits). This will take care of fetching the remote changes and merging them with your local changes -- so, if the remote repository has a solution to an exercise, and your local copy has a solution to another exercise, then `git pull` should take care of that and update your local copy to have both solutions.

```
git add .
git commit -m "Describe the nature of your edits here"
git pull
git push
```

### Markdown to PDF
A Python script is provided that takes care of combining the markdown files and invoking the pandoc converter on the combined file. Simply open the command line in `munkres-study-notes` and call:

```
python convert.py Munkres
```

## Using the Issue Tracker

The [issue tracker](https://github.com/kellhus/munkres-study-notes/issues) can be used for requesting clarification from more knowledgeable participants on any issues that might arise, be they unclear wording in the text, unsufficient motivation of theorems or definitions, or problems with exercises. If you know the solution to an issue, make suitable changes to the markdown files. The issues can also be discussed in the process. An example issue is available [here](https://github.com/kellhus/munkres-study-notes/issues/1).

The issues can be classified using labels for easy lookup. The labels are intended as follows:

* **organizational**: for discussion concerning the group-study process;
* **question**: for specific questions about passages in the text or exercises;
* **mistake**: if you see something in someone else's solution or explanation that might be a mistake, open an issue and label it as such;
* **help wanted**: in case you plan to write a section explaining some theorem, but need proofreading or are not sure you can pull it off alone;
* **bug**: for drawing attention to bugs in the Python script or problems with other associated software.

## Guidelines

### General

* Don't be afraid to modify any files in the repository. The version control should track all changes, and reverts can be made if necessary.
* Not to put too fine a point on it, but use the issue tracker for any organizational or academic questions and / or discussion. No, seriously. :-)
* At the end of our work, the end product should be a nice, tidy set of notes and solutions that reflects any and all questions we had in studying the textbook. And, of course, a PDF file we can save onto our hard drives to remember the experience by.

### Editing the Markdown Files

* End each sentence with a new line. This guideline is motivated by the nature of the Git versioning control system, which tracks the lines, not the words or sentences in individual lines.
* The notation `Theorem (Exercise, Example, Lemma) 3.12.1` refers to Chapter 3, Section 12, Theorem (Exercise, Example, Lemma) 1.
* Use `### Comment on Lemma 2.5.4` to add commentary to the respective theorem or lemma.
* Use `### Exercise 1.12.5` to add a solution to an exercise.
* Use `### Freestyle Heading` to add something that does not fall into the above categories.
* Follow the structure of the book. That is, don't put Exercise 2.10.3 before Exercise 2.10.1 in the markdown file for Section 10.

### Academic Integrity

Of course the point of the study group is to learn and that requires doing the work yourself.  We will be putting together the solutions to problems and notes in the main branch, so you shouldn't look at the relevant sections until you've tried the problems yourself in order to avoid "spoilers".  If you just want discussion, clarification, or a little hint or push in the right direction, create an issue using the black plus sign at the top-right of the page, and label it according to the labelling conventions described above.  

<<<<<<< HEAD
=======
>>>>>>> 8460faa0c2cb97668ca16675eceae25483bdcff6
