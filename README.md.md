# Daily Reflection Decision Tree

## Problem Statement
This project is a simple decision tree system that helps students reflect on their daily performance and improve their productivity.

## Inputs to the System
The system takes the following inputs:

1. Task Completed (Yes/No)
2. Reason for not completing (if No):
   - Distraction
   - No Planning
   - Low Energy
3. Study Hours (numeric)
4. Mood (Good/Average/Bad)

These inputs help analyze both performance and behavior to generate meaningful suggestions.

## Decision Tree Logic

The system follows a deterministic decision tree to analyze user input and generate meaningful reflection.

### Logic Flow

* If the task is **not completed**:

  * If the reason is **Distraction**:
    → Suggest reducing phone usage and using focused study sessions.
  * If the reason is **No Planning**:
    → Suggest creating a simple daily schedule before starting.
  * If the reason is **Low Energy**:
    → Suggest improving sleep and taking proper breaks.

* If the task is **completed**:

  * If study hours are **greater than or equal to 5**:

    * If mood is **Good**:
      → Strong positive reinforcement.
    * Else:
      → Appreciate effort and suggest improving mindset.
  * If study hours are **less than 5**:
    → Suggest improving consistency and increasing study time.

This logic ensures that the same input always produces the same output (deterministic behavior).
