def get_num_words(text):
    return len(text.split())
def character_counter(text):
	chara_count = {}
	for chara in text:
		if chara.lower() in chara_count:
			chara_count[chara.lower()] += 1
		else:
			chara_count[chara.lower()] = 1
	return chara_count
def sort_on(diction):
	return diction["num"]
def sort_list(chara_dict):
	sorted_list = []
	for key, value in chara_dict.items():
		sorted_list.append({"char": key, "num": value})
	sorted_list.sort(reverse=True, key=sort_on)
	return sorted_list
