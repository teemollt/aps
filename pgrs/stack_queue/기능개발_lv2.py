def solution(progresses, speeds):
    answer = []
    n = len(speeds)
    done = [0] * n
    for i in range(n):
        cnt = 0
        while progresses[i] < 100:
            for j in range(n):
                if not done[j]:
                    progresses[j] += speeds[j]
        for k in range(i, n):
            if progresses[k] >= 100 and not done[k]:
                done[k] = 1
                cnt += 1
            else:
                break
        if cnt > 0:
            answer.append(cnt)
    return answer

# 재미로 js로도 풀어봄 풀이법도 다르게
# function solution(progresses, speeds) {
#     var answer = [];
#     var left = [];
#     var n = progresses.length;
#     for (var i = 0; i < n; i++) {
#         var pLeft = (100 - progresses[i])/speeds[i];
#         if (pLeft%1 != 0) {
#             pLeft = parseInt(pLeft) + 1;
#         };
#     left.push(pLeft);
#     }
#     var idx = 0
#     while (idx < n) {
#         var cnt = 0;
#         for (var i = idx; i < n; i++) {
#             if (left[i] <= left[idx]) {
#                 cnt += 1
#             }
#             else {break}
#         }
#         idx = i
#         if (cnt > 0) {
#             answer.push(cnt)
#         }
#     }
#     return answer;
# }