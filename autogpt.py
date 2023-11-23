import time
import pyautogui
import pyperclip



def pyautoguifunc(content, number_of_times, counter, timing_interval):
	
	for lines in range(counter, counter + number_of_times):
		pyperclip.copy(content[lines])
		pyautogui.click()
		pyautogui.hotkey('ctrl', 'v')
		pyautogui.hotkey('enter')
		print(f"Chunk number {lines} printed")
		time.sleep(timing_interval)
	return counter+number_of_times

def content_return(files, content_chunk, splitter):

# Splitting the text by the splitter and removing any leading or trailing newlines from each part
	content = [part.strip() for part in files.read().split(splitter) if part.strip()]
	if(content_chunk != ""):
		counter = 0
		for lines in content:
			if content_chunk in lines:
				break
			else:
				counter+=1
		
		counter -= 1
	else:
		counter = 0
	return content, counter



timing = int(input("Timing interval: "))
fileinputs = str(input("Input file:"))
files = open(f"{fileinputs}.txt", "r", encoding = "utf-8")
content_chunk = str(input("A part of the current prompt to be submitted\nIf starting from the first prompt, press enter\n:"))
splitter = str(input("Splitter text:"))
print("Move to ChatGPT. Make sure to click on the form field.")
content_, counter_ = content_return(files, content_chunk, splitter)



time.sleep(5)

while True:
	print("Note that the program is built for ChatGPT-4. It will run for 30 times and then pause for 3 hours. Remove this if you want it to work for ChatGPT-3 more efficiently")
	counter_ = pyautoguifunc(content_, 30, counter_, timing)
	time.sleep(60*60*3)
	
