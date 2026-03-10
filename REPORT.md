# The project REPORT is where students will document key learnings, challenges, and reflections on their experience using CoPilot for software development. 

# First Impressions - Initial Take on the Project Assignment
## In this section, students will provide their initial thoughts on the project assignment, including their understanding of the requirements, any assumptions they made, points that need clarification, and their overall approach to tackling the project.
## Initial Thoughts
When I first read the assignment, I understood that the goal was to build a simplified Hangman‑style word‑guessing game, but with strict constraints: no loops in the core logic, pure functions, separation of UI and logic, and a focus on design thinking before coding. It felt different from typical programming assignments because the emphasis was not only on coding but also on documenting my reasoning and interacting with Copilot in a structured way.
## Assumptions Made
I assumed the minimal core function should only handle updating guessed letters and lives, not full game logic.
I assumed the secret word would always be a valid lowercase string.
I assumed guesses would be single characters, not full words.
I assumed the game loop and UI would come later, so Phase 2 should stay intentionally simple.
## Points Needing Clarification
Whether repeated guesses should cost a life.
Whether the minimal function should validate input types.
How strict the “no mutation” rule was (I confirmed that copying lists was required)
Whether recursion was acceptable for replay instead of while True.

# Key Learnings
## Here, students will summarize the most important things they learned while working on the project. This could include computer science related concepts, technical skills, insights about using CoPilot effectively, and any new concepts or tools they encountered
## Computer Science Concepts and Technical Skills
I learned how to write pure functions that avoid side effects and mutation.
I practiced separating logic from UI, which made the code cleaner and easier to test.
I improved my understanding of state management in games.
I learned how to use pytest to validate behavior and catch mistakes early.
I gained experience structuring a Python project with multiple modules.
## Insights about Using CoPilot Effectively
Copilot works best when I give clear, specific prompts.
It is very helpful for generating test cases and documentation.
It sometimes tries to over‑engineer solutions unless I explicitly ask for minimalism.
Asking Copilot why it suggests something helps me understand whether to accept or reject it.
## New Concepts or Tools Encountered
Using pytest for automated testing.
Working with Copilot in Ask Mode vs Agent Mode
Understanding how Copilot logs interactions into JOURNAL.md.
Designing a game loop without using while True
# Report on CoPilot Prompting Experience
## Student may pull examples from the JOURNAL.md to illustrate their experience, including specific interactions that were particularly helpful or challenging.
### Types of prompts that worked well
Can you review my update_game_state function?
Can you suggest tests for this function?
Can you document main.py without being too verbose?
Why do you recommend this change?
### Types of prompts that did not work well or failed
Vague prompts like “Improve this code” led to over‑engineered solutions.
Asking Copilot to “optimize” the function made it try to add loops or mutate lists.
Sometimes Copilot tried to rewrite the entire file instead of making small edits.
# Limitations, Hallucinations and Failures
## In this section, students will document any instances where CoPilot provided incorrect or misleading information (hallucinations) or where it failed to provide a useful response. They will analyze why these issues occurred and how they impacted their work on the project.
## For example: Fabricated APIs, Deprecated functions, Subtle logical errors, Confident but wrong explanations, Over-engineered solutions, Under-engineered solutions, overcomplicated code, oversimplified code, etc.
## Examples of Hallucinations or Failures or Misleading Information or Confident but Wrong Explanations, or Over-engineered or Under-engineered Solutions
Suggesting the use of a set instead of a list for guessed letters, which would break ordering.
Proposing loops in the core logic, even though loops were forbidden
Recommending unnecessary input validation or extra features not required in Phase 2.
Occasionally trying to mutate the original list, violating purity.
## Analysis of Why These Issues Occurred
Copilot generalizes from typical Hangman implementations, which are more complex.
Without strict instructions, it tries to “improve” code beyond the assignment’s minimal requirements.
It sometimes assumes performance optimization is needed, even when simplicity is the goal
## Impact on the Project
I had to carefully evaluate suggestions instead of accepting them blindly
It reinforced the importance of understanding the assignment deeply before using AI tools.
It made me more aware of how easily AI can drift away from constraints unless guided clearly.
# AI Trust
## When did I trust the AI?
When generating test cases.
When reviewing code for clarity and documentation.
When explaining concepts or edge cases.
## When did I stop trusting it?
When it suggested structural changes that violated assignment rules.
When it tried to add loops or mutate inputs.
When it proposed over‑complicated solutions.
## What signals or situations or patterns indicated low reliability?
Overly confident tone with incorrect suggestions.
Adding features I didn’t ask for.
Rewriting too much code at once
Suggesting unnecessary abstractions.
# What I Learned
## What did you learn about software development?
Writing pure functions forces clearer thinking about state and behavior.
Testing early helps catch mistakes before they grow.
Documentation is easier when done incrementally.
Simplicity is often better than cleverness.
## What did you learn about using AI tools?
AI is a powerful assistant, but not a replacement for understanding.
Good prompts lead to good results; vague prompts lead to chaos.AI can accelerate work, but only if I stay in control.AI is best used for brainstorming, reviewing, and generating tests.
## When should you trust AI? When should you double-check it?
Trust it for patterns, examples, and documentation.
Double‑check logic, constraints, and anything that affects correctness.
# Reflection
## Did AI make you faster? Why or why not?
Yes,especially for generating tests, documentation, and reviewing code.But sometimes it slowed me down when it over‑engineered solutions.
## Did you feel in control of the code?
Yes, because I made the final decisions and kept the minimal function simple.
## Would you use AI the same way next time? What would you change?
I would use more precise prompts from the beginning Ask for smaller, incremental suggestions.
Avoid asking Copilot to “improve” code without constraints.