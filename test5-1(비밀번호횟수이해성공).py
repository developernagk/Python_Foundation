{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a9871f28",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "비밀번호를 입력하세요 ; 4953\n",
      "비밀번호를 입력하세요 ; 343\n",
      "비밀번호를 입력하세요 ; 1234\n",
      "비밀번호가 정확합니다!\n"
     ]
    }
   ],
   "source": [
    "pwd = \"????\"\n",
    "count = 1\n",
    "\n",
    "while pwd != \"1234\" and count <= 3 :\n",
    "    pwd = input(\"비밀번호를 입력하세요 ; \")\n",
    "    count = count + 1\n",
    "\n",
    "if pwd == \"1234\" :\n",
    "    print(\"비밀번호가 정확합니다!\")\n",
    "elif count > 3 :\n",
    "    print(\"비밀번호 입력 오류가 3번 발생하여, 처리할 수 없습니다.\")\n",
    "else :\n",
    "    print(\"비밀번호가 정확합니다!\")"
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
