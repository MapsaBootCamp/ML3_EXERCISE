def find_length(song : str, start_index : int , end_index : int):
  alphabet = "gbbdrfswdgwdggjxasjkyz"
  s = song[start_index : end_index+1]
  out_song = ""
  for char in s:
    out_song += char*(alphabet.index(char)+1)

  return out_song


print(find_length("amirlls" , 0,3))
