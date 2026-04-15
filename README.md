# gradio-playlist-mergesort
cisc 121 final, made by Henry Hirsch

## problem
given a playlist with songs that have the following variables attached to them
- song name
- artist
- length
- energy level
sort the playlist by either length or energy

## chosen algorthm
I chose merge sort as I felt it was better for the task at hand, having a divide and conquer algorthm works well when showing how a class variables like the songs can be sorted to a non-expert

## 4 pillars

### decomposition
- split list in half
- keep splitting list in half until list is 1 element long
- once that is the case go through each list merging them together by comparing each variable in the lists and popping out the lesser one and putting it in a new list, then add the left over variables into the list
- repeat last step until you have a complete sorted list

### pattern recognition
- lots of repitition in the splitting and merging part of the algorthm, can reuse the function
- can also reuse a function in those to keep track of the step for a good repersentation for users of the program

### abstraction
- should not "show" how we keep track of steps

### algorthm design
<img width="335" height="725" alt="image" src="https://github.com/user-attachments/assets/920153b6-81b3-4744-9dc7-5915a8ecaff7" />
<img width="515" height="703" alt="image" src="https://github.com/user-attachments/assets/88db23ef-a27a-4477-ab33-b03da32e63f6" />


## steps to run
1) make sure you have gradio and a compatible version of python
2) open up file in a coding engine i.e vs code
3) run and click on provided link in terminal

## hugging face link

https://huggingface.co/spaces/HenryHirsch/playlist-mergesort

## testing
- there were a few problems that would cause errors when putting in values or just didnt make sense logically, I made a statment in my function which added songs too
1) not add a song which had accepted a NONE value
2) not accept a song whose values didnt make any sense (i.e song with a negative length)
this led to better results when putting through the algorthm which I also added an edge case to so it wouldnt give you a negitive step

## example video
example: https://www.youtube.com/watch?v=kInUHhHGPLE

## sources
- learn merge sort in 13 minutes by Bro Code: https://www.youtube.com/watch?v=3j0SWDX4AtU&t=132s
- AI USED: NONE

