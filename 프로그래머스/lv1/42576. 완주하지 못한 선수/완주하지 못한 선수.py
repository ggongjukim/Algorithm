def solution(participant, completion):
    participant = sorted(participant)
    completion = sorted(completion)
    answer = participant[-1]
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    return answer