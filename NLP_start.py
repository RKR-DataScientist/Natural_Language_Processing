# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import nltk
nltk.download()

paragraph = """On Good Friday, April 14, 1865, the Lincolns attended a play 
entitled Our American Cousin at Ford's Theater. During the 
performance, John Wilkes Booth arrived at the theater, entered 
the State Box from the rear, and shot the president in the back
 of his head at about 10:15 P.M. Lincoln was carried across the
 street to the Petersen House where he passed away the next day
 at 7:22 A.M. This was the first presidential assassination in
 American history, and the nation mourned the loss of its leader. 
His death was the result of the deep divisions and hatreds of the
 times. Lincoln's body was taken to Springfield by train, and he 
was buried in the Lincoln Tomb in Oak Ridge Cemetery on May 4, 1865. 
Because of the assassination, Reconstruction took place without Lincoln's 
guidance and leadership."""

# Tokenization Sentences
sentences = nltk.sent_tokenize(paragraph)

# Tokenization Words
words = nltk.word_tokenize(paragraph)