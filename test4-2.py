{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e23715a3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "60\n",
      "70\n",
      "80\n",
      "90\n",
      "100\n",
      "last value =  100\n"
     ]
    }
   ],
   "source": [
    "# 출력 결과는?\n",
    "\n",
    "value = 50\n",
    "\n",
    "while value < 100 :\n",
    "    value = value + 10\n",
    "    print(value)\n",
    "    \n",
    "print(\"last value = \", value)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "4a7a7cf6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "95\n",
      "90\n",
      "85\n",
      "80\n",
      "75\n",
      "70\n",
      "65\n",
      "60\n",
      "55\n",
      "50\n",
      "45\n",
      "40\n",
      "35\n",
      "30\n",
      "25\n",
      "20\n",
      "15\n",
      "10\n",
      "5\n",
      "0\n",
      "last value =  0\n"
     ]
    }
   ],
   "source": [
    "# 출력 결과는?\n",
    "\n",
    "value = 100\n",
    "\n",
    "while value > 0 :\n",
    "    value = value - 5\n",
    "    print(value)\n",
    "    \n",
    "print(\"last value = \", value)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "5508aa4c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "^\n",
      "@@\n",
      "^^^\n",
      "@@@@\n",
      "^^^^^\n",
      "@@@@@@\n",
      "^^^^^^^\n",
      "@@@@@@@@\n",
      "^^^^^^^^^\n",
      "Final number =  9\n"
     ]
    }
   ],
   "source": [
    "for i in range(10) :\n",
    "    if i%2 == 0 :\n",
    "        print(\"@\" * i)\n",
    "    else :\n",
    "        print(\"^\" * i)\n",
    "        \n",
    "print(\"Final number = \", i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "32d48168",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello\n",
      "Hello\n",
      "Hello\n",
      "Hello\n",
      "Hello\n",
      "There\n"
     ]
    }
   ],
   "source": [
    "# 'Hello'를 5번, 'There'를 한 번 출력\n",
    "\n",
    "for i in range(5) :\n",
    "    print(\"Hello\")\n",
    "\n",
    "print(\"There\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "f9adb046",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello\n",
      "There\n",
      "Hello\n",
      "There\n",
      "Hello\n",
      "There\n",
      "Hello\n",
      "There\n",
      "Hello\n",
      "There\n"
     ]
    }
   ],
   "source": [
    "# 'Hello', 'There' 를 둘 다 5번 출력\n",
    "\n",
    "for i in range(5) :\n",
    "    print(\"Hello\")\n",
    "    print(\"There\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "ef25c337",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "i =  1\n",
      "n =  2 ***\n",
      "i =  2\n",
      "n =  4 ***\n",
      "i =  3\n",
      "n =  6 ***\n",
      "i =  4\n",
      "n =  8 ***\n",
      "i =  5\n",
      "n =  10 ***\n",
      "i =  6\n",
      "n =  12 ***\n",
      "i =  7\n",
      "n =  14 ***\n",
      "i =  8\n",
      "n =  16 ***\n",
      "i =  9\n",
      "n =  18 ***\n",
      "i =  10\n",
      "n =  20 ***\n"
     ]
    }
   ],
   "source": [
    "# 1\n",
    "\n",
    "i = 0\n",
    "j = 10\n",
    "n = 0\n",
    "\n",
    "while i < j :\n",
    "    i = i + 1\n",
    "    n = n + 2\n",
    "    \n",
    "    print(\"i = \", i)\n",
    "    print(\"n = \", n, \"***\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "72392e1f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "i =  10\n",
      "i ** 2 =  100\n",
      "i =  1\n",
      "i ** 2 =  1\n",
      "i =  5\n",
      "i ** 2 =  25\n",
      "i =  9\n",
      "i ** 2 =  81\n",
      "i =  21\n",
      "i ** 2 =  441\n",
      "i =  53\n",
      "i ** 2 =  2809\n"
     ]
    }
   ],
   "source": [
    "# 2\n",
    "\n",
    "for i in [10,1, 5, 9, 21, 53] :\n",
    "    print(\"i = \", i)\n",
    "    print(\"i ** 2 = \", i ** 2)"
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
