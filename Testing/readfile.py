# Name: Kenneth Granger
# Date: 2023-09-21
# Course: COSC3143 Pi and Python
# Assignment: Exam 01

def main():
	file_name = input("Please input a file name: ")
	wordlist = sorted(open(file_name, "r").read().split())
	print("Total number of words is", len(wordlist))
	for i in wordlist:
		print(i)


if __name__ == "__main__":
	main()
