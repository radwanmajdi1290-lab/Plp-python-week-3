# Grade Reporter & Bug Hunt

- `grade_reporter.py`: loops through the score list, assigns grades, counts passes and fails, and calculates the average score.
- `bug_hunt.py`: fixes the broken loop program and includes comments explaining each bug that was corrected.

The hardest bug to find in Part B was the off-by-one mistake in the `while` condition. I knew something was wrong because the program ran without an error, but the total was lower than 15, which meant the loop stopped before reaching 5. The missing colon and string-to-integer issue were easier to catch because Python reported them immediately.
