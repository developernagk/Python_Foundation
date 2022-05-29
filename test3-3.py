{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c21d8c13",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "국어성적 입력 ; 90\n",
      "영어성적 입력 ; 90\n",
      "수학성적 입력 ; 90\n",
      "성적 평균은  90.0 이며, 합격입니다.\n"
     ]
    }
   ],
   "source": [
    "kor = float(input(\"국어성적 입력 ; \"))\n",
    "eng = float(input(\"영어성적 입력 ; \"))\n",
    "math = float(input(\"수학성적 입력 ; \"))\n",
    "\n",
    "avg = (kor + eng + math) / 3\n",
    "\n",
    "if avg >= 60 :\n",
    "    print(\"성적 평균은 \", avg, \"이며, 합격입니다.\")\n",
    "else:\n",
    "    print(\"성적 평균은 \", avg, \"이며, 불합격입니다.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "900cf2ac",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "국어성적 입력 ; 50\n",
      "영어성적 입력 ; 60\n",
      "수학성적 입력 ; 40\n",
      "성적 평균은  50.0 이며, 불합격입니다.\n"
     ]
    }
   ],
   "source": [
    "kor = float(input(\"국어성적 입력 ; \"))\n",
    "eng = float(input(\"영어성적 입력 ; \"))\n",
    "math = float(input(\"수학성적 입력 ; \"))\n",
    "\n",
    "avg = (kor + eng + math) / 3\n",
    "\n",
    "if avg >= 60 :\n",
    "    print(\"성적 평균은 \", avg, \"이며, 합격입니다.\")\n",
    "else:\n",
    "    print(\"성적 평균은 \", avg, \"이며, 불합격입니다.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "832f5997",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "국어성적 입력 ; 100\n",
      "영어성적 입력 ; 100\n",
      "수학성적 입력 ; 5\n",
      "성적 평균은  68.33333333333333 이지만 50점 미안 과락이 있어서, 불합격입니다.\n"
     ]
    }
   ],
   "source": [
    "kor = float(input(\"국어성적 입력 ; \"))\n",
    "eng = float(input(\"영어성적 입력 ; \"))\n",
    "math = float(input(\"수학성적 입력 ; \"))\n",
    "\n",
    "avg = (kor + eng + math) / 3\n",
    "\n",
    "if avg >= 60 and kor >= 50 and eng >= 50 and math >= 50 :\n",
    "    print(\"성적 평균은 \", avg, \"이며, 과락과목도 없기 때문에 합격입니다.\")\n",
    "else:\n",
    "    if avg >= 60 :\n",
    "        print(\"성적 평균은 \", avg, \"이지만 50점 미안 과락이 있어서, 불합격입니다.\")\n",
    "    else:\n",
    "        print(\"성적 평균은 \", avg, \"이며, 불합격입니다.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "5bff402a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "국어성적 입력 ; 60\n",
      "영어성적 입력 ; 60\n",
      "수학성적 입력 ; 60\n",
      "성적 평균은  60.0 이며, 과락과목도 없기 때문에 합격입니다.\n"
     ]
    }
   ],
   "source": [
    "kor = float(input(\"국어성적 입력 ; \"))\n",
    "eng = float(input(\"영어성적 입력 ; \"))\n",
    "math = float(input(\"수학성적 입력 ; \"))\n",
    "\n",
    "avg = (kor + eng + math) / 3\n",
    "\n",
    "if avg >= 60 and kor >= 50 and eng >= 50 and math >= 50 :\n",
    "    print(\"성적 평균은 \", avg, \"이며, 과락과목도 없기 때문에 합격입니다.\")\n",
    "else:\n",
    "    if avg >= 60 :\n",
    "        print(\"성적 평균은 \", avg, \"이지만 50점 미안 과락이 있어서, 불합격입니다.\")\n",
    "    else:\n",
    "        print(\"성적 평균은 \", avg, \"이며, 불합격입니다.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "cb085603",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "국어성적 입력 ; 100\n",
      "영어성적 입력 ; 20\n",
      "수학성적 입력 ; 90\n",
      "성적 평균은  70.0 이지만 50점 미만 과락이 있어서, 불합격입니다.\n"
     ]
    }
   ],
   "source": [
    "kor = float(input(\"국어성적 입력 ; \"))\n",
    "eng = float(input(\"영어성적 입력 ; \"))\n",
    "math = float(input(\"수학성적 입력 ; \"))\n",
    "\n",
    "avg = (kor + eng + math) / 3\n",
    "\n",
    "if avg >= 60 :\n",
    "    if kor < 50 or eng < 50 or math < 50 :\n",
    "        print(\"성적 평균은 \", avg, \"이지만 50점 미만 과락이 있어서, 불합격입니다.\")\n",
    "    else :\n",
    "        print(\"성적 평균은 \", avg, \"이며, 과락과목도 없기 때문에 합격입니다.\")\n",
    "else :\n",
    "    print(\"성적 평균은 \", avg, \"이며, 불합격입니다.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "63ed5017",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "키를 m 단위로 입력해 주세요 ; 1.52\n",
      "몸무게를 kg 단위로 입력해 주세요 ; 32\n",
      "BMI 지수는  13.850415512465373 이며, 저체중 상태입니다.\n"
     ]
    }
   ],
   "source": [
    "height = float(input(\"키를 m 단위로 입력해 주세요 ; \"))\n",
    "weight = float(input(\"몸무게를 kg 단위로 입력해 주세요 ; \"))\n",
    "\n",
    "bmi = weight / (height * height)\n",
    "\n",
    "if bmi < 18.5 :\n",
    "    print(\"BMI 지수는 \", bmi, \"이며, 저체중 상태입니다.\")\n",
    "elif bmi < 23 :\n",
    "    print(\"BMI 지수는 \", bmi, \"이며, 정상 상태입니다.\")\n",
    "elif bmi < 25 :\n",
    "    print(\"BMI 지수는 \", bmi, \"이며, 과체중 상태입니다.\")\n",
    "elif bmi < 30 :\n",
    "    print(\"BMI 지수는 \", bmi, \"이며, 비만1 상태입니다.\")\n",
    "elif bmi < 40 :\n",
    "    print(\"BMI 지수는 \", bmi, \"이며, 비만2 상태입니다.\")\n",
    "else :\n",
    "    print(\"BMI 지수는 \", bmi, \"이며, 심각한비만3 상태입니다.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "a805cee7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "input your score ; 40\n",
      "your score is  40  and then grade is  F\n"
     ]
    }
   ],
   "source": [
    "score = input(\"input your score ; \")\n",
    "score = int(score)\n",
    "\n",
    "if score >= 80 :\n",
    "    grade = \"A\"\n",
    "elif score >= 60 :\n",
    "    grade = \"B\"\n",
    "elif score >= 50 :\n",
    "    grade = \"C\"\n",
    "else :\n",
    "    grade = \"F\"\n",
    "\n",
    "print(\"your score is \", score, \" and then grade is \", grade)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "3dde0691",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "첫번째 정수 입력하세요 ; 3\n",
      "두번째 정수 입력하세요 ; 4\n",
      "세번째 정수 입력하세요 ; 2\n",
      "3 4 2  중에 가장 큰 수는  4\n"
     ]
    }
   ],
   "source": [
    "n1 = int(input(\"첫번째 정수 입력하세요 ; \"))\n",
    "n2 = int(input(\"두번째 정수 입력하세요 ; \"))\n",
    "n3 = int(input(\"세번째 정수 입력하세요 ; \"))\n",
    "\n",
    "largest = 0\n",
    "\n",
    "if largest < n1 :\n",
    "    largest = n1\n",
    "if largest < n2 :\n",
    "    largest = n2\n",
    "if largest < n3 :\n",
    "    largest = n3\n",
    "\n",
    "print(n1, n2, n3, \" 중에 가장 큰 수는 \", largest)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "7297375e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "생년월일을 입력하세요 ; 20010907\n",
      "당신의 나이는  20 입니다.\n"
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
    "if Birthdate > \"20220524\" :\n",
    "    print(\"나이를 계산할 수 없습니다.\")\n",
    "\n",
    "else :\n",
    "    age = 2022 - int(Year)\n",
    "    \n",
    "if Month > \"05\" :\n",
    "    age = age - 1\n",
    "    \n",
    "print(\"당신의 나이는 \", age, \"입니다.\")"
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
