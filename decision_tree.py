{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "69d40e68-244f-4bde-8951-acd982a356f2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Did you complete your task? (Yes/No):  Yes\n",
      "Enter study hours:  12\n",
      "Mood (Good/Average/Bad):  good\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Reflection:\n",
      "Excellent work! You're productive and consistent. Keep it up!\n"
     ]
    }
   ],
   "source": [
    "def daily_reflection(task_completed, reason, hours, mood):\n",
    "\n",
    "    if task_completed.lower() == \"no\":\n",
    "        if reason.lower() == \"distraction\":\n",
    "            return \"You were distracted today. Try keeping your phone away and use focused study blocks.\"\n",
    "\n",
    "        elif reason.lower() == \"no planning\":\n",
    "            return \"You lacked a plan. Create a simple schedule before starting your day.\"\n",
    "\n",
    "        elif reason.lower() == \"low energy\":\n",
    "            return \"Low energy affected your productivity. Focus on proper sleep and breaks.\"\n",
    "\n",
    "        else:\n",
    "            return \"Invalid reason provided.\"\n",
    "\n",
    "    elif task_completed.lower() == \"yes\":\n",
    "\n",
    "        if hours >= 5:\n",
    "            if mood.lower() == \"good\":\n",
    "                return \"Excellent work! You're productive and consistent. Keep it up!\"\n",
    "            else:\n",
    "                return \"Good job completing tasks despite your mood. Try improving your mindset.\"\n",
    "\n",
    "        else:\n",
    "            return \"You completed your task but can improve consistency. Try increasing study time.\"\n",
    "\n",
    "    else:\n",
    "        return \"Invalid input for task completion.\"\n",
    "\n",
    "\n",
    "# Taking user input\n",
    "task_completed = input(\"Did you complete your task? (Yes/No): \")\n",
    "\n",
    "if task_completed.lower() == \"no\":\n",
    "    reason = input(\"Reason (Distraction/No Planning/Low Energy): \")\n",
    "else:\n",
    "    reason = \"\"\n",
    "\n",
    "hours = int(input(\"Enter study hours: \"))\n",
    "mood = input(\"Mood (Good/Average/Bad): \")\n",
    "\n",
    "# Calling function\n",
    "result = daily_reflection(task_completed, reason, hours, mood)\n",
    "\n",
    "print(\"\\nReflection:\")\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b6b0b22a-041c-4c02-a66f-7e1852b9a0eb",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
