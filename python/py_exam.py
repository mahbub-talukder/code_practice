
"""Authentication Tokens problem"""
#solution

def numberOftoken(expireLimit,commands):
    
    token_storage = {}
    for command in commands:
        cmd =  command[0]
        token_id =  command[1]
        time =  command[2]
        # print("time-->", time)

        if cmd == 0:
            token_storage[token_id] = expireLimit
        
        if cmd == 1:
            if token_id in token_storage and token_storage[token_id] >= time:
                token_storage[token_id] = token_storage[token_id] + expireLimit
                

    active_token = []
    print("token_storage-->",token_storage)
    last_cmd = commands[-1]
    for token in token_storage:
       if token_storage[token] >=  last_cmd[2]:
           active_token.append(str(token))


    if len(active_token) == 0:
        return 0
    else:
        return ",".join(active_token)


commands = [
    [0,1,1],
    [1,1,3],
    [0,2,3],
    [1,2,5],
    [0,3,6]
]     

results = numberOftoken(4,commands)
print("results-->", results)
