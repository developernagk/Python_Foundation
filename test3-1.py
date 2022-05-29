{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8a98e283",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello. John\n"
     ]
    }
   ],
   "source": [
    "name = \"John\"\n",
    "print(\"Hello.\", name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e040634d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "78 점 입니다.\n"
     ]
    }
   ],
   "source": [
    "score = 78\n",
    "print(score, \"점 입니다.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "715d817a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "name John score 78\n"
     ]
    }
   ],
   "source": [
    "print(\"name\", name, \"score\", score)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "9577feec",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "i + j = 103\n",
      "******************************\n"
     ]
    }
   ],
   "source": [
    "i = 100\n",
    "j = 3\n",
    "print(\"i + j =\", i + j)\n",
    "\n",
    "twinkle = '*'\n",
    "print(twinkle * 30)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "0d66e419",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your name ; 나경\n"
     ]
    }
   ],
   "source": [
    "name = input('Enter your name ; ')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "02c0f2f5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "나경\n"
     ]
    }
   ],
   "source": [
    "print(name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "196cb203",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your age ; 22\n"
     ]
    }
   ],
   "source": [
    "age = input('Enter your age ; ')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "16b382c2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "22\n"
     ]
    }
   ],
   "source": [
    "print(age)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "7224c786",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "My name is  나경  and  22 years old.\n"
     ]
    }
   ],
   "source": [
    "print('My name is ', name, ' and ', age, 'years old.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "64b92dda",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "My name is \" 나경 \".\n"
     ]
    }
   ],
   "source": [
    "print('My name is \\\"', name,'\\\".')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "ad049fe7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your name ; 나경\n",
      "Enter your age ; 22\n",
      "My name is  나경\n",
      "Age = 22\n"
     ]
    }
   ],
   "source": [
    "name = input('Enter your name ; ')\n",
    "age = input('Enter your age ; ')\n",
    "\n",
    "print('My name is ', name)\n",
    "print('Age =', age)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "c0607893",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "당신의 국어 성적은? 90\n",
      "당신의 영어 성적은? 90\n",
      "당신의 수학 성적은? 90\n",
      "3개 과목의 평균은  90.0 입니다.\n"
     ]
    }
   ],
   "source": [
    "kor = input(\"당신의 국어 성적은? \")\n",
    "kor = float(kor)\n",
    "\n",
    "eng = input(\"당신의 영어 성적은? \")\n",
    "eng = float(eng)\n",
    "\n",
    "math = input(\"당신의 수학 성적은? \")\n",
    "math = float(math)\n",
    "\n",
    "avg = (kor + eng + math) / 3\n",
    "print(\"3개 과목의 평균은 \", avg, \"입니다.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "d4c5abdb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "이름 3글자를 입력하세요 ; 김나경\n",
      "김김김김김\n",
      "나나나나나\n",
      "경경경경경\n"
     ]
    }
   ],
   "source": [
    "name = input(\"이름 3글자를 입력하세요 ; \")\n",
    "print(name[0] * 5)\n",
    "print(name[1] * 5)\n",
    "print(name[2] * 5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "f404e612",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "당신의 이름을 입력하세요 ; 김나경\n",
      "당신의 소속기관을 입력하세요 ; 동아대학교\n",
      "당신의 출생년도를 입력하세요 ; 2002\n",
      "당신의 이름은  김나경\n",
      "동아대학교 에 소속되어 있으시군요\n",
      "당신의 나이는  20 세, 맞죠?\n"
     ]
    }
   ],
   "source": [
    "name = input(\"당신의 이름을 입력하세요 ; \")\n",
    "belong = input(\"당신의 소속기관을 입력하세요 ; \")\n",
    "birthyear = int(input(\"당신의 출생년도를 입력하세요 ; \"))\n",
    "\n",
    "print(\"당신의 이름은 \", name)\n",
    "print(belong, \"에 소속되어 있으시군요\")\n",
    "print(\"당신의 나이는 \", 2022 - birthyear, \"세, 맞죠?\")"
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
