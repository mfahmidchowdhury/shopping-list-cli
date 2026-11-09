# Reflections

1. Share one aspect of building this project you found challenging and how you
   overcame it.

   tbh the hardest part for me was definitely figuring out how to handle bad user input w/o the whole app crashing rn. like, when i asked for quantity and someone typed letters instead of numbers, it broke everything lol (Python Software Foundation, n.d.). i overcame this by using a try/except block combined with a while loop to catch ValueError errors. so if u type something weird, it just prints a nice warning msg and lets u try again instead of crashing out. writing those edge cases took a minute to get used to, but it made the cli feel way more stable and user-friendly.

2. Share one technical concept that you gained a deeper understanding of
   through building this project. Explain that concept in simple terms and
   explain how it is used in your project.

   btw building this rlly helped me understand how lists of dictionaries work together for data structures. basically, think of a list as a container holding multiple items, and each item is its own dictionary with key-value pairs like name, quantity, and price . in my shopping list app, every time u add something, it appends a new dictionary containing those details to the cart list. this made it super easy to loop through everything using standard iteration and calculate the total price later on without getting confused by messy variables.