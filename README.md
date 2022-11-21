# 6G-Assessment
Dear 6G,

This is what I came up with for your assessment.
I tried to show as many different things as I could
such as f-strings, typing, etc. Though there are a lot more things that I know are possible in Python3 such as list-comprehensions,
walrus-operators and one-line if-else statements. I hope you will be satisfied with my solution.

## Obstacles
I ran into a couple of obstacles while writing this program. For example, the assignment tells me that compensation is paid on a montly
basis. Does this tell me that I can assume that there are always exactly four weeks in a month? I decided to make two extra functions just
to make sure that someone doesn't get extra compensation for a month, because the month starts on a Thursday and ends on a Wednesday.

The amount of workdays was also a bit vague, since I don't know which day people work, so I assumed that - becuse people don't work for more
than five days - people always start work on Monday. That means that if they only work three days per week, that they'll work on Monday,
Tuesday and Wednesday. I also had slight bit of trouble interpreting if one person works four and a half days, or sometimes four, sometimes
five days. But I just assumed that they worked four and a half days.

Last but not the smallest struggle I had was about the assignment telling me to create an overview **for the current year**. This sentence
clashed a bit with another sentence telling me that the output should only have a column "for the entire month". Does that mean
that I have to create twelve different columns for each month? That'd be really messy in my opinion, so I made it that a report does specify
in which month it is for. (You can also change the date to something else manually, but you'll have to dig into the code for that).


## How to run
First of all you'll need to clone this repository to your local/virtual machine with a `git pull` command.

Once the project is on your machine, you'll need to install dependencies (preferably in a new virtual environment). Do this with:
```
pip install -r requirements.txt
```

After that you're ready to go ahead and run `main.py`. Once the script has completed its work, you'll see a new file in `data/employee_data_compensation.csv`.
```
python main.py
```