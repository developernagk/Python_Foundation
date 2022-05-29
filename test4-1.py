{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "57de007b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a is less than b and c\n",
      "a is less than either a or b (or both)\n",
      "a is true\n"
     ]
    }
   ],
   "source": [
    "a = 1\n",
    "b = 2\n",
    "c = 3\n",
    "\n",
    "# And\n",
    "if a < b and a < c :\n",
    "    print(\"a is less than b and c\")\n",
    "    \n",
    "# Non-exclusive or\n",
    "if a < b or a < c :\n",
    "    print(\"a is less than either a or b (or both)\")\n",
    "    \n",
    "# Boolean data type. This is legal!\n",
    "a = True\n",
    "\n",
    "if a :\n",
    "    print(\"a is true\")\n",
    "else :\n",
    "    print(\"a is false\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "522a22ac",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "생년월일을 입력하세요 ; 20010907\n"
     ]
    }
   ],
   "source": [
    "Birthdate = input(\"생년월일을 입력하세요 ; \")\n",
    "\n",
    "Year = Birthdate[0 : 4]\n",
    "Month = Birthdate[4 : 6]\n",
    "Day = Birthdate[6 : ]\n",
    "\n",
    "if Month < \"01\" or Month > \"12\" :\n",
    "    print(\"월이 잘못 입력되었습니다. 다시 실행해주세요!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "17a80845",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "당신의 나이는  20 입니다\n"
     ]
    }
   ],
   "source": [
    "if Birthdate > \"20220525\" :\n",
    "    print(\"나이를 계산할 수 없습니다.\")\n",
    "else :\n",
    "    age = 2022 - int(Year)\n",
    "    \n",
    "    if Month > \"05\" :\n",
    "        age = age - 1\n",
    "        \n",
    "    print(\"당신의 나이는 \", age, \"입니다\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "42323b6e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "국어점수를 입력하세요 ; 90\n",
      "영어점수를 입력하세요 ; 70\n",
      "수학점수를 입력하세요 ; 50\n",
      "역사점수를 입력하세요 ; 30\n",
      "과락입니다.\n"
     ]
    }
   ],
   "source": [
    "Korean = int(input(\"국어점수를 입력하세요 ; \"))\n",
    "English = int(input(\"영어점수를 입력하세요 ; \"))\n",
    "Math = int(input(\"수학점수를 입력하세요 ; \"))\n",
    "History = int(input(\"역사점수를 입력하세요 ; \"))\n",
    "\n",
    "if Korean < 50 or English < 50 or Math < 50 or History < 50 :\n",
    "    print(\"과락입니다.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "d6573b0f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "국어점수를 입력하세요 ; 90\n",
      "영어점수를 입력하세요 ; 70\n",
      "수학점수를 입력하세요 ; 50\n",
      "역사점수를 입력하세요 ; 80\n",
      "합격입니다.\n"
     ]
    }
   ],
   "source": [
    "Korean = int(input(\"국어점수를 입력하세요 ; \"))\n",
    "English = int(input(\"영어점수를 입력하세요 ; \"))\n",
    "Math = int(input(\"수학점수를 입력하세요 ; \"))\n",
    "History = int(input(\"역사점수를 입력하세요 ; \"))\n",
    "Mean = (Korean + English + Math + History) / 4\n",
    "\n",
    "if Korean >= 50 and English >= 50 and Math >= 50 and History >= 50 and Mean >= 60 :\n",
    "    print(\"합격입니다.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "3f1eaf42",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-1\n"
     ]
    }
   ],
   "source": [
    "# 1\n",
    "n = 1\n",
    "m = -1\n",
    "\n",
    "if n < -m :\n",
    "    print(n)\n",
    "else :\n",
    "    print(m)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "790affbb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    }
   ],
   "source": [
    "# 2\n",
    "n = 1\n",
    "m = -1\n",
    "l = 0\n",
    "\n",
    "if n <= -m and m < l :\n",
    "    print(n)\n",
    "elif m >= l :\n",
    "    print(m)\n",
    "else :\n",
    "    print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "e7f531ca",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "s1 ;  ab\n",
      "s1 ;  ab\n",
      "s2 ;  abc\n"
     ]
    }
   ],
   "source": [
    "# 3\n",
    "s1 = \"ab\"\n",
    "s2 = \"abc\"\n",
    "s3 = \"bc\"\n",
    "\n",
    "if s1 < s2 :\n",
    "    print(\"s1 ; \", s1)\n",
    "    \n",
    "if s1 < s3 :\n",
    "    print(\"s1 ; \", s1)\n",
    "    \n",
    "if s2 < s3 :\n",
    "    print(\"s2 ; \", s2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "e446f7d1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "국어성적 ; 50\n",
      "영어성적 ; 50\n",
      "수학성적 ; 50\n",
      "불합격\n"
     ]
    }
   ],
   "source": [
    "Korean = int(input(\"국어성적 ; \"))\n",
    "English = int(input(\"영어성적 ; \"))\n",
    "Math = int(input(\"수학성적 ; \"))\n",
    "\n",
    "Mean = (Korean + English + Math) / 3\n",
    "\n",
    "if Korean < 50 or English < 50 or Math < 50 :\n",
    "    print(\"과락\")\n",
    "elif Mean >= 60 :\n",
    "    print(\"합격\")\n",
    "else :\n",
    "    print(\"불합격\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "a54dffae",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "월을 입력하세요 ; 13\n",
      "입력 오류\n"
     ]
    }
   ],
   "source": [
    "mon = int(input(\"월을 입력하세요 ; \"))\n",
    "\n",
    "if mon == 1 or mon == 3 or mon == 5 or mon == 7 or mon == 8 or mon == 10 or mon == 12 :\n",
    "    print(\"31일까지\")\n",
    "elif mon == 2 :\n",
    "    print(\"28일 또는 29일까지\")\n",
    "elif mon == 4 or mon == 6 or mon == 9 or mon ==11 :\n",
    "    print(\"30일까지\")\n",
    "else :\n",
    "    print(\"입력 오류\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "74fd2994",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "월을 입력하세요 ; 13\n",
      "입력 오류\n"
     ]
    }
   ],
   "source": [
    "mon = int(input(\"월을 입력하세요 ; \"))\n",
    "\n",
    "if mon in [1,3,5,7,8,10,12] :\n",
    "    print(\"31일까지\")\n",
    "elif mon == 2 :\n",
    "    print(\"28일 또는 29일까지\")\n",
    "elif mon in [4,6,9,11] :\n",
    "    print(\"30일까지\")\n",
    "else :\n",
    "    print(\"입력 오류\")"
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
