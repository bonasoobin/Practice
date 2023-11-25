def solution(letter):

    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}   

    
    answer = ''
    a = []
    letter = letter.split(' ')
    for i in range(len(list(letter))):
        a.append(morse[letter[i]])
    answer = answer.join(a)
    return answer