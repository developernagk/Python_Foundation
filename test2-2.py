{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "71885064",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "My name is  김나경  and  22 years old.\n"
     ]
    }
   ],
   "source": [
    "name = '김나경'\n",
    "age = 22\n",
    "\n",
    "print('My name is ', name, ' and ', age, 'years old.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "2a94ca33",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your name ;이시연\n",
      "Enter your age ;25\n",
      "My name is  이시연  and  25 years old\n",
      "My name is \" 이시연 \".\n"
     ]
    }
   ],
   "source": [
    "# get name and age from user, and  print them\n",
    "\n",
    "name  = input('Enter your name ;')\n",
    "age = input('Enter your age ;')\n",
    "\n",
    "print('My name is ', name, ' and ', age, 'years old')\n",
    "print('My name is \\\"', name, '\\\".')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "9b41e551",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "첫 번째 실수 입력: 1.1\n",
      "두 번째 실수 입력: 20\n",
      "21.1\n"
     ]
    }
   ],
   "source": [
    "number1 = float(input('첫 번째 실수 입력: '))\n",
    "number2 = float(input('두 번째 실수 입력: '))\n",
    "\n",
    "print(number1 + number2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "555c966e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "정수 입력: 5\n",
      "*****\n"
     ]
    }
   ],
   "source": [
    "number = int(input('정수 입력: '))\n",
    "\n",
    "print('*' * number)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5bb6c16e",
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
