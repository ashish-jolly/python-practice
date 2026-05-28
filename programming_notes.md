### DAY 6

Problems solved: 4
Time spend: 3 hours 15 minutes

concepts learned:
- while loop practice
- modulo operator (%)
- counter variable
- list indexing
- moving index with index += 1

Mistakes I made
- forgot to move index
- used index += 5 instead of index += 1
- printed wrong variable

important pattern learned:

numbers = [4, 7, 2, 9, 10]

index = 0
counter = 0
while index < len(numbers):
    if numbers[index] > 5:
        counter += 1
    index += 1
    
print(counter)

# DAY 12
### What I learned
- splitting a sentence with .split() and convert it to a list
- learned to combine a same length words and count it with len
- return result must outside the for loop

### Mistakes i made
- tried to append dictionary instead of list inside dictionary
- sometimes guessing

### Key patterns
- if key in dict - check existence
- dict[key] += 1 - Increment count

# DAY 13
### What I learned
- I learned to find average with division using /
- partially learn to split words and count letters on it and convert letters count into value
- partially learn to merge two dictionary to one

### Mistakes I made
- overcoplicating code without thinking properly
- didn't use parentheses after "set"

### DAY 14
- 3 problems, while loop + conditions
- problem 1 took 1 hour - mistake was in instead of < in while condition
- Learned: % gives remainder, not multiplication
- Learned: increment must be outside if but inside the while loop
- Independent level: much higher than Day 13 on same problem type

### DAT 15
- 3 problems completed
- New concepts:accumulator pattern total += numbers[x],finding largest with largest = numbers[0]
- weakness:overcomplicated with unnecessary variables
- = assigns, += adds and assigns
- focus limit today: 2.5 hours

### DAY 17
-  Reverse list - solved, key learning: len(numbers) - 1 for last index, append() to add to list, >= 0 condition, i -= 1 to go backwards
- Second largest - solved, key learning: order assignment matters - save old value first before overwriting
- Total time: 3 hours 8 minutes
- focus dropped at end - acceptable fo first full day post-exams

### DAY 18
- for loops indroduced
- key difference from while loop: no index, no condition, no increment - Python handles it
- 5 problems solved: print all, print even, sum, largest, count above average
- two loop pattern: first loop to calculate, second loop to use that result
- Unanswered question: Why is average calculated outside the first loop- answer tomorrow
- Focus limit today: 2 hours 10 minutes- low sleep cause

### DAY 19
- 8 for loop problems completed
- patterns solidfied:filtering, accumulating, transforming, two-list comparison
- key learning: if number in list2 checks membership without index
- len(word) inside append - no need for separate step
- focus limit today: 2hours 5minutes
- no major errors today - speed improving

### DAY 20
- Dictionaries with for loops - 6 problems completed
- Key syntax: {} to create, dict[key] = value to add/update
- Looping: for key in dict gives keys, dict[key] gives value
- Patterns: filtering into new dict, accumulating values, updating values
- focus limit: 2 hours 15 minutes - last 15 minutes was shallow
- Next: more dictionary problems tomorrow to solidify

### DAY 21
- word/character counting pattern: if word in dict ~ dict[word] += 1, else ~ dict[word] = 1
- continue keyword - skips current loop iteration, moves to next
- Use == not "is" for string comparison - is checks identity, == checks value
- New concept: frequency dictionary - building count of each item from a list or string 
- problem 1: word count from list - 1hour 13 minutes (new pattern, hard)
- problem 2: number count from list  - 8min (same pattern, fast)
- problem 3: letter count from sentence, ignoring spaces - 46min (new twist with continue)
- most frquent word problem - incomplete, left at starting variable syntax
- Total time: 2hr 38min
- Tomorrow: finish most frequent word problem first, answer how to access word_counts["apple"]

### DAY 22
- 5 problems completed
- patterns: most frequent word, squares dictionary, pass/fail grading, total + most expensive combined, grouping into list inside dictionary
- new pattern: lists as dictionary values - dict1["even"].append(number)
- lazy thinking identified as active problem - need to pause and think before answering
- merge dictionaries problem - incomplete, left for tomorrow
- Total time: 2hr 34min

### DAY 23
- merge dictionaries - completed, 2 loops patter, result[key] = value syntax solidified
- reversed each word problem - incomplete, know the plan left at coding stage
- key learning: word[::-1] reverses a string , " ".join(list) into string
- morning session: 0 code written due to lazy thinking
- afternoon: session was productive
- total time today - 1hr 51min
- tomorrow - finish reverse words problem first

### DAY 24
- duplicates problem completed using dictionary keys - result[number] = 1, then list(result.key())
- key insight: logic guidance from mentor = good. syntax answers from mentor = harmful. Check notes first, struggle 20 minutes, ten ask for only hints
- list(dict.keys()) - extracts all keys as a list
- total time today: 1hr 40min

### CONSISTENCY BUILDING NOTES
- solved a dictionary problem that was almost forgot and recalling it by these kind of problems
- result[number] = 1 and result[number] += 1 not fully understand. understand correctly tomorrow. the code is a part of the problem
- 40minutes consistency building done

### CONSISTENCY BUILDING NOTES DAY 2
- understand what is happening in result[number] = 1 and result[number] += 1
- done variation problem with same logic
- total time 45min. consistency building done
- tomorrow: print each key and value using a second loop through result dictionary

### CONSISTENCY BUILDING NOTES DAY 3
- done yesterday's incomplete problem which is dictionary's key and value separately printing
- today stopped session mid logic of a problem which is finding highest count word
- consistency building done, 50 minutes

### CONSISTENCY BUILDING NOTES DAY 4
- solved most frequent word problem using dictionary
- corrected the mistake in my code and get the correct output
- consistency done 35minutes
- tomorrow will understand more deeply and consolidate this problem before starting another problem

