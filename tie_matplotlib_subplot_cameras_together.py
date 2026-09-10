import numpy as np
import matplotlib.pyplot as plt


def on_move(event):
    '''
    For a figure with multiple 3D subplots, this function is used
    as a callback whenever there is an event in the figure viewer
    window, such that the view for all subplots is tied together.

    Expected use case:
    fig.canvas.mpl_connect('motion_notify_event', on_move)
    where fig is the figure of interest, and defined in the
    namespace this callback is called from.
    '''
    event_ind = None
    list_axes = fig.get_axes()
    for checking_ind, checking_ax in enumerate(list_axes):
        if event.inaxes == checking_ax:
            event_ind = checking_ind
            break
    if event_ind is None:
        return

    adjustment_made = False
    for action_ind in range(len(list_axes)):
        if action_ind == event_ind:
            continue
        action_ax = list_axes[action_ind]
        if checking_ax.button_pressed in checking_ax._rotate_btn:
            action_ax.view_init(elev=checking_ax.elev, azim=checking_ax.azim, roll=checking_ax.roll)
            adjustment_made = True
        elif checking_ax.button_pressed in checking_ax._zoom_btn:
            action_ax.set_xlim3d(checking_ax.get_xlim3d())
            action_ax.set_ylim3d(checking_ax.get_ylim3d())
            action_ax.set_zlim3d(checking_ax.get_zlim3d())
            adjustment_made = True
    if adjustment_made:
        fig.canvas.draw_idle()


if __name__ == "__main__":
    num_points = 100
    x = np.random.random(num_points)
    y = np.random.random(num_points)
    z = np.random.random(num_points)


    fig = plt.figure()
    # fig.subplots_adjust(left=0, right=1, top=1, bottom=0, wspace=0)
    ax  = fig.add_subplot(2, 2, 1, projection='3d')
    ax2 = fig.add_subplot(2, 2, 2, projection='3d')
    ax3 = fig.add_subplot(2, 2, 3, projection='3d')
    ax4 = fig.add_subplot(2, 2, 4, projection='3d')

    for ax_now in (ax, ax2, ax3, ax4):
        ax_now.scatter(x,y,z)

    fig.canvas.mpl_connect('motion_notify_event', on_move)

    plt.show()