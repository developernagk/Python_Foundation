{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c8770139",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "M\n",
      "a\n",
      "n\n",
      "g\n",
      "o\n"
     ]
    }
   ],
   "source": [
    "# while문\n",
    "\n",
    "i = 0\n",
    "fr = \"Mango\"\n",
    "\n",
    "while i < len(fr) :\n",
    "    letter = fr[i]\n",
    "    print(letter)\n",
    "    i = i + 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "dfac6557",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "M\n",
      "a\n",
      "n\n",
      "g\n",
      "o\n"
     ]
    }
   ],
   "source": [
    "# for문\n",
    "\n",
    "for letter in \"Mango\" :\n",
    "    print(letter)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "876921bc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7\n",
      "49\n",
      "14\n",
      "196\n",
      "21\n",
      "441\n",
      "28\n",
      "784\n",
      "35\n",
      "1225\n",
      "42\n",
      "1764\n",
      "49\n",
      "2401\n"
     ]
    }
   ],
   "source": [
    "# 1에서 50 사이의 7의 배수, 그 수의 제곱 값 출력\n",
    "\n",
    "for i in range(1, 50, 1) :\n",
    "    if i%7 == 0 :\n",
    "        print(i)\n",
    "        print(i**2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "03572c3e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "for i in range(1, 11) :\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "4c3c0cf0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n"
     ]
    }
   ],
   "source": [
    "for i in range(10) :\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "8a9f0059",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "9\n",
      "8\n",
      "7\n",
      "6\n",
      "5\n",
      "4\n",
      "3\n",
      "2\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "for i in range(10, 0, -1) :\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "10784672",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-10\n",
      "-9\n",
      "-8\n",
      "-7\n",
      "-6\n",
      "-5\n",
      "-4\n",
      "-3\n",
      "-2\n",
      "-1\n",
      "0\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "for i in range(-10, 11) :\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "82efd084",
   "metadata": {},
   "outputs": [],
   "source": [
    "for i in range(10, 0) :\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "535a14e2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-10\n",
      "-7\n",
      "-4\n",
      "-1\n",
      "2\n",
      "5\n",
      "8\n"
     ]
    }
   ],
   "source": [
    "for i in range(-10, 11, 3) :\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "f6a0ea0f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "H\n",
      "O\n",
      "R\n",
      "S\n",
      "T\n",
      "M\n",
      "A\n",
      "N\n",
      "N\n",
      "글자수 =  9\n"
     ]
    }
   ],
   "source": [
    "# 문자열 처리\n",
    "\n",
    "name = \"HORSTMANN\"\n",
    "count = 0\n",
    "\n",
    "for char in name :\n",
    "    print(char)\n",
    "    count = count + 1\n",
    "    \n",
    "print(\"글자수 = \", count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "1ba5b1d8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "apple\n",
      "banana\n",
      "lemon\n",
      "tomato\n",
      "아이템 수 =  4\n"
     ]
    }
   ],
   "source": [
    "# 리스트 처리\n",
    "\n",
    "fruit = [\"apple\", \"banana\", \"lemon\", \"tomato\"]\n",
    "count = 0\n",
    "\n",
    "for fr in fruit :\n",
    "    print(fr)\n",
    "    count = count + 1\n",
    "    \n",
    "print(\"아이템 수 = \", count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "d25ecdf5",
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
      "아이템 수 =  5\n",
      "b\n",
      "a\n",
      "n\n",
      "a\n",
      "n\n",
      "a\n",
      "아이템 수 =  6\n",
      "l\n",
      "e\n",
      "m\n",
      "o\n",
      "n\n",
      "아이템 수 =  5\n",
      "t\n",
      "o\n",
      "m\n",
      "a\n",
      "t\n",
      "o\n",
      "아이템 수 =  6\n"
     ]
    }
   ],
   "source": [
    "# 리스트 처리\n",
    "\n",
    "fruit = [\"apple\", \"banana\", \"lemon\", \"tomato\"]\n",
    "\n",
    "for fr in fruit :\n",
    "    count = 0\n",
    "    for f in fr :\n",
    "        print(f)\n",
    "        count = count + 1\n",
    "        \n",
    "    print(\"아이템 수 = \", count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "4fa8d330",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "*\n",
      "**\n",
      "***\n",
      "****\n",
      "*****\n",
      "******\n",
      "*******\n",
      "********\n",
      "*********\n",
      "**********\n"
     ]
    }
   ],
   "source": [
    "# 1\n",
    "# \"*\" 순차적으로 점점 많이 출력\n",
    "\n",
    "i = 0\n",
    "\n",
    "for i in range(1, 11) :\n",
    "    print('*' * i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "7ae418f8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "**********\n",
      "*********\n",
      "********\n",
      "*******\n",
      "******\n",
      "*****\n",
      "****\n",
      "***\n",
      "**\n",
      "*\n"
     ]
    }
   ],
   "source": [
    "# 2\n",
    "# \"*\" 순차적으로 점점 적게 출력\n",
    "\n",
    "i = 0\n",
    "\n",
    "for i in range(10, 0, -1) :\n",
    "    print('*' * i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "ca43d4e4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "P\n",
      "e\n",
      "t\n",
      "e\n",
      "r\n",
      " \n",
      "R\n",
      "a\n",
      "b\n",
      "b\n",
      "i\n",
      "t\n",
      "총 글자 수는 =  11\n"
     ]
    }
   ],
   "source": [
    "# 성과 이름 한 글자씩 출력\n",
    "\n",
    "name = \"Peter Rabbit\"\n",
    "count = 0\n",
    "\n",
    "for char in name :\n",
    "    print(char)\n",
    "    if char != ' ' :\n",
    "        count = count + 1\n",
    "        \n",
    "print('총 글자 수는 = ', count)"
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
