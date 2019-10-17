import re

def findMatchedText(text, regexp):
	matches = re.findall(regexp, text)
	result = []

	for match in matches:
		result.append(match)

	# set을 이용하여 중복제거
	return list(set(result))
