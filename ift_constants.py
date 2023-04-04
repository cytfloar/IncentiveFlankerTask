INST1_MRI = """
In this task, you will see 5 letters at a time. On each trial, one of the middle letters will be different from the others. 

If the different letter is “S” or “K”, press your right index finger
If the different letter is “C” or “H”, press your right middle finger. 

For example, if you see the letters SSKSS, press your right index finger. 
If you see letters KCKKK, press your right middle finger.

Press your middle finger to continue.
"""

INST1 = """
In this task, you will see 5 letters at a time. On each trial, one of the middle letters will be different from the others. 

If the different letter is “S” or “K”, press “7” with your right hand. 
If the different letter is “C” or “H”, press “2” with your left hand.

For example, 
if you see the letters SSKSS, press “7” on the keyboard. 
If you see letters KCKKK, press “2” on the keyboard.

Press the spacebar to continue. 
"""

INST2_MRI = """If you press the CORRECT key, five white stars will appear. 
If you press the INCORRECT button or do not make a response in time, five red stars will appear. 

Press your middle finger to continue.
"""
INST2 = """If you press the CORRECT key, five white stars will appear. 
If you press the INCORRECT key or do not make a response in time, five red stars will appear. 

Press the spacebar to continue.

"""
INST3 = """On some of the trials (“incentive trials”), you will have the opportunity to win money if you make a correct response, 
or you will lose money if you make an incorrect response. 

“Incentive trials” will begin with a picture of a “thumbs up” 
and the amount that you can win or lose. 
"""

INST4 = """For example, if you see this picture: 
it means that on the next trial, 
if you make the correct response, you will WIN 25 cents, 
but if you make an incorrect response, or do not make a response quickly enough, you will LOSE 25 cents. 
"""

INST5 = """On the remaining trials (“neutral trials”), 
you will not earn or lose money, regardless of your response. 
“Neutral trials” will begin with a picture of thumbs out to the side, 
labeled with “0” cents. 
"""

INST6 = """For example, if you see this picture: 
It means that on the next trial, 
you will not win or lose any money, 
regardless of what response you make.
"""

INST_MRI = """
Remember!

Identify the letters that is different from the other 4 letters
For:
‘S’ or ‘K’ press your right INDEX FINGER
‘H’ or ‘C’ press your right MIDDLE FINGER

With 'Thumbs-up', 
you WIN the Incentive Value for every CORRECT answer
you LOSE the Incenive Value for every WRONG answer

For a neutral thumb position you neither gain nor lose!

You current balance is: $%.2f

Ready to start? Press your middle finger to continue.
"""

INST = """ 
Remember!

Identify the letters that is different from the other 4 letters
For:
'S' or 'K' press “2”; 'H' or 'C' press "7"

With 'Thumbs-up', 
you WIN the Incentive Value for every CORRECT answer
you LOSE the Incenive Value for every WRONG answer

For a neutral thumb position you neither gain nor lose!

You current balance is: $%.2f

Ready to start? Press space to continue.
"""

START = """ The task is about to begin.

Get ready...
"""
RESULT = """ You have completed %s

Correct Answers: %d
Wrong Answers: %d (%dO, %dC)

Money Gained: $%.2f
Money Lost: $%.2f

Total money you made during %s: $%.2f

Your Final Balance: $%.2f

Please wait for the task to continue. 

"""

