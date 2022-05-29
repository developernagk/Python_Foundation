{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "28a349b4",
   "metadata": {},
   "outputs": [],
   "source": [
    "word = input(\"단어입력 : \")\n",
    "test = input(\"찾을단어 : \")\n",
    "\n",
    "count = 0\n",
    "for char in word :\n",
    "    count = count + 1\n",
    "    if char == test :\n",
    "        print(count, \"번째에 \", test, \"가 있음\")\n",
    "        break\n",
    "    elif count >= len(word) :\n",
    "        print(\"아무것도 없음\")\n",
    "        break"
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
