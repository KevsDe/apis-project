![img](Input/banner.png)

# Objective of this project: getting and shaping information in order to return results related to the user input parameters.

Information sources:
* [Kaggle link](https://www.kaggle.com/gulsahdemiryurek/harry-potter-dataset?select=Characters.csv)
* [Api link](https://www.potterapi.com/)
* [Web scraped](https://harrypotter.fandom.com/)

For this project I used:
Libraries:
* Pandas
* Numpy
* Regex
* Matplotlib
* Seaborn
* Requests
* Dotenv
* bs4
* Sys
* Argparse
* In adittion to functions that I created during the whole process.

## Summary
For this project my objective was enhance the content of a data set, obtaining more information from an api and web scraping in order to return valuable information to the user based on the input parameters, this project is based in the Harry Potter Universe. 
* Valid character parameters : 'Aberforth Dumbledore', 'Alastor Moody', 'Albus Dumbledore', 'Alecto Carrow', 'Alice Longbottom', 'Alicia Spinnet', 'Amos Diggory', 'Amycus Carrow', 'Angelina Johnson', 'Anthony Goldstein', 'Antonin Dolohov', 'Argus Filch', 'Arthur Weasley', 'Aurora Sinistra', 'Bellatrix Lestrange', 'Blaise Zabini', 'Bloody Baron', 'Cedric Diggory', 'Charity Burbage', 'Charles Weasley', 'Cho Chang', 'Colin Creevey', 'Corban Yaxley', 'Cornelius Fudge', 'Cuthbert Binns', 'Dean Thomas', 'Dedalus Diggle', 'Dennis Creevey', 'Dobby', 'Dolores Umbridge', 'Draco Malfoy', 'Dudley Dursley', 'Elphias Doge', 'Emmeline Vance', 'Ernest Macmillan', 'Fat Friar', 'Fenrir Greyback', 'Filius Flitwick', 'Firenze', 'Fleur Delacour', 'Frank Longbottom', 'Fred Weasley', 'Gabrielle Delacour', 'Garrick Ollivander', 'Gellert Grindelwald', 'George Weasley', 'Gilderoy Lockhart', 'Ginevra Weasley', 'Godric Gryffindor', 'Gregory Goyle', 'Hannah Abbott', 'Harry Potter', 'Helena Ravenclaw', 'Helga Hufflepuff', 'Hermione Granger', 'Horace Slughorn', 'Igor Karkaroff', 'Irma Pince', 'James Potter I', 'Justin Finch-Fletchley', 'Katie Bell', 'Kingsley Shacklebolt', 'Kreacher', 'Lavender Brown', 'Lee Jordan', 'Lily J. Potter', 'Lucius Malfoy', 'Luna Lovegood', 'Marcus Flint', 'Marietta Edgecombe', 'Michael Corner', 'Millicent Bulstrode', 'Minerva McGonagall', 'Molly Weasley', 'Mundungus Fletcher', 'Narcissa Malfoy', 'Neville Longbottom', 'Nymphadora Tonks', 'Oliver Wood', 'Padma Patil', 'Pansy Parkinson', 'Parvati Patil', 'Penelope Clearwater', 'Percy Weasley', 'Peter Pettigrew', 'Petunia Dursley', 'Pomona Sprout', 'Poppy Pomfrey', 'Quirinus Quirrell', 'Regulus Black', 'Remus Lupin', 'Rodolphus Lestrange', 'Rolanda Hooch', 'Romilda Vane', 'Ronald Weasley', 'Rowena Ravenclaw', 'Rubeus Hagrid', 'Rufus Scrimgeour', 'Salazar Slytherin', 'Seamus Finnigan', 'Septima Vector', 'Severus Snape', 'Sirius Black', 'Sturgis Podmore', 'Susan Bones', 'Sybill Trelawney', 'Terry Boot', 'Theodore Nott', 'Tom Riddle', 'Vernon Dursley', 'Viktor Krum', 'Vincent Crabbe', 'Walden Macnair', 'Wilhelmina Grubbly-Plank', 'Zacharias Smith'.
* Valid house parameters : 'Gryffindor','Slytherin','Ravenclaw','Hufflepuff'.
* Valid faction parameters : 'Dumbledores_Army','Death_Eater','Ministry_Of_Magic','Order_Of_The_Phoenix'.
* Valid gender parameters : 'Male','Fermale','Unknown'

## Files
* Data_set_Api_Call_Web_Scraping.ipynb: processing the data set, api and web scraping.
* Main.py: executable program.
* src: directory with functions files. 


## Thanks 
Thanks for reading and for been interested in this rookie project.
