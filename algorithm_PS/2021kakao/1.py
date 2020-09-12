def solution(new_id):
    new_id = new_id.lower()
    
    for i in new_id:
        if i.islower() or i in ["1","2","3","4","5","6","7","8","9","0"] or i == '_' or i == '-' or i == '.':
            continue
        
        new_id = new_id.replace(i, "")

    while True:
        if '..' in new_id:
            new_id = new_id.replace('..', '.')
        else:
            break

    if new_id:
        if new_id[0] == '.':
            new_id = new_id[1:]
        
    if new_id:  
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    if not(new_id):
        new_id = "a"
    
    if len(new_id) >= 16:
        new_id = new_id[0:15]

        if new_id[-1] == '.':
            new_id = new_id[:-1]

    if len(new_id) <= 2:
        tmp = new_id[-1]
        while len(new_id) != 3:
            new_id = new_id + tmp



    return new_id

new_id = "...!@BaT#*..y.abcdefghijklm"
new_id = "z-+.^."
new_id = "=.="
new_id = "123_.def"
new_id =	"abcdefghijklmn.p"

print(solution(new_id))