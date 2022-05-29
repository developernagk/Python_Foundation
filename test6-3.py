{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c5027cd4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I/O error: [Errno 2] No such file or directory: 'myfile.txt'\n"
     ]
    }
   ],
   "source": [
    "# check File IO\n",
    "\n",
    "import sys\n",
    "\n",
    "try :\n",
    "    inf = open('myfile.txt', 'r')\n",
    "    s = f.readline()\n",
    "    \n",
    "except IOError as err :\n",
    "    print(\"I/O error: {0}\".format(err))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c202336b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# check zero dividion\n",
    "\n",
    "import sys\n",
    "\n",
    "def divide(x, y) :\n",
    "    try :\n",
    "        result = x / y\n",
    "        \n",
    "    except ZeroDividionError :\n",
    "        print(\"division by zero!\")\n",
    "        \n",
    "    else :\n",
    "        print(\"result is \", result)\n",
    "        \n",
    "    finally :\n",
    "        print(\"executing finally clause\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "bd6a7e36",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please enter an integer : as\n",
      "Oops! That was no valid number. Try again...\n",
      "Please enter an integer : 0.9\n",
      "Oops! That was no valid number. Try again...\n",
      "Please enter an integer : 2\n"
     ]
    }
   ],
   "source": [
    "# try: Exception 1\n",
    "\n",
    "import sys\n",
    "\n",
    "while True :\n",
    "    try :\n",
    "        x = int(input(\"Please enter an integer : \"))\n",
    "        break\n",
    "    except ValueError :\n",
    "        print(\"Oops! That was no valid number. Try again...\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "269b54b2",
   "metadata": {},
   "outputs": [],
   "source": [
    "# try Exception 2\n",
    "\n",
    "import sys\n",
    "\n",
    "try :\n",
    "    x = 1 / 10\n",
    "    \n",
    "except ZeroDivisionError as err :\n",
    "    print('Handing run-time error : ', err)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "e90d9609",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I/O error : [Errno 2] No such file or directory: 'myfile.txt'\n"
     ]
    }
   ],
   "source": [
    "# Except with Multiple Exceptions\n",
    "\n",
    "import sys\n",
    "\n",
    "try :\n",
    "    f = open('myfile.txt', 'r')\n",
    "    s = f.readline()\n",
    "    i = int(s.strip())\n",
    "except IOError as err :\n",
    "    print(\"I/O error : {0}\".format(err))\n",
    "except ValueError :\n",
    "    print(\"Could not convert data to an integer.\")\n",
    "except :\n",
    "    print(\"Unexpected error : \", sys.exc_info()[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "9d40e3f8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Going to close the file\n",
      "['This is my test file for exception handing!!\\n', '===================================']\n"
     ]
    }
   ],
   "source": [
    "# Try-Finally 사용\n",
    "\n",
    "try :\n",
    "    fh = open(\"t.txt\", \"w\")\n",
    "    try :\n",
    "        fh.write(\"This is my test file for exception handing!!\\n\")\n",
    "        fh.write(\"=\" * 35)\n",
    "    finally :\n",
    "        print(\"Going to close the file\")\n",
    "        fh.close()\n",
    "        fh = open(\"t.txt\", \"r\")\n",
    "        print(fh.readlines())\n",
    "        fh.close()\n",
    "        \n",
    "except IOError :\n",
    "    print(\"Error : can\\'t find file or read data\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "da0a1e2a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "32.0\n",
      "451.00399999999996\n",
      "Colder than absolute zero!\n"
     ]
    },
    {
     "ename": "AssertionError",
     "evalue": "None",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mAssertionError\u001b[0m                            Traceback (most recent call last)",
      "Input \u001b[0;32mIn [11]\u001b[0m, in \u001b[0;36m<cell line: 9>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      7\u001b[0m \u001b[38;5;28mprint\u001b[39m(KToFahrenheit(\u001b[38;5;241m273\u001b[39m))\n\u001b[1;32m      8\u001b[0m \u001b[38;5;28mprint\u001b[39m(KToFahrenheit(\u001b[38;5;241m505.78\u001b[39m))\n\u001b[0;32m----> 9\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[43mKToFahrenheit\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;241;43m-\u001b[39;49m\u001b[38;5;241;43m5\u001b[39;49m\u001b[43m)\u001b[49m)\n",
      "Input \u001b[0;32mIn [11]\u001b[0m, in \u001b[0;36mKToFahrenheit\u001b[0;34m(Temperature)\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mKToFahrenheit\u001b[39m(Temperature) :\n\u001b[0;32m----> 4\u001b[0m     \u001b[38;5;28;01massert\u001b[39;00m(Temperature \u001b[38;5;241m>\u001b[39m\u001b[38;5;241m=\u001b[39m \u001b[38;5;241m0\u001b[39m), \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mColder than absolute zero!\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m      5\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m((Temperature \u001b[38;5;241m-\u001b[39m \u001b[38;5;241m273\u001b[39m) \u001b[38;5;241m*\u001b[39m \u001b[38;5;241m1.8\u001b[39m) \u001b[38;5;241m+\u001b[39m \u001b[38;5;241m32\u001b[39m\n",
      "\u001b[0;31mAssertionError\u001b[0m: None"
     ]
    }
   ],
   "source": [
    "# assert\n",
    "\n",
    "def KToFahrenheit(Temperature) :\n",
    "    assert(Temperature >= 0), print(\"Colder than absolute zero!\")\n",
    "    return((Temperature - 273) * 1.8) + 32\n",
    "\n",
    "print(KToFahrenheit(273))\n",
    "print(KToFahrenheit(505.78))\n",
    "print(KToFahrenheit(-5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "f20abe7a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a positive number : -3\n",
      "Only positive numbers are allowed!\n"
     ]
    },
    {
     "ename": "AssertionError",
     "evalue": "None",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mAssertionError\u001b[0m                            Traceback (most recent call last)",
      "Input \u001b[0;32mIn [13]\u001b[0m, in \u001b[0;36m<cell line: 4>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;66;03m# assert\u001b[39;00m\n\u001b[1;32m      3\u001b[0m num \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mint\u001b[39m(\u001b[38;5;28minput\u001b[39m(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mEnter a positive number : \u001b[39m\u001b[38;5;124m'\u001b[39m))\n\u001b[0;32m----> 4\u001b[0m \u001b[38;5;28;01massert\u001b[39;00m(num \u001b[38;5;241m>\u001b[39m \u001b[38;5;241m0\u001b[39m), \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mOnly positive numbers are allowed!\u001b[39m\u001b[38;5;124m'\u001b[39m)\n\u001b[1;32m      6\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mnumber is \u001b[39m\u001b[38;5;124m\"\u001b[39m, num)\n",
      "\u001b[0;31mAssertionError\u001b[0m: None"
     ]
    }
   ],
   "source": [
    "# assert\n",
    "\n",
    "num = int(input('Enter a positive number : '))\n",
    "assert(num > 0), print('Only positive numbers are allowed!')\n",
    "\n",
    "print(\"number is \", num)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "8a596438",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your age : 130\n",
      "나이는 1세에서 100세까지만 입력 가능!\n"
     ]
    },
    {
     "ename": "AssertionError",
     "evalue": "None",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mAssertionError\u001b[0m                            Traceback (most recent call last)",
      "Input \u001b[0;32mIn [15]\u001b[0m, in \u001b[0;36m<cell line: 4>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;66;03m# assert\u001b[39;00m\n\u001b[1;32m      3\u001b[0m age \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mint\u001b[39m(\u001b[38;5;28minput\u001b[39m(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mEnter your age : \u001b[39m\u001b[38;5;124m'\u001b[39m))\n\u001b[0;32m----> 4\u001b[0m \u001b[38;5;28;01massert\u001b[39;00m(age \u001b[38;5;241m>\u001b[39m \u001b[38;5;241m1\u001b[39m \u001b[38;5;129;01mand\u001b[39;00m age \u001b[38;5;241m<\u001b[39m\u001b[38;5;241m=\u001b[39m \u001b[38;5;241m100\u001b[39m), \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m나이는 1세에서 100세까지만 입력 가능!\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m      6\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mage is \u001b[39m\u001b[38;5;124m\"\u001b[39m, age)\n",
      "\u001b[0;31mAssertionError\u001b[0m: None"
     ]
    }
   ],
   "source": [
    "# assert\n",
    "\n",
    "age = int(input('Enter your age : '))\n",
    "assert(age > 1 and age <= 100), print(\"나이는 1세에서 100세까지만 입력 가능!\")\n",
    "\n",
    "print(\"age is \", age)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "936a009a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your age : 130\n",
      "처리할 수 없는 숫자가 입력 되었습니다. 다시 입력해주세요\n",
      "Enter your age : 102\n",
      "처리할 수 없는 숫자가 입력 되었습니다. 다시 입력해주세요\n",
      "Enter your age : 50\n",
      "입력된 나이는  50 세 입니다.\n"
     ]
    }
   ],
   "source": [
    "# while\n",
    "\n",
    "age = int(input('Enter your age : '))\n",
    "\n",
    "while age < 1 or age > 100 :\n",
    "    print(\"처리할 수 없는 숫자가 입력 되었습니다. 다시 입력해주세요\")\n",
    "    age = int(input('Enter your age : '))\n",
    "    \n",
    "print(\"입력된 나이는 \", age, \"세 입니다.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "8bcedfd4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your age : 삼십세\n",
      "처리할 수 없는 문자가 입력되었습니다! 정수로 입력하세요\n",
      "Enter your age : 3\n"
     ]
    }
   ],
   "source": [
    "# try\n",
    "\n",
    "import sys\n",
    "\n",
    "while True :\n",
    "    try :\n",
    "        age = int(input('Enter your age : '))\n",
    "        break\n",
    "        \n",
    "    except ValueError :\n",
    "        print(\"처리할 수 없는 문자가 입력되었습니다! 정수로 입력하세요\")"
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
