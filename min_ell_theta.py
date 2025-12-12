def learn_theta(data, colors):
    max_blue = float('-inf')
    min_red = float('inf')
    for i in range(len(data)):
        if colors[i] == 'blue':
            if data[i] > max_blue:
                max_blue = data[i]
        else:
            if data[i] < min_red:
                min_red = data[i]
    return (max_blue + min_red) / 2


def compute_ell(data, colors, theta):
    loss = 0
    for i in range(len(data)):
        if colors[i] == 'red' and data[i] <= theta:
            loss += 1
        elif colors[i] == 'blue' and data[i] > theta:
            loss += 1
    return float(loss)


def minimize_ell(data, colors):
    best_theta = None
    best_loss = float('inf')
    for theta in data:
        loss = compute_ell(data, colors, theta)
        if loss < best_loss:
            best_loss = loss
            best_theta = theta
    return best_theta


def minimize_ell_sorted(data, colors):
    n = len(data)
    total_blue = sum(1 for c in colors if c == 'blue')
    red_le_theta = 0
    blue_gt_theta = total_blue
    best_loss = red_le_theta + blue_gt_theta
    best_theta = data[0]
    for i in range(n):
        x = data[i]
        c = colors[i]
        if c == 'red':
            red_le_theta += 1
        else:
            blue_gt_theta -= 1
        loss = red_le_theta + blue_gt_theta
        if loss < best_loss:
            best_loss = loss
            best_theta = x
    return best_theta