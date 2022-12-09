# 11:18
import operator
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani


def get_dir(point1, point2):
    res = [0, 0]
    x_dir = point1[0] - point2[0]
    y_dir = point1[1] - point2[1]
    if point1[0] - point2[0] > 1:
        res[0] = 1
        res[1] = y_dir
    elif point1[0] - point2[0] < -1:
        res[0] = -1
        res[1] = y_dir
    elif point1[1] - point2[1] > 1:
        res[1] = 1
        res[0] = x_dir
    elif point1[1] - point2[1] < -1:
        res[1] = -1
        res[0] = x_dir
    return res


def part1():
    file = open("data9")
    lines = list(map(lambda x: x.split(" "), file.read().split("\n")))
    file.close()

    dirs = {'R': [1, 0], 'L': [-1, 0], 'U': [0, 1], 'D': [0, -1]}
    h_pos = [0, 0]
    t_pos = [0, 0]
    t_positions = set()

    for move in lines:
        for _ in range(int(move[1])):
            h_pos = tuple(map(operator.add, h_pos, dirs[move[0]]))
            t_pos = tuple(map(operator.add, t_pos, get_dir(h_pos, t_pos)))
            t_positions.add(t_pos)
    return len(t_positions)


print(part1())


# -------------------------- part 2
def get_dir(point1, point2):
    res = [0, 0]
    x_dir = min(point1[0] - point2[0], 1)
    y_dir = min(point1[1] - point2[1], 1)
    if point1[0] - point2[0] > 1:
        res[0] = 1
        res[1] = y_dir
    elif point1[0] - point2[0] < -1:
        res[0] = -1
        res[1] = y_dir
    elif point1[1] - point2[1] > 1:
        res[1] = 1
        res[0] = x_dir
    elif point1[1] - point2[1] < -1:
        res[1] = -1
        res[0] = x_dir
    return res


def part2():
    file = open("data9")
    lines = list(map(lambda x: x.split(" "), file.read().split("\n")))
    file.close()

    dirs = {'R': [1, 0], 'L': [-1, 0], 'U': [0, 1], 'D': [0, -1]}
    positions = [(0, 0) for _ in range(10)]
    t_positions = set()

    for move in lines:
        for _ in range(int(move[1])):
            positions[0] = tuple(map(operator.add, positions[0], dirs[move[0]]))
            for i in range(1, 10):
                positions[i] = tuple(map(operator.add, positions[i], get_dir(positions[i-1], positions[i])))
            t_positions.add(positions[-1])
            all_positions.append(positions.copy())
            # print(positions[0], positions[9])
    # print(t_positions)
    # print('\n'.join(map(str, positions)))
    return len(t_positions)


all_positions = [[(0, 0) for _ in range(10)]]

print(part2())


# Viz
def update(i):
    axs[0].clear()
    for pos in all_positions[i]:
        c = '#000000'
        alpha = 0.3
        if all_positions[i].index(pos) == 0:
            c = '#FF0000'
            alpha = 1
        elif all_positions[i].index(pos) == 9:
            c = '#0000FF'
            alpha = 1
            axs[1].scatter(pos[0], pos[1], c=c)
        axs[0].scatter(pos[0], pos[1], c=c, alpha=alpha)
    # size = max(ax.get_xlim()[1] // 5, 1 + abs(max(abs(max(all_positions[i], key=lambda a: abs(a[1]))[1]),
    #                                            abs(max(all_positions[i], key=lambda a: abs(a[0]))[0]))) % 10)
    size = 10
    rang = [-(x := 2 * size), x]
    # Set range and ticks.
    axs[0].set_xlim(rang)
    axs[0].set_ylim(rang)
    axs[0].set_xticks(np.arange(min(rang), max(rang) + 1, 0.2 * size))
    axs[0].set_yticks(np.arange(min(rang), max(rang) + 1, 0.2 * size))
    axs[0].set_box_aspect(1)
    axs[1].set_xlim(rang)
    axs[1].set_ylim(rang)
    axs[1].set_xticks(np.arange(min(rang), max(rang) + 1, 0.2 * size))
    axs[1].set_yticks(np.arange(min(rang), max(rang) + 1, 0.2 * size))
    axs[1].set_box_aspect(1)


fig, axs = plt.subplots(1, 2)
animation = ani.FuncAnimation(fig, update, frames=len(all_positions), interval=100, repeat=False)
paused = False


def toggle_pause(self):
    global paused
    if paused:
        animation.resume()
    else:
        animation.pause()
    paused = not paused


# print('\n'.join(map(str, all_positions)))

fig.canvas.mpl_connect('button_press_event', toggle_pause)

plt.show()

# 2585, 2553 Too high
