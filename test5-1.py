{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6f1011a6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "10\n",
      "15\n",
      "20\n",
      "25\n",
      "30\n",
      "35\n",
      "40\n",
      "45\n",
      "50\n",
      "55\n",
      "60\n",
      "65\n",
      "70\n",
      "75\n",
      "80\n",
      "85\n",
      "90\n",
      "95\n",
      "100\n"
     ]
    }
   ],
   "source": [
    "# 1 ~ 100 사이의 5의 배수\n",
    "\n",
    "i = 1\n",
    "n = 1\n",
    "while n < 100 :\n",
    "    n = i * 5\n",
    "    i = i + 1\n",
    "    print(n)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "0badd7e9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "숫자를 입력하시오 ; 3\n",
      "3\n",
      "3\n",
      "3\n",
      "num =  3\n"
     ]
    }
   ],
   "source": [
    "# 조건에 따른 while문 실행\n",
    "\n",
    "num = int(input(\"숫자를 입력하시오 ; \"))\n",
    "\n",
    "if num != 99999 :\n",
    "    i = 0\n",
    "    while i < num :\n",
    "        print(num)\n",
    "        i = i + 1\n",
    "        \n",
    "print(\"num = \", num)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "2767b0b5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Do you want to quit?y\n"
     ]
    }
   ],
   "source": [
    "# 사용자가 종료를 요청할 때(\"y\" 입력)까지 반복하기\n",
    "\n",
    "quit = \"n\"\n",
    "\n",
    "while quit != \"y\" :\n",
    "    quit = input(\"Do you want to quit?\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "04f62d96",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "비밀번호를 입력하세요 ; 5555\n",
      "비밀번호를 입력하세요 ; 3333\n",
      "비밀번호를 입력하세요 ; 1234\n"
     ]
    }
   ],
   "source": [
    "# 맞는 패스워드를 입력할 때까지 반복하기\n",
    "\n",
    "pwd = \"????\"\n",
    "\n",
    "while pwd != \"1234\" :\n",
    "    pwd = input(\"비밀번호를 입력하세요 ; \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "bf096e6b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "비밀번호를 입력하세요 : 5676\n",
      "비밀번호를 입력하세요 : 3644\n",
      "비밀번호를 입력하세요 : 1234\n",
      "비밀번호 입력 오류가 3번 발생하여, 처리할 수 없습니다.\n"
     ]
    }
   ],
   "source": [
    "# 맞는 패스워드를 입력할 때까지 반복하기, 3번하기 비밀번호 틀리면 반복 입력 기회는 없다\n",
    "\n",
    "pwd = \"????\"\n",
    "count = 1\n",
    "\n",
    "while pwd != \"1234\" and count <= 3 :\n",
    "    pwd = input(\"비밀번호를 입력하세요 : \")\n",
    "    count = count + 1\n",
    "    \n",
    "if count > 3 :\n",
    "    print(\"비밀번호 입력 오류가 3번 발생하여, 처리할 수 없습니다.\")\n",
    "else  :\n",
    "    print(\"비밀번호가 정확합니다!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "534f8483",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "s =  2\n",
      "s =  3\n",
      "s =  4\n",
      "s =  5\n",
      "s =  6\n",
      "s =  7\n",
      "s =  8\n",
      "s =  9\n",
      "s =  10\n"
     ]
    }
   ],
   "source": [
    "# 출력 결과는?\n",
    "\n",
    "s = 1\n",
    "n = 1\n",
    "\n",
    "while s < 10 :\n",
    "    s = s + n\n",
    "    print(\"s = \", s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "558db187",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "x =  0.5\n",
      "y =  1.5\n",
      "x =  0.25\n",
      "y =  1.75\n",
      "i =  2\n"
     ]
    }
   ],
   "source": [
    "# 출력 결과는?\n",
    "\n",
    "x = 1.0\n",
    "y = 1.0\n",
    "i = 0\n",
    "\n",
    "while y <= 1.5 :\n",
    "    x = x / 2\n",
    "    y = x + y\n",
    "    i = i + 1\n",
    "    \n",
    "    print(\"x = \", x)\n",
    "    print(\"y = \", y)\n",
    "    \n",
    "print(\"i = \", i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "469931d2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "정수를 몇개 입력 받을까요? 1\n",
      "숫자를 입력하세요 ; 4\n",
      "입력받은 수의 평균은 =  4.0\n"
     ]
    }
   ],
   "source": [
    "numofnum = 0\n",
    "count = 1\n",
    "sum = 0\n",
    "\n",
    "while numofnum <= 0 :\n",
    "    numofnum = int(input(\"정수를 몇개 입력 받을까요? \"))\n",
    "    \n",
    "while count <= numofnum :\n",
    "    num = float(input(\"숫자를 입력하세요 ; \"))\n",
    "    count = count + 1\n",
    "    sum = sum + num\n",
    "                \n",
    "print(\"입력받은 수의 평균은 = \", sum / numofnum)"
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
