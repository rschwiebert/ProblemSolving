#!/usr/bin/perl
# https://projecteuler.net/problem=7

# What is the 10 001st prime number?
# I would have liked to use a sieve, but it seems bad to have to specify
# how long the array containing the sieve is. In this method, no choice is made.

use warnings;
use strict;

my @primes = (2,3,5);
my $i = 6;

sub divisorCheck{
    # simple check for the existence of a prime divisor
    # last element of input array is the candidate
    # the other elements are known primes
    # return 1 if prime, 0 otherwise
    my $candidate = $_[-1];
    my $limit = $candidate ** 0.5;
    my $j = 0;
    
    while ($_[$j] <= $limit){
        if ($candidate % $_[$j] == 0){
            return 0;
        } else {
            $j++;
        }
    }
    return 1;
}

while (($#primes) < 10000){
    if (&divisorCheck((@primes,$i)) == 1){
        push @primes,$i;
    } 
    $i++;
}

my $answer = $primes[-1];
print "The answer is: $answer\n";

exit;
