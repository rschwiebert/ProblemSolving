#!/usr/bin/perl
# https://projecteuler.net/problem=1

use warnings;
use strict;

my $total = 0;
my $i = 0;

foreach $i (1..1000){
    if ($i%3 == 0){
        $total += $i;
    } elsif ($i%5 == 0) {
        $total += $i;
    }
}

print "The answer is: $total\n";

exit;
