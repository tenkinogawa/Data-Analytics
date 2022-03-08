data {
    int N;
    int y[N];
}
parametars {
    real<lower=0, upper=1> theta;
}
model {
    theta ~ beta(1,1); 
    y ~ bernoulli(theta);
}