### CONSISTENCY BUILDING NOTES DAY 5
- understand more deeply most frequent word problem
- did variation of this problem called most frequent number
- realized one thing that is in dictionary inside "number" is the key not "key"
- use None for empty number variable
- consistency done, 1hr

### CONSISTENCY BUILDING PHASE DAY 6
- did logic of grouping in dictionary which is a new pattern
- understand it in a good way
- need to umderstand more deeply tomorrow
- halfway writing the code stopped because of consistency building
- consistency done, 1hr

### CONSISTENCY BUILDING NOTES DAY 7
- complete yesterday's halfway stopped problem
- understand it more deeply
- from tomorrow i will try my maximum to debug myself before asking claude
- consistency done, 1hr

### CONSISTENCY BUILDING NOTES DAY 8
- recalled merging dictionary problem
- did variation of it
- learned to add new key-value pair to any dictionary
- consistency done, 1hr

### CONSISTENCY BUILDING NOTES DAY 9
- tried to do inverting a dictionary which is a new pattern
- not finished and understood it correctly, tomorrow will more deeply understand and finish it
- consistency done, 1hr 10min

### CONSISTENCY BUILDING NOTES DAY 10
- completed the inverting problem and understand it
- did a variation of it
- going to answer claude's questions about programming
- started a frequency counting problem and stopped halfway logic. will finish tomorrow
- consistency done, 1hr 10min

### CONSISTENCY BUILDING NOTES DAY 11
- done frequency counting problem and understand it
- started function
- did small problem of function
- consistency done, 1hr 20min

### DAY 25
- today done 3 function problem
- 2 problems almost understand, one understand moderately will understand more tomorrow of this problem
- find a bug in indedation with returning. also understand that more tomorrow
- consistency done, 1hr 20min

### DAY 26
- today done 3 function problems
- reversing a string, getting total of numbers in a list, a palindrome problem means backwards and forwards if equal return true, else return false
- but palindrome problem needs to understand more tomorrow
- consistency done, 1hr 20min

### DAY 27
- today done 5 problems in functions
- celsius to fahrenheit, finding longest word, count words in a sentence, finding positive or negative. if positive return true else false, getting multiplication of numbers
- confused dictionary pattern with list pattern. eventually understand these types of things python
- forget split need to more carefully think when programming
- consistency done, 1hr 30min

### DAY 28
- today learn to give function inside a function
- understand conditions using but need to consolidate more
- debbugged a small error
- consistency done, 1hr 30min

### DAY 29
- today did a test from claude which is i already consolidated problem doing under 15 min. half passed it.
- did a hard function dictionary problem and understood it. but need to completely have in my head
- needs to be more careful of dead codes.
- consistency done, 1hr 30min

### DAY 30
- did 5 function problems. filter even numbers from a list of numbers, filter longer than a number in the input with list of words,squaring numbers in a list, capitalizing words in a list, removing duplicates from a list of numbers.
- to find duplicates use 'in' and do according to that
- for finding square 'number ** 2', for cube 'number ** 3', etc.
- consistency done, 1hr 30.

### DAY 31
- did 6 problems. 1 set problem, 1 tuple problem, 4 list comprehension problem and 1 is unfinished tomorrow will finish and understand it
- consolidated enough sets and tuples
- learned disguishion between dictionary and sets
- list comprehension started today and understand as much i learned
- consistency done, 1hr 45min

### DAY 32
- did 4 list comprehension problem and in it 2 problems with ternary expression and 1 problem did with error handling but need to understand it more. total 5 problems
- ternary expression means without filtering giving condition in list comprehension
- tomorrow need to understand more the problem i did of error handling and understand error handling more
- consistency done, 1hr 45min

### DAY 33
- did two error handling problem
- introduced finally today in base level like a the thing finished
- learn to put condition inside try in error handling
- learned 2 errors in good level but not deeper level. ZeroDivisionError and ValueError
- consistency done, 1hr 45min

### DAY 34
- today was learning with new ai perplexity and in a different style learning which hard for me rn
- try to learn deeper about error handling but sudden jump in hardness caused bad learning
- need to understand more tomorrow
- today was building a small calculator was problem
- consistency done, 2hours

### DAY 35
- today done 5 error handling programs including a calculator
- consolidated enough but need to be done more consolidation
- one thing to notice while coding is risky code will only inside try others outside or above try
- consistency done, 2hours

### DAY 36
- today done 3 error handling problems including a atm system and 1 last problem need to finish tomorrow
- consistency done, 2hrs

### DAY 37
- total done 3 problems one problem is in halfway need to finish tomorrow
-consistency done, 2hr 15min

### DAY 38
- started file handling
- w = write/overwrite, a = append, r = read
- fixed vs code directory issue
- need more practice tomorrow
- consistency done, 2hr 15min

### DAY 39
- did 5 file handling problems
- use str to convert integer to string and use n\ for new line. if needed to use n\ in a file handling it must be in a string
- learned new error in error handling called FileNotFoundError
- and be aware of learning deep down basics in python
- consistency done, 2hr 15min

### DAY 40
- did 7 programs
- learned basics of modules and imports and did a very small project myself
- be aware of very basics
- tomorrow need to understand a list loop problem
- consistency done, 2hr 30min

### DAY 41
- did 1 program of basic oop
- understanding basic oop today deeply
- tomorrow need to continue the same problem understanding more
- consistency done, 2hr 30min. pushed through resistance and always try to push throuh resistance.

### DAY 42
- done 3 basic oop problems
- understand basic oop in a good way but need more deep understanding
- tomorrow first thing to do is trying to understand deep
- consistency done, 2hr 30min