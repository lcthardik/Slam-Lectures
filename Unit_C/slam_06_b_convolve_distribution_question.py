# Instead of moving a distribution, move (and modify) it using a convolution.
# 06_b_convolve_distribution
# Claus Brenner, 26 NOV 2012
from pylab import plot, show, ylim
from distribution import *

def move(distribution, delta):
    """Returns a Distribution that has been moved (x-axis) by the amount of
       delta."""
    return Distribution(distribution.offset + delta, distribution.values)

def convolve(a, b):
    """Convolve distribution a and b and return the resulting new distribution."""

    # --->>> Put your code here.
    lt=[]
    for i in range(len(a.values)):
        ov=len(lt)-i
        for j in range(len(b.values)):
            p=a.values[i]*b.values[j]
            if (ov):
                lt[len(lt)-ov]=lt[len(lt)-ov]+p
                ov-=1
            else:
                lt.append(p)
    a.offset=a.offset+b.offset
    a.values=lt
    print(lt)
    Distribution.normalize(a)

    return a# Replace this by your own result.


if __name__ == '__main__':
    arena = (0,1000)

    # Move 3 times by 20.
    moves = [20] * 50

    # Start with a known position: probability 1.0 at position 10.
    position = Distribution.unit_pulse(10)
    plot(position.plotlists(*arena)[0], position.plotlists(*arena)[1],
         drawstyle='steps')

    # Now move and plot.
    for m in moves:
        move_distribution = Distribution.triangle(m, 2)
        position = convolve(position, move_distribution)
        plot(position.plotlists(*arena)[0], position.plotlists(*arena)[1],
             drawstyle='steps')
        
        

    ylim(0.0, 1.1)
    show()

