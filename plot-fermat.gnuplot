set terminal pngcairo enhanced font "arial,10" fontscale 1.0 size 600, 400
set output 'plot-fermat.png'
set logscale y 10
set title 'Fermat'
set xlabel 'Bits'
set ylabel 'Seconds'
plot [3:17] 'brute-force-fermat.dat' with lines, 'pollard-rho-fermat.dat' with lines