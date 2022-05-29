{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "7fe5be35",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "단어를 입력하세요 ; apple\n",
      "위치를 찾을 한 글자를 입력하세요 ; e\n",
      "e 는 apple 내에 없습니다\n"
     ]
    }
   ],
   "source": [
    "word = input(\"단어를 입력하세요 ; \")\n",
    "letter = input(\"위치를 찾을 한 글자를 입력하세요 ; \")\n",
    "\n",
    "count = 0\n",
    "\n",
    "for char in word :\n",
    "    count = count + 1\n",
    "    if char == letter :\n",
    "        break\n",
    "        \n",
    "if count == len(word) :\n",
    "    print(letter, \"는\", word, \"내에 없습니다\")\n",
    "else :\n",
    "    print(letter, \"는\", word, \"의\", count, \"번째 위치합니다\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "11d2d06a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "단어를 입력하세요 ; love\n",
      "위치를 찾을 한 글자를 입력하세요 ; a\n",
      "a 는 love 의 4 번째 위치합니다\n"
     ]
    }
   ],
   "source": [
    "word = input(\"단어를 입력하세요 ; \")\n",
    "letter = input(\"위치를 찾을 한 글자를 입력하세요 ; \")\n",
    "\n",
    "count = 0\n",
    "\n",
    "for char in word :\n",
    "    count = count + 1\n",
    "    if char == letter :\n",
    "        break\n",
    "        \n",
    "if count == len(word) :\n",
    "    print(letter, \"는\", word, \"의\", count, \"번째 위치합니다\")\n",
    "else :\n",
    "    print(letter, \"는\", word, \"내에 없습니다\")"
   ]
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
