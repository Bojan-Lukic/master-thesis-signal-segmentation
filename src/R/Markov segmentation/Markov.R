rm(list=ls())

library(MHMMR)

# setwd("C:\\Users\\bojan\\Desktop\\Studium Master WS21\\masterarbeit\\Python implementation\\Test signals and benchmarks")
# setwd("C:\\Users\\bojan\\Desktop\\Studium Master WS21\\masterarbeit\\Python implementation\\Machine learning segmentation")
setwd("C:\\Users\\bojan\\Desktop\\Studium Master WS21\\masterarbeit\\Python implementation\\Markov segmentation")
y <- t(read.table("filtered_processes.txt", sep=" "))
# y <- t(read.table("outfile2.txt", sep=" "))
x <- seq(1, length(y[, 1]), by=1)

matplot(x, y, type = "l", xlab = "x", ylab = "Y", lty = 1)

K <- 6 # Number of regimes (states)
p <- 1 # Dimension of beta (order of the polynomial regressors)
variance_type <- "heteroskedastic" # "heteroskedastic" or "homoskedastic" model

n_tries <- 1
max_iter <- 1500
threshold <- 1e-6
verbose <- TRUE

mhmmr <- emMHMMR(X = x, Y = y, K, p, variance_type, n_tries, 
                 max_iter, threshold, verbose)

mhmmr$summary()

mhmmr$plot(what = c("smoothed", "regressors", "loglikelihood"))


# names(unclass(mhmmr))
# names(unclass(mhmmr$stat))
K <- 4 # Number of regimes (states)
mhmmr <- emMHMMR(X = x, Y = y, K, p, variance_type, n_tries, 
                 max_iter, threshold, verbose)
mhmmr$stat$klas
