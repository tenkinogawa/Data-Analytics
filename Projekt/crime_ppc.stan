generated quantities {
    real mu = normal_rng(4359, 1703);
    real sigma = exponential_rng(1703);
    real crime_all_prior = normal_rng(mu, sigma);
}