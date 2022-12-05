# this function find weak pareto improvement for cancel at least 1 edge in the cycle.
def find_weak_pareto_improvement(allocation: list[list[float]], valuations: list[list[float]], cycle: list):
    for i in range(0, len(cycle) - 2, 2):  # pass over all the couples of players
        for j in range(0, len(valuations)):  # pass over all the objects
            if j == cycle[i + 1]:  # if this the same object- continue to the next
                continue
            else:
                if allocation[j][cycle[i]] == 0:  # this object dont share
                    continue
                elif allocation[j][cycle[i + 2]] == 0:  # this object dont share
                    continue
                else:  # this object share
                    first_obj_alloc = allocation[cycle[i + 1]][cycle[i]]
                    sec_obj_alloc = allocation[j][cycle[i + 2]]
                    lose_first_player = first_obj_alloc * valuations[cycle[i + 1]][
                        cycle[i]]  # how much the first player will lose?
                    win_first_player = allocation[j][cycle[i]] * valuations[j][
                        cycle[i]]  # how much the first player will win?
                    lose_sec_player = sec_obj_alloc * valuations[j][
                        cycle[i + 2]]  # how much the second player will lose?
                    win_sec_player = allocation[cycle[i + 1]][cycle[i + 2]] * valuations[cycle[i + 1]][
                        cycle[i + 2]]  # how much the second player will win?
                    if win_first_player < lose_first_player:  # the first player cannot give up on all this object,
                        # find another
                        break
                    elif win_sec_player < lose_sec_player:  # the second player cannot give up on all this object,
                        # hand over part
                        max_los = allocation[j][cycle[i]] / win_sec_player
                        allocation[cycle[i + 1]][cycle[i]] = 0  # update allocation matrix
                        allocation[cycle[i + 1]][cycle[i + 2]] += first_obj_alloc
                        allocation[j][cycle[i + 2]] -= max_los
                        allocation[j][cycle[i]] += max_los
                        return allocation
                    else:  # update allocation matrix
                        allocation[cycle[i + 1]][cycle[i]] = 0
                        allocation[cycle[i + 1]][cycle[i + 2]] += first_obj_alloc
                        allocation[j][cycle[i + 2]] -= first_obj_alloc
                        allocation[j][cycle[i]] += first_obj_alloc
                        return allocation


if __name__ == '__main__':
    allo = [[0, 1], [0, 1], [0.5, 0.5], [0.6, 0.4]]
    val = [[15, 40], [15, 25], [40, 30], [30, 5]]
    cy = [0, 2, 1, 3, 0]
    print(find_weak_pareto_improvement(allo, val,
                                       cy))
