{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "78d9f532",
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
    "    \n",
    "    print(\"아이템 수 = \", count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "fc6ddda8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " $\n",
      " $\n",
      " $\n",
      " $\n",
      " $\n",
      " $\n",
      " $\n",
      " $\n",
      " $\n"
     ]
    }
   ],
   "source": [
    "for i in range(3) :\n",
    "    for j in range(3) :\n",
    "        print(\" $\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "9ba5e109",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "#\n",
      " $\n",
      " $\n",
      " $\n",
      " $\n",
      " $\n",
      "#\n",
      " $\n",
      " $\n",
      " $\n",
      " $\n",
      " $\n"
     ]
    }
   ],
   "source": [
    "for i in range(2) :\n",
    "    print(\"#\")\n",
    "    for j in range(5) :\n",
    "        print(\" $\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b5aa6b38",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1st level =  2\n",
      " 2nd level =  1\n",
      " i * j =  2\n",
      " 2nd level =  2\n",
      " i * j =  4\n",
      " 2nd level =  3\n",
      " i * j =  6\n",
      " 2nd level =  4\n",
      " i * j =  8\n",
      "1st level =  4\n",
      " 2nd level =  1\n",
      " i * j =  4\n",
      " 2nd level =  2\n",
      " i * j =  8\n",
      " 2nd level =  3\n",
      " i * j =  12\n",
      " 2nd level =  4\n",
      " i * j =  16\n",
      "1st level =  6\n",
      " 2nd level =  1\n",
      " i * j =  6\n",
      " 2nd level =  2\n",
      " i * j =  12\n",
      " 2nd level =  3\n",
      " i * j =  18\n",
      " 2nd level =  4\n",
      " i * j =  24\n"
     ]
    }
   ],
   "source": [
    "for i in range(2, 7, 2) :\n",
    "    print(\"1st level = \", i)\n",
    "    \n",
    "    for j in range(1, 5, 1) :\n",
    "        print(\" 2nd level = \", j)\n",
    "3        print(\" i * j = \", i * j)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "f49ee445",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7 th table\n",
      "  7  *  1  =  7\n",
      "  7  *  2  =  14\n",
      "  7  *  3  =  21\n",
      "  7  *  4  =  28\n",
      "  7  *  5  =  35\n",
      "  7  *  6  =  42\n",
      "  7  *  7  =  49\n",
      "  7  *  8  =  56\n",
      "  7  *  9  =  63\n",
      "8 th table\n",
      "  8  *  1  =  8\n",
      "  8  *  2  =  16\n",
      "  8  *  3  =  24\n",
      "  8  *  4  =  32\n",
      "  8  *  5  =  40\n",
      "  8  *  6  =  48\n",
      "  8  *  7  =  56\n",
      "  8  *  8  =  64\n",
      "  8  *  9  =  72\n"
     ]
    }
   ],
   "source": [
    "# times table : 7, 8\n",
    "\n",
    "for i in range(7, 9) :\n",
    "    print(i, \"th table\")\n",
    "    \n",
    "    for j in range(1, 10, 1) :\n",
    "        print(\" \", i, \" * \", j, \" = \", i * j)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "48362e5a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20\n"
     ]
    }
   ],
   "source": [
    "# a의 값은 무엇인가?\n",
    "\n",
    "a = 0\n",
    "for i in range(10) :\n",
    "    a = a + 1\n",
    "    \n",
    "for j in range(10) :\n",
    "    a = a + 1\n",
    "        \n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "e3f77c4d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "110\n"
     ]
    }
   ],
   "source": [
    "# a의 값은 무엇인가?\n",
    "\n",
    "a = 0\n",
    "for i in range(10) :\n",
    "    a = a + 1\n",
    "    for j in range(10) :\n",
    "        a = a + 1\n",
    "        \n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "fb1b00c6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "# 다음은 무엇이 출력되는가?\n",
    "\n",
    "fruit = \"banana\"\n",
    "count = 0\n",
    "for char in fruit :\n",
    "    if char == \"a\" :\n",
    "        count = count + 1\n",
    "        \n",
    "print(count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "5eb9618e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "b\n",
      "n\n",
      "n\n",
      "3\n"
     ]
    }
   ],
   "source": [
    "fruit = \"banana\"\n",
    "count = 0\n",
    "\n",
    "for char in fruit :\n",
    "    if char == 'a' :\n",
    "        count = count + 1\n",
    "    elif char == 'n ':\n",
    "        break\n",
    "    else :\n",
    "        print(char)\n",
    "        \n",
    "print(count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "b5cadb60",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "i + j =  1 and count =  1\n",
      "i + j =  2 and count =  2\n",
      "i + j =  3 and count =  3\n",
      "i + j =  2 and count =  4\n",
      "i + j =  3 and count =  5\n",
      "i + j =  4 and count =  6\n",
      "i + j =  3 and count =  7\n",
      "i + j =  4 and count =  8\n",
      "i + j =  4 and count =  9\n",
      "i + j =  5 last count :  9\n"
     ]
    }
   ],
   "source": [
    "# 2개 수를 더한 결과가 5의 배수이면 반복문 종료\n",
    "\n",
    "count = 0\n",
    "\n",
    "for i in range(5) :\n",
    "    for j in range(3) :\n",
    "        if (i + j) % 5 != 0 :\n",
    "            count = count + 1\n",
    "            print(\"i + j = \", i + j, \"and count = \", count)\n",
    "        else :\n",
    "            break\n",
    "            \n",
    "print(\"i + j = \", i + j, \"last count : \", count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "f9da75ff",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "input a positive interger : 0.9\n"
     ]
    },
    {
     "ename": "ValueError",
     "evalue": "invalid literal for int() with base 10: '0.9'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "Input \u001b[0;32mIn [15]\u001b[0m, in \u001b[0;36m<cell line: 3>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;66;03m# prime number 여부 확인\u001b[39;00m\n\u001b[0;32m----> 3\u001b[0m num \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mint\u001b[39;49m\u001b[43m(\u001b[49m\u001b[38;5;28;43minput\u001b[39;49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43minput a positive interger : \u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m      5\u001b[0m prime_yes \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mTrue\u001b[39;00m\n\u001b[1;32m      7\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m i \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28mrange\u001b[39m(\u001b[38;5;241m2\u001b[39m, num) :\n",
      "\u001b[0;31mValueError\u001b[0m: invalid literal for int() with base 10: '0.9'"
     ]
    }
   ],
   "source": [
    "# prime number 여부 확인\n",
    "\n",
    "num = int(input(\"input a positive interger : \"))\n",
    "\n",
    "prime_yes = True\n",
    "\n",
    "for i in range(2, num) :\n",
    "    if num % i == 0 :\n",
    "        prime_yes = False\n",
    "        break\n",
    "        \n",
    "if prime_yes == True :\n",
    "    print(num, \"is a prime number\")\n",
    "else :\n",
    "    print(num, \"is not a prime number\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "0f61669c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "단어를 입력하세요 : apple\n",
      "위치를 찾을 한 글자를 입력하세요 : a\n",
      "a 는 apple 의 1 번째 위치합니다\n"
     ]
    }
   ],
   "source": [
    "# 연습문제 1, 코드와 결과\n",
    "\n",
    "word = input(\"단어를 입력하세요 : \")\n",
    "letter = input(\"위치를 찾을 한 글자를 입력하세요 : \")\n",
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
   "execution_count": null,
   "id": "4a74110a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 연습문제 2(사용자에게 메시지를 입력 받음, 메시지 내에서 'a'개수를 확인하여 출력)\n",
    "\n",
    "message = input(\"문장을 입력하세요 : \")\n",
    "letter = input(\"위치를 찾을 한 글자를 입력하세요 : \")\n",
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
   "execution_count": null,
   "id": "fdbed3e4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 연습문제 3(구구단 출력, 2단부터 시작, 몇 단까지 출력할 지는 사용자에게 입력 받음)"
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
