from heapq import heappush, heappop

# mostly finished, was too tired and renamed a variable without thinking, will fix tomorrow or so
def calculate_path(start_pos, final_pos, adjacent_rooms, heuristics_calc, calc_cost):
    room_set = list()
    prev_pos = dict()
    heappush(room_set, [0, start_pos])
    score_g, score_f = {start_pos: 0}, {start_pos: heuristics_calc(start_pos, final_pos)}
    while room_set:
        current_f, cur_pos = heappop(room_set)
        if cur_pos is final_pos:
            movement_list = list()
            while cur_pos in prev_pos:
                movement_list.append(cur_pos)
                cur_pos = prev_pos[cur_pos]
            movement_list.append(start_pos)
            return movement_list[::-1]
        for adjacent in adjacent_rooms(cur_pos):
            t_g_score = score_g[cur_pos] + calc_cost(cur_pos, adjacent)
            if adjacent not in score_g or t_g_score < score_g[adjacent]:
                prev_pos[adjacent] = cur_pos
                score_g[adjacent], score_f[adjacent] = t_g_score, t_g_score + heuristics_calc(adjacent, final_pos)
                heappush(room_set, (score_f[adjacent], adjacent))
    return None

def neighbors(position):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    return [(position[0] + direction[0], position[1] + direction[1]) for direction in directions]

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def cost(current_location, destined_location):
    return 1

if __name__ == '__main__':
    starter_position, ending_position = [(0, 0), (5, 5)]
    print(f"Path: {calculate_path(starter_position, ending_position, neighbors, heuristic, cost)}")
