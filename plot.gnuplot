set terminal pngcairo enhanced font "arial,10" fontscale 1.0 size 600, 400
set output 'plot.png'
set logscale y 10
set title 'Miller-rabin'
set xlabel 'Bits'
set ylabel 'Seconds'
plot [3:17] 'brute-force-miller.dat' with lines, 'pollard-rho-miller.dat' with lines