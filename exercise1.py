# import step, fix the "Module ‘sys‘ Has No Attribute ‘argv‘" bug.
import sys
sys.argv=['']

from matplotlib import pyplot as plt
import math
import xlwt


def EulerAndQuaternionTransform(input_data):
    data_len = len(input_data)
    angle_is_not_rad = False
    if data_len == 3:
        r = 0
        p = 0
        y = 0
        if angle_is_not_rad:  # 180 ->pi
            r = math.radians(input_data[0])
            p = math.radians(input_data[1])
            y = math.radians(input_data[2])
        else:
            r = input_data[0]
            p = input_data[1]
            y = input_data[2]
        sinp = math.sin(p / 2)
        siny = math.sin(y / 2)
        sinr = math.sin(r / 2)

        cosp = math.cos(p / 2)
        cosy = math.cos(y / 2)
        cosr = math.cos(r / 2)
        w = cosr * cosp * cosy + sinr * sinp * siny
        x = sinr * cosp * cosy - cosr * sinp * siny
        y = cosr * sinp * cosy + sinr * cosp * siny
        z = cosr * cosp * siny - sinr * sinp * cosy
        return [w, x, y, z]
    elif data_len == 4:
        w = input_data[0]
        x = input_data[1]
        y = input_data[2]
        z = input_data[3]

        r = math.atan2(2 * (w * x + y * z), 1 - 2 * (x * x + y * y))
        p = math.asin(2 * (w * y - z * x))
        y = math.atan2(2 * (w * z + x * y), 1 - 2 * (y * y + z * z))
        if angle_is_not_rad:  # pi ->180
            r = math.degrees(r)
        p = math.degrees(p)
        y = math.degrees(y)
        return [r, p, y]


def paint(x=1, y=2):
    time = []
    tx = []
    ty = []
    tz = []
    qx = []
    qy = []
    qz = []
    qw = []
    roll = []
    pitch = []
    yaw = []
    with open('07.txt', 'r') as f:
        data = f.readlines()
        for i in range(len(data)):
            temp_data = data[i].split(' ')
            time.append(float(temp_data[0]))
            tx.append(float(temp_data[1]))
            ty.append(float(temp_data[2]))
            tz.append(float(temp_data[3]))
            temp_q = EulerAndQuaternionTransform([tx[-1], ty[-1], tz[-1]])
            qx.append(temp_q[0])
            qy.append(temp_q[1])
            qz.append(temp_q[2])
            qw.append(temp_q[3])
            roll.append(float(temp_data[-3]))
            pitch.append(float(temp_data[-2]))
            yaw.append(float(temp_data[-1]))

   # f = xlwt.Workbook()
   # sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)
   # for i in range(len(tx)):
      #  sheet1.write(i, 0, time[i])
      #  sheet1.write(i, 1, tx[i])
      #  sheet1.write(i, 2, ty[i])
      # sheet1.write(i, 3, tz[i])
      #  sheet1.write(i, 4, qx[i])
      # sheet1.write(i, 5, qy[i])
      # sheet1.write(i, 6, qz[i])
      #  sheet1.write(i, 7, qw[i])
   # f.save('data.xlsx')


    fig1, axs = plt.subplots(3, 1)
    axs[0].scatter(time, tx, marker='o', c='r', s=1)
    axs[0].set_ylabel('tx(m)')
    axs[1].scatter(time, ty, marker='o', c='y', s=1)
    axs[1].set_ylabel('ty(m)')
    axs[2].scatter(time, tz, marker='o', c='b', s=1)
    axs[2].set_ylabel('tz(m)')
    axs[2].set_xlabel('time(s)')
    axs[0].set_title('xyz scatter view')
    plt.savefig('xyz scatter view.png')
    plt.show()

    fig2, axs = plt.subplots(4, 1)
    axs[0].scatter(time, qx, marker='o', c='r', s=1)
    axs[0].set_ylabel('qx(m)')
    axs[1].scatter(time, qy, marker='o', c='y', s=1)
    axs[1].set_ylabel('qy(m)')
    axs[2].scatter(time, qz, marker='o', c='b', s=1)
    axs[2].set_ylabel('qz(m)')
    axs[3].scatter(time, qw, marker='o', c='k', s=1)
    axs[3].set_ylabel('qw(m)')
    axs[3].set_xlabel('time(s)')
    axs[0].set_title('qxyzw scatter view')
    plt.savefig('qxyzw scatter view.png')
    plt.show()

    fig3, axs = plt.subplots(3, 1)
    axs[0].scatter(time, roll, marker='o', c='r', s=1)
    axs[0].set_ylabel('roll(m)')
    axs[1].scatter(time, pitch, marker='o', c='y', s=1)
    axs[1].set_ylabel('pitch(m)')
    axs[2].scatter(time, yaw, marker='o', c='b', s=1)
    axs[2].set_ylabel('yaw(m)')
    axs[2].set_xlabel('time(s)')
    axs[0].set_title('pry scatter view')
    plt.savefig('pry scatter view.png')
    plt.show()

    fig4, axs = plt.subplots(3, 1)
    axs[0].plot(time, tx, c='r')
    axs[0].set_ylabel('tx(m)')
    axs[1].plot(time, ty, c='y')
    axs[1].set_ylabel('ty(m)')
    axs[2].plot(time, tz, c='b')
    axs[2].set_ylabel('tz(m)')
    axs[2].set_xlabel('time(s)')
    axs[0].set_title('xyz line view')
    plt.savefig('xyz line view.png')
    plt.show()

    fig5, axs = plt.subplots(4, 1)
    axs[0].plot(time, qx, c='r')
    axs[0].set_ylabel('qx(m)')
    axs[1].plot(time, qy, c='y')
    axs[1].set_ylabel('qy(m)')
    axs[2].plot(time, qz, c='b')
    axs[2].set_ylabel('qz(m)')
    axs[3].plot(time, qw, c='k')
    axs[3].set_ylabel('qw(m)')
    axs[3].set_xlabel('time(s)')
    axs[0].set_title('qxyzw line view')
    plt.savefig('qxyzw line view.png')
    plt.show()

    fig6, axs = plt.subplots(3, 1)
    axs[0].plot(time, roll, c='r')
    axs[0].set_ylabel('roll(m)')
    axs[1].plot(time, pitch, c='y')
    axs[1].set_ylabel('pitch(m)')
    axs[2].plot(time, yaw, c='b')
    axs[2].set_ylabel('yaw(m)')
    axs[2].set_xlabel('time(s)')
    axs[0].set_title('pry line view')
    plt.savefig('pry line view.png')
    plt.show()


if __name__ == "__main__":
    paint()
