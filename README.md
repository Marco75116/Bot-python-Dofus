# Bot-python-Dofus #RPA

I used the following libraries : pytesseract,pytautogui,PIL(Image,ImageGrab),time

This program is a robotic process automation of an activity of the Dofus game: "Forgemagie". 
Forgemagie is time consuming, punctuated by repetitive tasks requiring "complex" analysis / decision.
I decided to make this bot to save time, to save plying pleasure and my desire to program made me open pycharm.

Here are the steps of how this program works.
First I used pillow to screen the part of the screen that interested me whose data I wanted to process, like the images below.

![cazcherligne2](https://user-images.githubusercontent.com/83420479/145916491-c6963c34-fbe7-41fe-ac55-a2835a002014.png)
![190110120938748285](https://user-images.githubusercontent.com/83420479/145916443-8713b636-c812-4e90-bfd6-ba278e67f6b5.png)

Then pytesseract helped me to extract the data into a string. I cleaned the string to keep only numbers that i will identify and reorganize in a precise order into a tab.
From this tab the program with Pyautogui executes the exactly the optimized number of mouse clicks.
I do an infinite loop on these steps because there is a part of randomness in Forgemagie.


In reality, the program did not work all the time. The sizes and order of data caused bugs. Pytesseract has various interpretations,numbers become letters,letters become punctuations etc ... So I ran the program and fixed all the bugs until I had a program that worked every time!
