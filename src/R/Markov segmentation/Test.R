function (X, Y, K, p = 3, variance_type = c("heteroskedastic", 
    "homoskedastic"), n_tries = 1, max_iter = 1500, threshold = 1e-06, 
    verbose = FALSE) 
{
    if (is.vector(Y)) {
        Y <- as.matrix(Y)
    }
    mData <- MData$new(X, Y)
    nb_good_try <- 0
    total_nb_try <- 0
    best_loglik <- -Inf
    while (nb_good_try < n_tries) {
        if (n_tries > 1 && verbose) {
            message("EM try number: ", nb_good_try + 1, 
                "\n")
        }
        total_nb_try <- total_nb_try + 1
        variance_type <- match.arg(variance_type)
        param <- ParamMHMMR$new(mData = mData, K = K, p = p, 
            variance_type = variance_type)
        param$initParam(nb_good_try + 1)
        iter <- 0
        prev_loglik <- -Inf
        converged <- FALSE
        top <- 0
        stat <- StatMHMMR$new(paramMHMMR = param)
        while ((iter <= max_iter) && !converged) {
            stat$EStep(param)
            param$MStep(stat)
            iter <- iter + 1
            lambda <- 1e-05
            stat$loglik <- stat$loglik + log(lambda)
            if (verbose) {
                message("EM - MHMMR: Iteration: ", iter, 
                  " | log-likelihood: ", stat$loglik)
            }
            if ((prev_loglik - stat$loglik) > 1e-04) {
                top <- top + 1
                if (top == 10) {
                  warning("EM log-likelihood is decreasing from ", 
                    prev_loglik, "to ", stat$loglik, "!")
                }
            }
            converged <- (abs(stat$loglik - prev_loglik)/abs(prev_loglik) < 
                threshold)
            if (is.na(converged)) {
                converged <- FALSE
            }
            prev_loglik <- stat$loglik
            stat$stored_loglik <- c(stat$stored_loglik, stat$loglik)
        }
        if (n_tries > 1 && verbose) {
            message("Max value of the log-likelihood: ", 
                stat$loglik, "\n\n")
        }
        if (length(param$beta) != 0) {
            nb_good_try <- nb_good_try + 1
            total_nb_try <- 0
            if (stat$loglik > best_loglik) {
                statSolution <- stat$copy()
                paramSolution <- param$copy()
                best_loglik <- stat$loglik
            }
        }
        if (total_nb_try > 500) {
            stop("can't obtain the requested number of classes")
        }
    }
    if (n_tries > 1 && verbose) {
        message("Best value of the log-likelihood: ", statSolution$loglik, 
            "\n")
    }
    statSolution$MAP()
    statSolution$computeStats(paramSolution)
    return(ModelMHMMR(param = paramSolution, stat = statSolution))
}