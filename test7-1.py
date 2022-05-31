{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "025c2740",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a\n"
     ]
    }
   ],
   "source": [
    "name = 'apple'\n",
    "\n",
    "print(name[0])\n",
    "'a'\n",
    "\n",
    "school = '한동대학교'\n",
    "\n",
    "address = '경북 포항시 북구 흥해읍'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "7aad8c29",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'CuttyCat'"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s1 = 'Cutty'\n",
    "s2 = 'Cat'\n",
    "s3 = s1 + s2\n",
    "s3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "8bf13dbc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'CuttyCuttyCutty'"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s1 * 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "a0ffb81a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'@@@@@@@@@@'"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'@' * 10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "9fdf7cd5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s1 = 'cat'\n",
    "s2 = 'Cat'\n",
    "s1 == s2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "184bd6d8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s1 == 'cat'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "6ed4beba",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s1 > 'bird'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "3effd2aa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fruit = 'banana'\n",
    "len(fruit)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "8f0c253d",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndexError",
     "evalue": "string index out of range",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "Input \u001b[0;32mIn [11]\u001b[0m, in \u001b[0;36m<cell line: 2>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m length \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mlen\u001b[39m(fruit)\n\u001b[0;32m----> 2\u001b[0m last \u001b[38;5;241m=\u001b[39m \u001b[43mfruit\u001b[49m\u001b[43m[\u001b[49m\u001b[43mlength\u001b[49m\u001b[43m]\u001b[49m\n",
      "\u001b[0;31mIndexError\u001b[0m: string index out of range"
     ]
    }
   ],
   "source": [
    "length = len(fruit)\n",
    "last = fruit[length]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "60210657",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'a'"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "last = fruit[length - 1]\n",
    "last"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "16bc8e34",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a\n",
      "p\n",
      "p\n",
      "l\n",
      "e\n",
      "a\n",
      "p\n",
      "p\n",
      "l\n",
      "e\n"
     ]
    }
   ],
   "source": [
    "fruit = \"apple\"\n",
    "\n",
    "index = 0\n",
    "while index < len(fruit) :\n",
    "    letter = fruit[index]\n",
    "    print(letter)\n",
    "    index = index + 1\n",
    "    \n",
    "fruit = \"apple\"\n",
    "\n",
    "for ch in fruit :\n",
    "    print(ch)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "41345efe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'on'"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s = 'Monty Python'\n",
    "s[0 : 5] # index 0, 1, 2, 3, 4\n",
    "s[6 : 12] # index 6, 7, 8, 9, 10, 11\n",
    "s[1 : 3] # index 1,2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "645a7824",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'ana'"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fruit = 'banana'\n",
    "fruit[ : 3] # index 0, 1, 2\n",
    "fruit[3 : ] # index from 3 to last"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "7e77913d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "문자열 입력 : apple\n",
      "s[0 : 1 ]= a\n",
      "s[0 : 2 ]= ap\n",
      "s[0 : 3 ]= app\n",
      "s[0 : 4 ]= appl\n",
      "s[0 : 5 ]= apple\n"
     ]
    }
   ],
   "source": [
    "# 연습문제 1(문자열을 입력 받음, 반복문과 함수 len() 사용)\n",
    "\n",
    "input_str = input(\"문자열 입력 : \")\n",
    "l = len(input_str)\n",
    "index = 0\n",
    "\n",
    "while index < l :\n",
    "    print(\"s[0 :\", index + 1, \"]=\", input_str[0 : index + 1])\n",
    "    index = index + 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "2eb67d14",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'BANANA'"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "word = 'banana'\n",
    "new_word = word.upper()\n",
    "new_word"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "40db6e9b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "word = 'banana'\n",
    "index = word.find('a')\n",
    "index"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "5c4ea3b6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "word.find('na')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "a89386c0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "word.find('na', 3) # 두번째 숫자는 찾기 시작하는 index number"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "cb4de66c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-1"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "name = 'bob'\n",
    "name.find('b', 1, 2) # 세번째 숫자는 어디까지 찾을지 지정하는 index number"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "fdf8ae0f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'a' in 'banana'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "00e6b777",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'seed' in 'banana'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "fc663ca1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'ana' in 'banana'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "cc73df1c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a\n",
      "e\n",
      "s\n"
     ]
    }
   ],
   "source": [
    "# 함수 사용\n",
    "\n",
    "def in_both(word1, word2) :\n",
    "    for letter in word1 :\n",
    "        if letter in word2 :\n",
    "            print(letter)\n",
    "            \n",
    "in_both('apples', 'oranges')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "c2d2af31",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "문자열 입력 : apple\n",
      "찾아 바꿀 문자 : e\n",
      "applE\n"
     ]
    }
   ],
   "source": [
    "# 연습문제 2(문자열을 입력 받음, 대문자로 바꿀 문자 또는 문자열을 입력 받음, 입력 받은 문자를 대문자로 바꾼 후 전체 문자열을 출력)\n",
    "\n",
    "Input_Str = input(\"문자열 입력 : \")\n",
    "Input_find = input(\"찾아 바꿀 문자 : \")\n",
    "find_Length = len(Input_find)\n",
    "\n",
    "Index = Input_Str.find(Input_find)\n",
    "\n",
    "if Index == -1 :\n",
    "    print(\" 바꿀 문자가 없네요!\")\n",
    "else :\n",
    "    beforeStr = Input_Str[0 : Index]\n",
    "    changeStr = Input_Str[Index : Index + find_Length].upper()\n",
    "    afterStr = Input_Str[Index + find_Length : ]\n",
    "    result = beforeStr + changeStr + afterStr\n",
    "    print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "213555a1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 연습문제 3\n",
    "# (문자열을 입력 받음)\n",
    "# (대문자는 소문자로 소문자는 대문자로 바꾸어서 저장하고 출력)\n",
    "# (바꾼 후 다음을 출력(대문자 개수, 소문자 개수, 대소문자가 아닌 문자 개수))\n",
    "\n"
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
