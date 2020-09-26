if __name__ == '__main__':
    N = int(input())
    board = []
    result = []
    dirY = [-1, 0, 0, 1]
    dirX = [0, -1, 1, 0]

    for i in range(N):
        board.append(list(input()))

    num = 1
    for i in range(N):
        for j in range(N):
            if(board[i][j] == '1'):
                num = num + 1
                queue = [[i, j]]
                cnt = 1
                board[i][j] = num
                while queue :
                    h, y = queue[0][0], queue[0][1]
                    del queue[0]
                    for dir in range(4):
                        newY = h + dirY[dir]
                        newX = y + dirX[dir]

                        if 0 <= newY < N and 0 <= newX < N and board[newY][newX] == '1':
                            board[newY][newX] = num
                            queue.append([newY, newX])
                            cnt = cnt + 1

                result.append(cnt)
    result.sort()
    print("{0}".format(num -1))
    for i in range(len(result)):
        print(result[i])