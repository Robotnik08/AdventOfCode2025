# Advent of code 2025

This is my repository for the Advent of Code 2024. I will be solving the puzzles in [Dosato](https://github.com/Robotnik08/cdosato).
<br>

## Context

Dosato is a programming language that I created. It is a unique and robust intepreted language designed for the general purpose. It is a high-level language that is easy to learn and use. This is one of the main reasons why I chose to use Dosato for solving the Advent of Code puzzles.

### Why Dosato?

I like it :P, it's really not a bad language for this and I barely get any extra challenges from the language itself. It is also just cool to solve these puzzles in a language that I created myself.

## How to run the code

To run the code, you will need to have the Dosato interpreter installed on your machine. You can download the Dosato interpreter [here](https://github.com/Robotnik08/cdosato/releases/latest). Once you have the Dosato interpreter installed, you can run the code by typing the following command in the terminal:

```
dosato <filename>
```

Where `<filename>` is the name of the Dosato file that you want to run. For example, if you want to run the code in the file `day1.to`, you would type the following command in the terminal:

```bash
dosato day1.to
```

Thats it really. I hope you enjoy the solutions. Feel free to reach out to me if you have any questions or suggestions. I am always happy to help.


## Log

### Day 1
- Part 1
    - Ended up doing the mathy approach
- Part 2
    - Mathy approach was not the easier way here, spending more time than I wanted to on this one, but switched to a more straightforward approach and got it done. Optimised to use a mathy approach after the fact.
### Day 2
- Part 1
    - Straightforward implementation, but a bit slow.
- Part 2
    - This slowness carried over to part 2 as well. Need to optimise this heavily, there must be some trick to detect repeated digits without checking the ENTIRE range. (update later: I made it way quicker with modulos)
### Day 3
- Part 1
    - Very easy implementation.
- Part 2
    - Had to remake the entire thing to accomodate for the new logic, but it was still pretty straightforward, works with any battery size.
### Day 4
- Part 1
    - Initial implementation, straightforward.
- Part 2
    - Fun solve, but was a bit slow, so I improved it by using a stack to keep track of what needs to be checked, instead of checking the entire grid every iteration.
### Day 5
- Part 1
    - My brain decided to not wake up on time today, so I was late, part 1 was easy though.
- Part 2
    - I was overthinking this one too much, in this end sorting the start and end positions and keeping track of how many ranges cover each position, works really quickly.
### Day 6
- Part 1
    - I woke at at 9am to preserve my sanity, anyways, very easy day.
- Part 2
    - Same as part 1, I merged them all into collumns and just did it, very easy day today.
### Day 7
- Part 1
    - Solution ended up being pretty straightforward, just simulating the process.
- Part 2
    - Instead of a recursive solution, just keep track of the amount of timelines per row, and add accordingly, ended up being pretty quick.
### Day 8
- Part 1
    - Initially tried to do a more complex solution, then also realised I read the instructions wrong. After that and a very painful bug on my end, I got it done.
- Part 2
    - had to rewrite it completely, and managed to update part 1 to use the same logic. Ended up being a pretty fun solve.
### Day 9
- Part 1
    - Straightforward implementation of the problem statement.
- Part 2
    - Way harder, In the end grouped all edges together, and ran for each rect combination. It's kinda bruteforcey but it works.
### Day 10
- Part 1
    - Very clean and elegant solution by XORing all combinations of buttons until the correct light configuration is found.
- Part 2
    - Unfortunetely couldn't think of a programmatic way to solve part 2, so I caved in and used python with z3 to solve it really quickly. A bit of a bummer, might get back to it later.
### Day 11
- Part 1
    - Memoized DFS to count all paths from "you" to "out".
- Part 2
    - Reused the memoized DFS to count all paths for the segments and multiplied the results. Decided to remove the cache as it was tainted per call, so I passed it as a parameter.