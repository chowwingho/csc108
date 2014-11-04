csc108
======
CSC108H Assignment 2

Due Date: Tuesday 4 November 2014 by 9:00pm

Authorship Detection

Automated authorship detection is the process of using a computer program to analyze a large collection of texts, one of which has an unknown author, and making guesses about the author of that unattributed text. The basic idea is to use different statistics from the text -- called "features" in the machine learning community -- to form a linguistic "signature" for each text. One example of a simple feature is the number of words per sentence. Some authors may prefer short sentences while others tend to write sentences that go on and on with lots and lots of words and are not very concise, just like this one. Once we have calculated the signatures of two different texts we can determine their similarity and calculate a likelihood that they were written by the same person.

Automated authorship detection has uses in plagiarism detection, email-filtering, social-science research, and as forensic evidence in court cases. Also called authorship attribution, this is a current research field and the state-of-the-art linguistic features are considerably more complicated than the five simple features that we will use for our program. But even with our very basic features and simplifications, your program may still be able to make some reasonable predictions about authorship.

Starter Code: author_functions.py, author_program.py

We have begun a program that guesses the author of a text file by comparing its signature to a given set of linguistic signatures. Download the starter code author_functions.py and author_program.py. (Be sure to right-click on the links in your browser so that you can use "Save Link as..." rather than copying and pasting the code.) Once the files are set-up according to the steps below, author_program.py runs, but does almost nothing, because many of the functions' bodies are incomplete. Your task is to finish the incomplete functions in both files, as well as to add and use appropriate helper functions.

An Overview: How the program works

The program begins by asking the user for two strings: the first is the name of a file of text whose authorship is unknown (the mystery file) and the second is the name of a directory where each file in that directory contains the linguistic signature for one file of text. Note that a directory and folder are two words for the same thing.

The program calculates the linguistic signature for the mystery file and then calculates scores indicating how well the mystery file matches each signature file in the directory. The author from the signature file that best matches the mystery file is reported as the most likely author of the text in the mystery file.

Definitions: What is a token, word, sentence, and phrase?

For the purposes of this assignment, here are a few definitions:

If you call the str method split on a line from a file, you get a list of strings back. Each string in that list is a called a token.
Here is help(str.split):

S.split([sep]) -> list of str

        Return a list of the tokens in S, using string sep as the 
        separator. If sep is not specified, any whitespace string
        is a separator and empty strings are removed from the result.
    
