#Canvas options
set term pdf
set out "3-gnuplot.pdf"

#Basic options
set title "Plot in gnuplot" font ",10"
set xlabel "x"
set ylabel "f(x)"
set xrange [-pi:pi]
set yrange [-1:1]
set xtics (-pi, -pi/2, 0, pi/2, pi)
set ytics (-1, 0, 1)

#More options
set grid
set key rmargin box

#Plot
p sin(x) t "sin(x)" w l lt 1 lw 2, sin(2*x) t "sin(2*x)" w l lt 2 lw 2, sin(3*x) t "sin(3x)" w l lt 3 lw 2, sin(4*x) t "sin(4x)" w l lt 4 lw 2

