def rotate(x, i):
    i %= len(x)
    x[:i] = reversed(x[:i])
    x[i:] = reversed(x[i:])
    x[:] = reversed(x)
    return x


def solution(encrypted_text, key, rotation):
    answer = ''
    encrypted_text_tmp = []
    key_tmp = []
    for i in encrypted_text:
        encrypted_text_tmp.append(ord(i)-96)
    
    for i in key:
        key_tmp.append(ord(i)-96)

    
    rotate(encrypted_text_tmp, rotation)

    for i in range(len(encrypted_text_tmp)):
        answer += chr((encrypted_text_tmp[i] - key_tmp[i])%26+96)

    return answer

print(solution("qyyigoptvfb", "abcdefghijk", 3))