A word is a non-empty token from the file that isn't completely made up of punctuation.
You'll find the words in a file by using split to get the tokens and then removing the punctuation from the beginning and end of the tokens using the helper function clean_up that we provided in author_functions.py. If calling clean_up results in an empty string, then that empty string isn't considered a word. Notice that clean_up also converts the string to lowercase. This means that the cleaned up versions of 'yes', 'Yes' and 'YES!' will all be the same word. Words may contain inner punctuation; for example, "it's" is a word with a length of 4 and 'hard-and-fast' is a word with a length of 13.
A sentence is a string that:
is followed by (but doesn't include) the terminator characters ! ? . or the end of the file,
excludes whitespace on either end, and
is not empty.
Consider this file. Remember that a file is just a linear sequence of characters, even though it may look two dimensional. This file contains these characters:

            this is the\nfirst sentence. Isn't\nit? Yes ! !! This \n\nlast bit :) is also a sentence, but \nwithout a terminator other than the end of the file\n
        
By our definition, there are four sentences in the file:
Sentence 1	
"this is the\nfirst sentence"
Sentence 2	
"Isn't\nit"
Sentence 3	
"Yes"
Sentence 4	
"This \n\nlast bit :) is also a sentence, but \nwithout a terminator other than the end of the file"
Notice that:

The sentences do not include their terminator character.
The last sentence was not terminated by a character; it finishes with the end of the file.
Sentences can span multiple lines of the file.
A phrase is a non-empty section of a sentence that is separated by colons, commas, or semi-colons. The previous sentence (the one before this one) has three phrases by our definition. This sentence (the one you are reading right now) has only one. This is because we don't separate phrases based on parentheses.
We realize that these are not the usual definitions for sentences, words, or phrases, but using them here will make the assignment easier. More importantly, it will make your results match what we are expecting when we test your code. You may not modify these definitions, because if you do, your assignment will be marked as incorrect.

Completing author_functions.py

In author_functions.py, you must implement five required functions to calculate various linguistic features and a required function to compare authors based on these linguistic features. In addition, you must add some helper functions (one required, plus others that you choose to add) to aid with the implementation of these functions. In addition to the descriptions below, please see the docstring descriptions provided in the starter code. Add a second example function call to each of the given docstring descriptions in author_functions.py.

Function name:
(Parameter types) -> Return type	Description
avg_word_length:
(list of str) -> float	
The first linguistic feature is simply the average number of characters per word, calculated after the punctuation has been stripped using the already-written clean_up function. In the sentence prior to this one, the average word length is 6.04. Notice that the comma and the final period are stripped but the hyphen inside "already-written" and the underscore in "clean_up" are both counted.

type_token_ratio:
(list of str) -> float	
The second linguistic feature, the Type-Token Ratio, is the number of different words used in a text divided by the total number of words in that text. (This feature is a measure of the repetitiveness of the vocabulary.) Again you must use the provided clean_up function so that "this","This","this," and "(this" are considered the same and are not counted as different words.

hapax_legomena_ratio:
(list of str) -> float	
The third linguistic feature, the Hapax Legomena Ratio, is similar to Type-Token Ratio in that it is a ratio that uses the total number of words as the denominator. The numerator for the Hapax Legomena Ratio is the number of words that occur exactly once in the text. In your code for this function you must not use a Python dictionary (even if you have already learned about them on your own or are reading ahead in class) or any other technique that keeps a count of the frequency of each word in the text. Instead, use this approach: As you read the file, keep two lists. The first contains all the words that have appeared at least once in the text and the second has all the words that have appeared at least twice in the text. Of course, the words on the second list must also appear on the first. Once you've read the whole text, you can use the two lists to calculate the number of words that appeared exactly once.

Note: you will be marked not only on correctness, but also on whether you follow the approach specified above.

split_on_separators:
(str, str) -> list of str	
This is a helper function. Several features require the program to split a string on any of a set of different separators, and this function will be used to do that.

Test this function carefully on its own before trying to use it in your other functions.

avg_sentence_length:
(list of str) -> float	
The fourth linguistic feature your code will calculate is the average number of words per sentence.

Tip: Sentences can span multiple lines. Rather than work with the given list of str (list of lines), start by creating a single huge string containing all of the strings, in order, from the list of lines. Next, call function split_on_separators on that huge string.

avg_sentence_complexity:
(list of str) -> float	
The final linguistic feature is sentence complexity, which is measured by the average number of phrases per sentence. We will find the phrases by taking each sentence, as defined above, and splitting it on any of colon, semi-colon, or comma.

Tip: Sentences can span multiple lines. Rather than work with the given list of str (list of lines), start by creating a single huge string containing all of the strings, in order, from the list of lines. Next, call function split_on_separators on that huge string.

compare_signatures:
(list, list, list of float) -> float	
Signature Files

We have created a set of signature files for you to use that have a fixed format. The first line of each file is the name of the author and the next five lines each contain a single float number. These are values for the five linguistic features in the following order:

Average Word Length
Type-Token Ratio
Hapax Legomena Ratio
Average Sentence Length
Average Sentence Complexity
You are welcome to create additional signature files for testing your code and for fun, but you must not change this format. Our testing of your program will depend on its ability to read the required signature-file format.
Determining the best match

To determine the best match between an unattributed text and the known signatures, the program uses the function compare_signatures, which calculates and returns a measure of the similarity of two linguistic signatures. You could imagine developing some complicated schemes, but our program will do almost the simplest thing imaginable. The similarity of signatures a and b will be calculated as the sum of the absolute differences on each feature, but with each difference multiplied by a "weight" so that the influence of each feature on the total score can be controlled. In other words, the similarity of signatures a and b (Sab) is the sum over all five features of: the absolute value of the feature difference times the corresponding weight for that feature. The equation below expresses this definition mathematically: 

 

where fi,x is the value of feature i in signature x and wi is the weight associated with feature i.

The example below illustrates this calculation. Each row concerns one of the five features. Suppose signature 1 and signature 2 are as shown in columns 2 and 3, and the features are weighted as shown in column 4. The final column shows the contribution of each feature to the overall sum, which is 12.0. 12.0 represents the similarity of signatures 1 and 2.

Feature number	Value of feature in signature 1	Value of feature in signature 2	Weight of feature	Contribution of this feature to the sum
1	4.4	4.3	11	abs(4.4 - 4.3) * 11 ➡ 1.1
2	0.1	0.1	33	abs(0.1 - 0.1) * 33 ➡ 0
3	0.05	0.04	50	abs(0.05 - 0.04) * 50 ➡ .5
4	10	16	0.4	abs(10-16) * 0.4 ➡ 2.4
5	2	4	4	abs(2 - 4) * 4 ➡ 8
SUM				12.0 

(Note: in Python, the floating-point result is reported as 12.000000000000007.)
Notice that if signatures 1 and 2 were exactly the same on every feature, the similarity would add up to zero. (It may have made sense to call this "difference" rather than similarity.) Notice also that if they are different on a feature that is weighted higher, their overall similarity value goes up more than if they are different on a feature with a low weight. This is how weights can be used to tune the importance of different features.

Completing author_program.py

In author_program.py, you must implement two required functions. For functions that involve reading from files or user input (e.g., the two functions described below), do not include example calls in the docstring descriptions.

Function name:
(Parameter types) -> Return type	Description
get_valid_filename:
(str) -> str	
See docstring description in author_program.py. Do not use for loops, or this function will receive a mark of zero. Use a while loop.

To determine whether a file exists, use the function os.path.exists. Function os.path.exists takes a string argument representing the name of a file and returns a Boolean to indicate whether the file exists.

The help for os.path.exists mentions passing it a path (which is a description of the file and where it exists among all your directories), but if you give it a string that is simply a file name, it will check in the directory in which your code is running.

get_valid_directory_name:
(str) -> str	
See docstring description in author_program.py. Do not use for loops, or this function will receive a mark of zero. Use a while loop.

Use the function os.path.isdir to check whether a string is a valid directory.

Additional requirements

Do not change any of the existing code. Read the comments and add your code in the places specified by the comments.
Do not round any floating point numbers.
Do not use type dict.
Do not add any user input or output, except where you are explicitly told to. In those cases, we have provided the exact print or input call to use. Do not modify these.
In particular, in author_functions.py, never call print or input. Doing so will cause all tests to fail.
Functions get_valid_filename and get_valid_directory_name must not use any for loops, or they will receive a mark of zero. The purpose of this is to have you practice while loops.
You must not use any break or continue statements. Any functions that do will receive a mark of zero. We are imposing this restriction (and we have not even taught you these statements) because they are very easy to "abuse," resulting in terrible code.
How to tackle this assignment

This program is much larger than what you wrote for Assignment 1, so you'll need a good strategy for how to tackle it. Here is our suggestion.

Principles:

To avoid getting overwhelmed, deal with one function at a time. Start with functions that don't call any other functions; this will allow you to test them right away. The steps listed below give you a reasonable order in which to write the functions.
For each function that you write, start by adding at least one example call to the docstring before you write the function.
Keep in mind throughout that any function you have might be a useful helper for another function. Part of your marks will be for taking advantage of opportunities to call an existing function.
As you write each function, begin by designing it in English, using only a few sentences. If your design is longer than that, shorten it by describing the steps at a higher level that leaves out some of the details. When you translate your design into Python, look for steps that are described at such a high level that they don't translate directly into Python. Design a helper function for each of these, and put a call to the helpers into your code. Don't forget to write a great docstring for each helper!
Steps:

Here is a good order in which to solve the pieces of this assignment.
Read this handout thoroughly and carefully, making sure you understand everything in it, particularly the different linguistic features.
Read the starter code to get an overview of what you will be writing. It is not necessary at this point to understand every detail of the functions we have provided.
Complete author_functions.py: add example(s) to the docstring, implement, and test the functions in this order:
avg_word_length
type_token_ratio
hapax_legomena_ratio
split_on_separators
avg_sentence_length. Begin by writing code to obtain a list of sentences from the text. Test that this part of your code works correctly before you worry about calculating the average sentence length.
avg_sentence_complexity
compare_signatures
Now you have implemented all the functions in author_functions.py. Run our a2_self_test.py program (see Testing your code) to confirm that your code passes our most basic tests. Correct any errors that this uncovers.
Complete author_program.py: implement and test these functions (note: do not add examples to the docstring, since these two functions involve user input):
get_valid_filename
get_valid_directory_name
You are now ready to run the full author detection program: run author_program.py. To do this you will need to set up a directory that contains only valid linguistic signature files. We are providing a set of these on the data files page. You'll also want some mystery text files to analyze. We have put a number of these on the data files page. If you are copying them to your home machine, don't put them in the same directory as the linguistic signature files.
Testing your code

We are providing a program called a2_self_test.py that imports your author_functions.py and checks that the required functions in that file satisfy some of the basic requirements. (It does not check get_valid_filename and get_valid_directory_name in author_program.py.)

When you run a2_self_test.py, it should produce no errors and its output should consist only of one thing: the word "okay". If there is any other output at all, or if any input is required from the user, then your code is not following the assignment specifications correctly and will be marked as incorrect. Go back and fix the error(s).

While you are playing with your program, you may want to use the signature files and mystery text files we have provided. This in conjunction with a2_self_test.py is still not sufficient testing to thoroughly test all of your functions under all possible conditions. With the functions on this assignment, there are many more possible cases to test (and cases where your code could go wrong). If you want to get a great mark on the correctness of your functions, do a great job of testing them under all possible conditions. Then we won't be able to find any errors that you haven't already fixed!

Marking

These are the aspects of your work that we will focus on in the marking:

Correctness: Your code should perform as specified. Correctness, as measured by our tests, will count for the largest single portion of your marks.

Docstrings: For each function that you design from scratch, write a good docstring. Do not change the docstrings that we have already written for you, except to add another example or two. Make sure that you read the Python style guidelines page for some important rules and guidelines about docstrings.

Internal comments: Within functions, the more complicated parts of your code should also be described using internal comments. For this assignment, internal comments will be more important than on Assignment 1.

Programming style: Your variable names should be meaningful and your code as simple and clear as possible.

Good use of helper functions: If you find yourself repeating a task, you should add a helper function and call that function instead of duplicating the code. And if a function body is more than about 20 lines long, introduce helper functions to do some of the work -- even if they will only be called once.
Formatting style: Make sure that you read the Python style guidelines page for some important rules and guidelines about formatting your code.

Submitting your assignment

You must hand in your work electronically, using the MarkUs online system. Instructions for doing so are posted on the Assignments page of the course website.

The very last thing you do before submitting should be to run a2_self_test.py one last time. Otherwise, you could make a small error in your final changes before submitting that causes your code to receive zero for correctness.

For this assignment, hand in two files:

author_functions.py
author_program.py
Once you have submitted, be sure to check that you have submitted the correct version; new or missing files will not be accepted after the due date. Remember that spelling of filenames, including case, counts. If your files are not named exactly as above, your code will receive zero for correctness.

Future Work

If you carefully examine the mystery files and correctly code up your assignment, you'll see that it correctly classifies many of the documents -- but not all. Some of the linguistic features that we have used (type-token ratio and hapax legomena ratio in particular) are standard techniques, but they may not be sufficient to do the classification task. There are other standard features and more sophisticated techniques that were too complicated for this assignment. Suppose you could use a Python dictionary to keep a count of how many times each word appeared in a document. What new linguistic features would that allow you to use? Some authors like to use lots of exclamation marks!!! or perhaps just a lot of punctuation?! Could you devise a linguistic feature to measure this? While this is fun to think about, do not add any different linguistic features to the version of the program that you submit for marking.

Another area for thought is how authorship attribution is related to plagiarism detection. In this TIME magazine article, plagiarism detection software is used to support the claim that Shakespeare was the author of an unattributed play.

In the field of machine learning (of which authorship detection is a subfield), programs often learn their own configuration values through training. In our case, could the program learn from trying to guess an author and then being told the right answer? Could it learn to adjust the weights being applied to the different features? What about learning a new feature? How would you do this?

Anticipated FAQs

How do I run author_program.py? Where do I save the files?
To begin, save the mystery files in the same directory as your author_functions.py and author_program.py files.
In that directory, create another directory for the signature files (e.g., call it signature_files). Save the .stats files in that new signature_files directory. Don't put anything else in that directory.
Next, run author_program.py.
When prompted to enter a filename, enter one of the mystery filenames (e.g., mystery1.txt).
When prompted to enter a directory, enter the name of the directory that contains the signature files (e.g., signature_files).
Can I define my own helper functions?

Yes. In fact, to earn full marks, you must write your own helper functions! See the marking scheme section of this handout.

My code takes a long time to run. Is that okay?
That depends. It is important to determine whether your code is working properly or whether there is some sort of problem with it. It is okay for your program to take a couple of minutes on the large mystery files. We'll be doing our automated testing with smaller data sets.

However, your code may have a problem such as an infinite loop, or it may be very inefficient. If that is the case, use the debugger to try to identify which function is taking a long time to execute.

Consider also whether the problem could have been solved in a simpler way. For example, if the program reads the text 20 times to reach a conclusion and it could reach the same conclusion by just reading the text once, the second approach is preferable. If the text is small you might not be able to tell the difference, but the longer the text gets, then the more pronounced the difference will be.

Will a correctly coded program successfully detect the authors for all mystery files?
Assuming your code is correct, it will be able to correctly detect the authors for all the provided mystery files except one. Of course, do not just rely on this to ensure the correctness of your code. Make sure you run detailed tests for every function you write.
